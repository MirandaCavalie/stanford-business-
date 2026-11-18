"""Normaliza los JSON públicos de crewbasecollective.com en un dataset semilla
(eventos, organizaciones, personas, participaciones) y genera un reporte de calidad.

Uso:
    python3 scripts/build_seed.py
Lee data/raw/ y escribe data/seed/ y data/QUALITY_REPORT.md.
"""
import csv
import difflib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
SEED = ROOT / "data" / "seed"


def norm(s):
    s = (s or "").replace("​", "").strip()
    return re.sub(r"\s+", " ", s)


def key(s):
    return re.sub(r"[^a-z0-9]", "", norm(s).lower())


def li_key(url):
    m = re.search(r"linkedin\.com/in/([^/?#]+)", url or "")
    return m.group(1).lower() if m else None


def load(name):
    return json.loads((RAW / name).read_text())


index = load("events-index.json")["events"]
people_raw = load("people.json")["people"]
sponsors_raw = load("sponsors.json")

events, orgs, people, parts = [], {}, {}, []


def org(name, website=None, logo=None, description=None, kind=None):
    k = key(name)
    if not k:
        return None
    o = orgs.setdefault(k, {"id": k, "name": norm(name), "website": None, "logo": None,
                            "description": None, "kinds": set(), "name_variants": set()})
    o["name_variants"].add(norm(name))
    o["website"] = o["website"] or website
    o["logo"] = o["logo"] or logo
    o["description"] = o["description"] or (norm(description) or None)
    if kind:
        o["kinds"].add(kind)
    return k


def person(name, linkedin=None, title=None, company=None):
    k = li_key(linkedin) or key(name)
    p = people.setdefault(k, {"id": k, "name": norm(name), "linkedin": linkedin, "title": None,
                              "company": None, "name_variants": set(), "title_variants": set(),
                              "company_variants": set()})
    p["name_variants"].add(norm(name))
    if title:
        p["title_variants"].add(norm(title))
        p["title"] = p["title"] or norm(title)
    if company:
        p["company_variants"].add(norm(company))
        p["company"] = p["company"] or norm(company)
        org(company)
    return k


for e in index:
    d = json.loads((RAW / "events" / f"{e['slug']}.json").read_text())
    ev = d["event"]
    events.append({
        "id": ev["slug"], "name": norm(ev["name"]), "type": ev["type"], "date": ev["eventDate"],
        "end_date": ev["endDate"], "start_time": ev["startTime"], "end_time": ev["endTime"],
        "location": norm(ev["location"]), "description": norm(ev["description"]),
        "theme": norm(ev["theme"]), "cover": ev["coverImageUrl"],
        "luma_links": ev.get("lumaLinks") or ([ev["lumaLink"]] if ev.get("lumaLink") else []),
        "is_partner_event": ev["isPartnerEvent"],
        "tracks": [{"name": norm(t["name"]), "description": norm(t["description"])} for t in d["tracks"]],
        "prizes": d["prizes"], "schedule_items": len(d["schedule"]), "photos": len(d["photos"]),
    })
    sid = ev["slug"]

    def add(role, pk=None, ok=None, **extra):
        parts.append({"event_id": sid, "role": role, "person_id": pk, "org_id": ok, **extra})

    for s in d["sponsors"]:
        ok = org(s["companyName"], s["companyWebsite"], s["companyLogo"], s["companyDescription"], "sponsor")
        if not s["representatives"]:
            add("sponsor", None, ok)
        for r in s["representatives"]:
            pk = person(r["username"], r["linkedin"], r.get("role"), r.get("companyName"))
            add("sponsor", pk, ok, rep_company=norm(r.get("companyName")))
    for s in d["partners"]:
        kind = s["partnerType"] or "partner"
        ok = org(s["companyName"], s["companyWebsite"], s["companyLogo"], s["companyDescription"], kind)
        if not s["representatives"]:
            add(f"partner:{kind}", None, ok)
        for r in s["representatives"]:
            pk = person(r["username"], r["linkedin"], r.get("role"), r.get("companyName"))
            add(f"partner:{kind}", pk, ok, rep_company=norm(r.get("companyName")))
    for role, lst in [("judge", d["judges"]), ("speaker", d["speakers"]), ("host", d["hosts"]),
                      ("volunteer", d["volunteers"]), ("team", d["team"])]:
        for r in lst:
            pk = person(r["username"], r.get("linkedin"), r.get("title"), r.get("companyName"))
            extra = {"topic": norm(r["topic"])} if role == "speaker" and r.get("topic") else {}
            add(role, pk, key(r.get("companyName")) or None, **extra)

for p in people_raw:
    person(p["username"], p["linkedin"], p["title"], p["companyName"])

for group, kind in [("sponsors", "sponsor"), ("venuePartners", "venue"),
                    ("communityPartners", "community")]:
    for o in sponsors_raw[group]:
        org(o["name"], o.get("website"), o.get("logoUrl"), None, kind)

# ---------- escribir semilla ----------
SEED.mkdir(parents=True, exist_ok=True)


