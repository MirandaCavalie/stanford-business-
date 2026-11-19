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
- **From the organizer interview:** the slowest step is adding new people. For every event he types each judge, sponsor and speaker into his admin portal one record at a time (about 15 judges per event: name, email, username, LinkedIn and image), pulling contact details from Excel sheets, WhatsApp chats and LinkedIn. He runs venues, judges and sponsors alone, and Crewbase is about a month old.

## The solution
Crewbase Copilot turns 21 events, 116 organizations, 114 people and 517 participations into a living network and uses it to plan the next event (shown on his real one: WinterHack 2026, Dec 18, AWS Builders Loft). AI suggests and the organizer approves every step.
0. **Smart intake, his #1 pain:** paste a WhatsApp thread, Excel rows or LinkedIn links. AI turns them into clean records, matches them against the network so nobody is entered twice, and exports them in his portal's exact format.
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
4. **Comms, his networking pain:**
   - Pick an event and a group (for example, WinterHack's judges) and get a 4-email sequence per person: invite, confirmation with logistics, day-before reminder, and thank-you with results.
   - Each email is personalized from that person's history with Crewbase.
   - Messages go out from his own channels, never in bulk through Luma: Gmail drafts, WhatsApp with the text prefilled, or LinkedIn with the message copied. Sent, replied and confirmed are tracked.
5. **Event day:**
   - Teams submit through a public form.
   - Judges score on their phones and the organizer sees a live leaderboard.
   - Each sponsor gets a report with the projects that used its tool, demo links and scores, which is exactly the deliverable sponsors pay for.
6. **Revenue and Luma:**
   - Sponsor cash, API credits and judge support fees are tracked per event.
   - Approved copy can be pushed to Luma through his Luma Plus API, and registrants imported back.
7. **Two Covey agents:**
   - **Crewbase Copilot** runs the planning flow from a chat ("Let's plan our next hackathon").
   - **Crewbase Growth** finds new sponsors and VC judges with sources, drafts LinkedIn and X launch posts, and finds communities to recruit builders.
   - A scheduled weekly digest flags data fixes and relationships that are cooling down.

## Expected value (how we measure it)
| Metric | Before | After (measured in the app) |
|---|---|---|
| Records typed by hand per event | ~15 judges + sponsors + speakers, one by one | One paste, then review and approve |
| Hours to prepare an event | [not measured yet] | [from Impact page] |
| Data health score | 18/100 | [live] |
| Recommendation acceptance rate | n/a | [logged per decision] |
| Luma copy kept vs. edited | n/a | [logged per version] |
| Outreach: sent → replied → confirmed | Not tracked today | Logged per draft |

Revenue comes from sponsors (cash or API credits) and from judge support fees ($100–500), and VC judges drive attendance. Recommendations flag investor and big-name judges, and outreach is tracked to confirmation, so the tool works on the steps that bring in money.

## Feasibility
- **It runs today on Crewbase's existing data.** We imported the structured JSON from its own website, so there is no migration.
- **Everything is on Converge:**
  - Enter is the app and the database.
  - Covey runs the agent.
  - Framia makes the creative.
- **Costs are credits, not engineers.** The whole prototype used about 500 credits.
- **There is human review everywhere.** Scores are computed in code, so they are auditable. AI only writes reasons and drafts.

## Assumptions and risks
- **Contacts listed under other companies are treated as connectors.** Not yet confirmed by the organizer.
- **The quality of recommendations depends on how complete the records are.** The Data Health module exists for this reason.
- **Luma publishing is copy-paste today.** He has Luma Plus, which has an API, so the approved copy can be pushed through the API next.

## Beyond Crewbase
Any community that runs events, such as other organizers, accelerators or university clubs, can import its past events, people and sponsors. It gets the same network, data health, partner recommendations and copy. Every organizer's memory becomes reusable knowledge.
