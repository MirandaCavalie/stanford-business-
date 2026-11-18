# Crewbase Copilot: from partner records to AI-guided event planning

**Team:** Miranda Cavalie · **Business:** Crewbase Collective (San Francisco) · **Built on:** Converge.AI (Enter, Covey, Framia)
**Prototype:** https://da946762214b46049c66aa2e3a5f9580.prod.enter.pro

## The problem
Crewbase runs AI hackathons, founder mixers, workshops and demo nights. Its real asset is the relationship network: who sponsored, judged, spoke or hosted, and at which event. Today that network lives in scattered records and in the organizer's memory.
- **Every event means re-entering the same data.** Descriptions, logos and bios get typed again, and the records end up inconsistent. In Crewbase's own public data we found:
  - 2 duplicate profiles and typos like "Synk" and "NVDIA".
  - 76 of 116 organizations with no description, and 15 of 21 events with no theme.
  - A data health score of **18/100**.
- **Choosing partners depends on memory.** 16 sponsor contacts actually belong to other companies: they are the connectors who bring sponsors in, but nothing records that.
- **The Luma page is rewritten from scratch every time.**
- Baseline from the organizer: **[X] hours per event**, **[Y] hours on Luma copy**, **[Z] sponsors contacted for every one that confirms**.

## The solution
Crewbase Copilot turns 21 events, 116 organizations, 114 people and 517 participations into a living network and uses it to plan the next event. AI suggests and the organizer approves every step.
1. **Data Health:**
   - A queue of duplicates, typos and empty fields.
   - AI drafts each fix and the organizer approves it in one click.
   - Every change is logged with before and after.
2. **Plan an event → explainable recommendations:**
   - From a brief, it ranks sponsors, judges and speakers with a transparent score: theme fit, role experience, recency, frequency, a connector bonus, and a penalty for asking the same person too often.
   - Each candidate gets a one-line reason grounded in real events, e.g. *"Colin Lowenberg judged 4 Crewbase hackathons and brought Tenki, AISA One and Tavily in as sponsors."*
3. **Luma copy, cover and outreach:**
   - The Luma page is drafted only from the accepted partners, in Crewbase's own voice, with unknowns left as [TBD] and a quality checklist.
   - A Framia-generated cover carries the real sponsor logos.
   - Personal invite drafts cite each person's history with Crewbase. Nothing is published or sent automatically.
4. **Covey agent:** "Crewbase Copilot" runs the same flow from a chat: "Let's plan our next hackathon."

## Expected value (how we measure it)
| Metric | Before | After (measured in the app) |
|---|---|---|
| Hours to prepare an event | [X] | [from Impact page] |
| Data health score | 18/100 | [live] |
| Recommendation acceptance rate | n/a | [logged per decision] |
| Luma copy kept vs. edited | n/a | [logged per version] |
| Outreach: sent → replied → confirmed | [Z] | [logged per draft] |

Sponsors are Crewbase's revenue. Better-matched invites and connector-aware recommendations go straight at the step that brings in money.

## Feasibility
- **It runs today on Crewbase's existing data.** We imported the structured JSON from its own website, so there is no migration.
- **Everything is on Converge:**
  - Enter is the app and the database.
  - Covey runs the agent.
  - Framia makes the creative.
- **Costs are credits, not engineers.** The whole prototype used about 500 credits.
- **There is human review everywhere.** Scores are computed in code, so they are auditable. AI only writes reasons and drafts.

## Assumptions and risks
- **Contacts from other companies are connectors.** [Confirmed or not by the organizer.]
- **The quality of recommendations depends on how complete the records are.** The Data Health module exists for this reason.
- **Luma has no plugin, so publishing stays copy-paste.** Covey's Browser Use could automate it later.

## Beyond Crewbase
Any community that runs events, such as other organizers, accelerators or university clubs, can import its past events, people and sponsors. It gets the same network, data health, partner recommendations and copy. Every organizer's memory becomes reusable knowledge.