def dump(name, rows):
    rows = [{k: sorted(v) if isinstance(v, set) else v for k, v in r.items()} for r in rows]
    (SEED / f"{name}.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    flat = [{k: (json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v)
             for k, v in r.items()} for r in rows]
    cols = list(dict.fromkeys(k for r in flat for k in r))
    with open(SEED / f"{name}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(flat)


events.sort(key=lambda e: e["date"])
dump("events", events)
dump("organizations", sorted(orgs.values(), key=lambda o: o["name"].lower()))
dump("people", sorted(people.values(), key=lambda p: p["name"].lower()))
dump("participations", parts)

# ---------- reporte de calidad ----------
L = ["# Reporte de calidad de datos de Crewbase", "",
     "Generado por `scripts/build_seed.py` a partir de los JSON públicos de crewbasecollective.com.", ""]
L += ["## Volumen", "",
      f"- Eventos: {len(events)} ({', '.join(f'{v} {k}' for k, v in Counter(e['type'] for e in events).most_common())})",
      f"- Organizaciones únicas: {len(orgs)}",
      f"- Personas únicas: {len(people)} (people.json publica {len(people_raw)})",
      f"- Participaciones (persona u organización × evento × rol): {len(parts)}",
      f"- Participaciones por rol: {dict(Counter(p['role'] for p in parts).most_common())}", ""]

dup_names = [n for n, c in Counter(key(p["username"]) for p in people_raw).items() if c > 1]
L += ["## Duplicados", "", f"**Personas repetidas en people.json:** {len(dup_names)}"]
for n in dup_names:
    rows = [p for p in people_raw if key(p["username"]) == n]
    L.append(f"- {rows[0]['username']}: {len(rows)} registros · LinkedIn: {', '.join(r['linkedin'] or '—' for r in rows)}")
names = sorted(o["name"] for o in orgs.values())
near = set()
for i, a in enumerate(names):
    for b in names[i + 1:]:
        if difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio() > 0.85:
            near.add((a, b))
L += ["", f"**Organizaciones con nombres casi iguales (posibles duplicados o erratas):** {len(near)}"]
L += [f"- \"{a}\" ≈ \"{b}\"" for a, b in sorted(near)]
L += [""]

inc = [p for p in people.values() if len(p["title_variants"]) > 1 or len(p["company_variants"]) > 1]
L += ["## Datos inconsistentes", "",
      f"**Personas con distintos cargos o empresas según el evento:** {len(inc)}"]
for p in inc[:40]:
    L.append(f"- {p['name']}: cargos {sorted(p['title_variants'])} · empresas {sorted(p['company_variants'])}")
mismatch = [x for x in parts if x.get("rep_company") and key(x["rep_company"]) != x["org_id"]]
L += ["", f"**Representantes cuya empresa no coincide con la organización que representan:** {len(mismatch)}"]
for x in mismatch[:30]:
    L.append(f"- {people[x['person_id']]['name']} representa a **{orgs[x['org_id']]['name']}**, pero figura en **{x['rep_company']}** ({x['event_id']})")
bad_li = [p for p in people.values() if p["linkedin"] and not li_key(p["linkedin"])]
L += ["", f"**LinkedIn con formato inválido:** {len(bad_li)}"]
L += [f"- {p['name']}: {p['linkedin']}" for p in bad_li]
L += [""]

L += ["## Campos vacíos", ""]
for label, cond in [("sin descripción", lambda e: not e["description"]),
                    ("sin tema", lambda e: not e["theme"]),
                    ("sin link de Luma", lambda e: not e["luma_links"])]:
    miss = [e["name"] for e in events if cond(e)]
    L.append(f"- Eventos {label}: **{len(miss)}/{len(events)}**")
for label, field in [("sin descripción", "description"), ("sin logo", "logo"), ("sin website", "website")]:
    miss = [o for o in orgs.values() if not o[field]]
    L.append(f"- Organizaciones {label}: **{len(miss)}/{len(orgs)}**")
for label, field in [("sin LinkedIn", "linkedin"), ("sin cargo", "title"), ("sin empresa", "company")]:
    miss = [p for p in people.values() if not p[field]]
    L.append(f"- Personas {label}: **{len(miss)}/{len(people)}**")
no_rep = [x for x in parts if x["role"] == "sponsor" and not x["person_id"]]
L.append(f"- Sponsors sin un contacto asignado: **{len(no_rep)}**")
L += [""]

rep = Counter()
for x in parts:
    if x["role"] == "sponsor" and x["org_id"]:
        rep[x["org_id"]] += 1
L += ["## Lo que la red ya permite (insumo para las recomendaciones)", "",
      "**Organizaciones que más veces fueron sponsor:**"]
L += [f"- {orgs[k]['name']}: {c} eventos" for k, c in rep.most_common(10)]
pc = defaultdict(set)
for x in parts:
    if x["person_id"]:
        pc[x["person_id"]].add(x["event_id"])
L += ["", "**Personas que más se repiten entre eventos:**"]
L += [f"- {people[k]['name']} ({people[k]['title']}, {people[k]['company']}): {len(v)} eventos"
      for k, v in sorted(pc.items(), key=lambda kv: -len(kv[1]))[:12]]
(ROOT / "data" / "QUALITY_REPORT.md").write_text("\n".join(L) + "\n")
print("\n".join(L))
