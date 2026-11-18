# Call with Saurabh Khire (Crewbase Collective): Tue Nov 17, 10 PM PT

**Goal:** leave with (1) baseline numbers for the "before" (business impact is 40% of the score), (2) his #1 priority, and (3) a yes/no on whether he'd actually use this. We have 15–20 minutes, so ask little and listen a lot.

---

## Context: what we should know going in

### The challenge
- **Smarter Event Operations: From Partner Records to AI-Guided Event Planning.**
- He described three pains:
  1. Repetitive manual entry for every event: description, cover, partner logos, profiles and photos. Even reused data ends up inconsistent.
  2. Picking partners, investors and judges depends on his memory and network. History, interests and themes aren't organized.
  3. Adapting the event into Luma copy is a repeated, manual task.
- Expected outcome: event and stakeholder data becomes **reusable organizational knowledge**. It is used to **plan partnerships** and **improve event communication**, and the organizer **reviews and edits** everything the AI suggests.
- Suggested metrics:
  - Prep time and repeated entry steps
  - Record completeness
  - Recommendation acceptance rate and outreach response
  - Copy review time and Luma registration conversion

### Crewbase today (from crewbasecollective.com)
- A Bay Area builder/founder community running hackathons, pitch competitions, workshops, demo nights and mixers.
- Their site already exposes structured public JSON for events, people and sponsors. We pulled all of it:

| Data | Count |
|---|---|
| Events (May–Oct 2026) | 21: 7 hackathons, 7 mixers, 3 demo nights, 3 workshops, 1 pitch |
| Organizations | 116 |
| People | 114 |
| Participations (who did what, at which event, in which role) | 517 |

- Recurring venues: Homebrew Club, AWS Builders Loft, Frontier Tower, Sports Basement, plus one in Santa Clara.
- Channels: a Luma calendar, Discord, LinkedIn and events@crewbasecollective.com. WhatsApp and X are "coming soon".
- "Get Involved" forms: sponsor, judge/speaker, partner, member/host, volunteer.
- Most frequent sponsors: Finchip AI (11 events), InsForge (10), Kylon (9), Nebius (6).
- Most frequent people: Ayush Ojha (17 events), Amitabh Das and Abhi Vasanth (13 each).

### Data quality findings (direct evidence of pain #1)
- **Duplicates:** Ali Amjad appears twice. Sartorial vs. Satorial.
- **Typos:** "Synk" (Snyk), "NVDIA", "Heat of GTM", "Ambdassedor", "Grwth".
- **Missing fields:**
  - 76 of 116 orgs have no description, 42 have no logo and 43 have no website.
  - 15 of 21 events have no theme and 17 of 21 have no Luma link.
  - 12 sponsor slots have no contact person.
- **16 "representative mismatches":** the contact listed for a sponsor works somewhere else.
  - Colin Lowenberg (Nebius) is listed for Tenki and Tavily.
  - Saurabh himself is listed for Kylon, Replit, Govia and Homebrew Club.
  - Either these are errors, or they are **connectors** who brought the sponsor in. That's very valuable for recommendations.
- Overall data health score in our app: **18/100, with 213 open issues.**

### What we've already built (all on Converge: Enter + Enter Cloud + AI All)
Live at https://da946762214b46049c66aa2e3a5f9580.prod.enter.pro. Anyone can browse; edits need an organizer passcode.
1. **Network:** every person and org with their full event history.
2. **Data Health:**
   - A fix queue covering duplicates, typos, empty fields and mismatches.
   - "Suggest with AI" drafts a fix, a human approves it, and every change is logged with before/after.
3. **Plan an event → Recommendations:**
   - Takes a brief, e.g. "AI Agents Hackathon, Dec 12, Frontier Tower, 80 builders".
   - Ranks the top 8 sponsors, judges and speakers with a transparent score: theme fit, role experience, recency, frequency, connector bonus, minus fatigue if asked less than 3 weeks ago.
   - Each card has a one-line reason grounded in real events.
   - Accept/dismiss is logged, which gives us the acceptance-rate metric.
   - Example: Colin Lowenberg ranks #1 for judge (90). He judged 4 hackathons and brought in Tenki, AISA One and Tavily as sponsors.
4. **Luma copy studio:** in progress right now. It drafts from the brief and the accepted shortlist, never invents sponsors or prizes, and adds a quality checklist, editing and copy-to-Luma.

