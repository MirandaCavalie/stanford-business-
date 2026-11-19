# Crewbase Copilot: from scattered contacts to AI-guided event planning

**Team:** Miranda Cavalie, Alejandro Gonzalez · **Business:** Crewbase Collective (San Francisco) · **Built on:** Converge.AI (Enter, Covey, Framia)
**Prototype:** https://da946762214b46049c66aa2e3a5f9580.live-preview.enter.pro

## The problem
Crewbase runs AI hackathons, founder mixers and demo nights. It is one month old and one person runs venues, judges and sponsors. Its real asset is the relationship network: who sponsored, judged, spoke or hosted, and at which event. That network lives in Excel sheets, WhatsApp chats, LinkedIn and the organizer's memory.
- **From the organizer interview:** the slowest step is adding new people. For every event he types each judge, sponsor and speaker into his admin portal one record at a time: about 15 judges per event, each with name, email, username, LinkedIn and image.
- **From Crewbase's own public data:** 2 duplicate profiles, typos like "Synk" and "NVDIA", 76 of 116 organizations with no description, and a data health score of 18/100.
- **Choosing partners depends on memory.** 16 sponsor entries list a contact who works at a different company. Several look like connectors who brought the sponsor in, but nothing records that.

## The solution
Crewbase Copilot turns 21 events, 116 organizations, 114 people and 517 participations into a living network and uses it to run the next event, shown on his real one: WinterHack 2026 (Dec 18, AWS Builders Loft). AI suggests and the organizer approves every step; nothing is published or sent automatically.
1. **Add people.** He pastes a WhatsApp thread, Excel rows or LinkedIn links. AI returns one clean row per person, matches it against the network so nobody is entered twice, flags missing fields instead of guessing, and exports in his portal's exact format.
2. **Data Health.** A queue of duplicates, typos and empty fields. AI drafts each fix, he approves it, and every change is logged.
3. **Plan an event.** It ranks sponsors, judges and speakers with a score computed in code and shown in full. AI only writes the one-line reason from real events. The Luma page and cover are built only from the people he accepts.
4. **Comms.** A 4-email sequence per person (invite, logistics, reminder, thank-you), written from their history and sent from his own Gmail, WhatsApp or LinkedIn.
5. **Event day.** Teams submit through a form, judges score on their phones, and each sponsor gets one link with the live demos built on its tool, which is what he already owes sponsors and collects by hand today.
6. **Covey agents.** Crewbase Copilot plans from a chat and Crewbase Growth finds new sponsors and VC judges with sources. Both read the app's live data through a read-only API.

## Expected value
| Metric | Before | After, measured in the app |
|---|---|---|
| New people per event | ~15 judges plus sponsors and speakers, typed one by one | One paste, then review and approve |
| Data health score | 18/100 | Recomputed live as fixes are approved |
| Partner decisions | From memory | Acceptance rate logged per recommendation |
| Luma copy | Rewritten from scratch | Share of the AI draft he keeps, logged per version |
| Outreach | Not tracked | Sent, replied and confirmed, logged per message |

His revenue is sponsor cash or API credits plus judge support fees ($100–500), and VC judges drive attendance. The tool works on the steps that bring that in. He gave no hours for today's process, so we do not claim hours saved; the Impact page projects them once he enters his baseline.

## Feasibility
- **It runs today on his data.** We imported the structured records from his own website; there is no migration, and exports match his portal.
- **Everything is on Converge.** Enter is the app and database, Covey runs the agents, Framia makes the cover. The whole prototype cost about 1,400 credits, not an engineer.
- **Human review everywhere.** Scores are computed in code and auditable. AI writes reasons and drafts only.

## Assumptions and risks
- Contacts listed under another company are treated as connectors; the organizer has not confirmed this yet.
- Recommendations are only as good as the records, which is why Data Health exists.
- Luma push is built but untested until he adds his Luma Plus API key; until then the copy is copy-paste.

## Beyond Crewbase
Any community that runs events, such as other organizers, accelerators or university clubs, can import its past events, people and sponsors and get the same network, cleanup, recommendations and comms. Several of them are already partners in Crewbase's network.
