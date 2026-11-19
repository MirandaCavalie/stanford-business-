# Crewbase Copilot: from partner records to AI-guided event planning

**Team:** Miranda Cavalie, Alejandro Gonzalez · **Business:** Crewbase Collective (San Francisco) · **Built on:** Converge.AI (Enter, Covey, Framia)
**Prototype:** https://da946762214b46049c66aa2e3a5f9580.live-preview.enter.pro

## The problem
Crewbase runs AI hackathons, founder mixers, workshops and demo nights. Its real asset is the relationship network: who sponsored, judged, spoke or hosted, and at which event. Today that network lives in scattered records and in the organizer's memory.
- **Every event means re-entering the same data.** Descriptions, logos and bios get typed again, and the records end up inconsistent. In Crewbase's own public data we found:
  - 2 duplicate profiles and typos like "Synk" and "NVDIA".
  - 76 of 116 organizations with no description, and 15 of 21 events with no theme.
  - A data health score of **18/100**.
- **Choosing partners depends on memory.** 16 sponsor entries list a contact who works at a different company. Several look like connectors who brought the sponsor in (one person appears on 8 of them), but nothing records that.
- **The Luma page is rewritten from scratch every time.**
- **From the organizer interview:** the slowest step is adding new people. For every event he types each judge, sponsor and speaker into his admin portal one record at a time (about 15 judges per event: name, email, username, LinkedIn and image), pulling contact details from Excel sheets, WhatsApp chats and LinkedIn. He runs venues, judges and sponsors alone, and Crewbase is about a month old.

## The solution
Crewbase Copilot turns 21 events, 116 organizations, 114 people and 517 participations into a living network and uses it to run the next event, shown on his real one: WinterHack 2026 (Dec 18, AWS Builders Loft). AI suggests and the organizer approves every step; nothing is published or sent automatically.
1. **Add people, his #1 pain.** He pastes a WhatsApp thread, Excel rows or LinkedIn links. AI turns them into one clean row per person, matches them against the network so nobody is entered twice, flags missing fields instead of guessing, and exports in his portal's exact format.
2. **Data Health.** A queue of duplicates, typos and empty fields. AI drafts each fix, he approves it, and every change is logged.
3. **Plan an event.** From a brief, it ranks sponsors, judges and speakers with a score computed in code and shown in full (theme fit, role experience, recency, frequency, connector bonus). AI only writes the one-line reason, e.g. *"Colin Lowenberg judged 4 Crewbase hackathons and brought Tenki, AISA One and Tavily in as sponsors."* The Luma page and cover are built only from the people he accepts.
4. **Comms.** A 4-email sequence per judge, sponsor or speaker (invite, logistics, reminder, thank-you), written from that person's history and sent from his own Gmail, WhatsApp or LinkedIn. Sent, replied and confirmed are tracked.
5. **Event day.** Teams submit through a public form, judges score on their phones, and each sponsor gets one link with the live demos built on its tool, which is what he already owes sponsors and collects by hand today.
6. **Covey agents.** Crewbase Copilot plans from a chat and Crewbase Growth finds new sponsors and VC judges with sources. Both read the app's live data through a read-only API with no contact details.

## Expected value (how we measure it)
| Metric | Before | After (measured in the app) |
|---|---|---|
| Records typed by hand per event | ~15 judges + sponsors + speakers, one by one | One paste, then review and approve |
| Hours to prepare an event | Not measured yet; the organizer enters it on the Impact page | Projected on the Impact page once he does |
| Data health score | 18/100 | Recomputed live as fixes are approved |
| Recommendation acceptance rate | n/a | Logged per decision |
| Luma copy kept vs. edited | n/a | Logged per version |
| Outreach: sent → replied → confirmed | Not tracked today | Logged per draft |

Revenue comes from sponsors (cash or API credits) and from judge support fees ($100–500), and VC judges drive attendance. Recommendations flag investor and big-name judges, and outreach is tracked to confirmation, so the tool works on the steps that bring in money.

## Feasibility
- **It runs today on Crewbase's existing data.** We imported the structured JSON from its own website, so there is no migration.
- **Everything is on Converge:**
  - Enter is the app and the database.
  - Covey runs the agent.
  - Framia makes the creative.
- **Costs are credits, not engineers.** The whole prototype used about 1,400 credits.
- **There is human review everywhere.** Scores are computed in code, so they are auditable. AI only writes reasons and drafts.

## Assumptions and risks
- **Contacts listed under other companies are treated as connectors.** Not yet confirmed by the organizer.
- **The quality of recommendations depends on how complete the records are.** The Data Health module exists for this reason.
- **Luma push is built but not yet tested.** It needs his Luma Plus API key; until he adds it, the approved copy is copy-paste.

## Beyond Crewbase
Any community that runs events, such as other organizers, accelerators or university clubs, can import its past events, people and sponsors. It gets the same network, data health, partner recommendations and copy. Every organizer's memory becomes reusable knowledge.