### What we still don't know (what this call is for)
- How long one event takes him today, and which step hurts most.
- How he really chooses and drops partners, and what a sponsor brings: money, credits or a venue.
- Whether the mismatches are errors or connectors.
- How his website is updated, and whether he has Luma Plus (API).
- Where he spends his day: WhatsApp, Discord, Gmail or Slack.
- His #1 priority.

---

## Questions

### 0. Opening (1 min)
"We pulled your public site data: 21 events, 116 organizations, 114 people and 517 participations. Your data is already structured, so we're building on top of it instead of starting from zero. We'd love 15 minutes to make sure we're solving the right problem."

### 1. Baseline: the "before" numbers (most important)
1. From the moment you decide to run an event until it's live on Luma, **how many hours does it take in total?** How many of those are manual work, like entering data, logos, bios and copy?
2. **Which step is the slowest or most annoying?**
3. Do you do this alone? How many people help on the operations side?
4. For a big hackathon, **how many sponsors or judges do you reach out to** to land the ones who confirm? How many reply?
5. **How long does writing the Luma page take?** Do you rewrite it several times?

### 2. How he decides who to invite (feeds the recommendations)
6. When you plan a new event, **how do you pick** sponsors, judges and investors? What makes someone a good fit?
7. **Why do you stop inviting someone?** No reply, asked too often, wrong theme, a bad experience?
8. What does a sponsor usually bring: **cash, credits or a venue**? Are sponsors your main source of revenue?
9. Is there anything you wish you tracked about each contact but don't today? For example replies, amounts, notes, or how many times you've asked them.

### 3. Validate what we found in his data
10. In 16 cases **the contact listed for a sponsor works at a different company**. For example, Colin Lowenberg from Nebius is listed for Tenki and Tavily, and you're listed for Replit, Kylon and Homebrew. **Is that a data error, or is that the person who brought the sponsor in?**
11. 76 of 116 organizations have no description, 15 of 21 events have no theme and 17 have no Luma link. **Does that info live somewhere else, or does it just never get entered?**
12. Ali Amjad appears twice, and there are typos like "Synk" and "Sartorial/Satorial". **How often do you end up fixing things like that?**

### 4. His tools and workflow
13. **How do you add events and people to your website?** Is there an admin panel? Did you build it? What database does it use?
14. Do you have **Luma Plus** (it has an API)? What were your **best and worst events** by registrations?
15. **Where do you spend your day: WhatsApp, Discord, Gmail or Slack?** That's where an assistant should live.
16. How do the **Get Involved form** submissions reach you, and what do you do with them?

### 5. Live demo check (3–4 min, screen share)
Demo path: https://da946762214b46049c66aa2e3a5f9580.prod.enter.pro
1. **Home:** "This is your network: 21 events, 116 orgs, 114 people, 517 participations. Data health is 18/100 today."
2. **Data Health:** show the Ali Amjad duplicate and the "Synk" typo with a one-click fix.
3. **Plan an event → AI Agents Hackathon → Recommendations:** Colin Lowenberg is #1 judge (90). He judged 4 hackathons and brought in Tenki, AISA One and Tavily.
4. **Luma copy → Cover → Outreach:** a draft page, a cover with real sponsor logos, and personal invite drafts. Nothing is sent or published automatically.
5. **Covey agent "Crewbase Copilot":** type "Let's plan our next hackathon" and show the same flow inside a chat.

Questions while demoing:

17. On Recommendations: **"Would you invite these 8 judges? Who's missing, and who would you never invite?"** Write his answer down word for word. It's a quote for the video and a validation of the scoring.
18. The agent noticed that Colin and Tony Chwang are also sponsors: **"Do you keep judges independent from sponsors?"**
19. On Data Health: "Is this the kind of cleanup you'd actually approve?"
20. On Outreach: "Would you send something like this? Over email, LinkedIn or WhatsApp?"

### 6. Priority and close
21. **If we could solve only one thing by Friday, what would it be:** the unified database, the recommendations or the Luma copy?
22. If it works, **would you use it for your next event?** Would you recommend it to other organizers, like AI Collective or BuildClub?
23. **Can we quote or mention you in the demo?** Do you have an upcoming event we can use as the example?

---

## What to write down (goes into PLAN.md afterwards)
| Metric | His answer |
|---|---|
| Hours per event today | |
| Slowest step | |
| Sponsors contacted / confirmed | |
| Time to write the Luma copy | |
| Mismatches: error or connector? | |
| Reaction to the top 8 judges | |
| #1 priority | |
| Channel where he works | |
| Luma Plus? | |
| Quote for the demo | |
