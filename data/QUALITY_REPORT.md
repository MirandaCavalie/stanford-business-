# Reporte de calidad de datos de Crewbase

Generado por `scripts/build_seed.py` a partir de los JSON públicos de crewbasecollective.com.

## Volumen

- Eventos: 21 (7 hackathon, 7 mixer, 3 demo, 3 workshop, 1 pitch_competition)
- Organizaciones únicas: 116
- Personas únicas: 114 (people.json publica 114)
- Participaciones (persona u organización × evento × rol): 517
- Participaciones por rol: {'judge': 147, 'sponsor': 127, 'host': 113, 'speaker': 77, 'partner:community': 33, 'partner:venue': 16, 'volunteer': 4}

## Duplicados

**Personas repetidas en people.json:** 1
- Ali Amjad: 2 registros · LinkedIn: https://www.linkedin.com/in/ali-amjad-a80732137/, https://www.linkedin.com/in/ali-amjad-a80732137a

**Organizaciones con nombres casi iguales (posibles duplicados o erratas):** 1
- "Sartorial" ≈ "Satorial"

## Datos inconsistentes

**Personas con distintos cargos o empresas según el evento:** 0

**Representantes cuya empresa no coincide con la organización que representan:** 16
- Colin Lowenberg representa a **Tenki**, pero figura en **Nebius** (universal-hackathon-mvebl5cy)
- Merve Isler representa a **Marvellous**, pero figura en **AI Builders** (universal-hackathon-mvebl5cy)
- Colin Lowenberg representa a **Tenki**, pero figura en **Nebius** (zero-human-startup-hackathon-mvd90q80)
- Colin Lowenberg representa a **Tenki**, pero figura en **Nebius** (build-your-co-founder-hackathon-mvd95cmu)
- Colin Lowenberg representa a **AISA One**, pero figura en **Nebius** (build-your-co-founder-hackathon-mvd95cmu)
- Saurabh Khire representa a **Kylon**, pero figura en **Crewbase Collective** (buildfest-demos-and-challenges-muj6rws3)
- Colin Lowenberg representa a **Tenki**, pero figura en **Nebius** (buildfest-demos-and-challenges-muj6rws3)
- Martina Beg representa a **Finchip AI**, pero figura en **Abaka AI** (buildfest-demos-and-challenges-muj6rws3)
- Saurabh Khire representa a **Replit**, pero figura en **Crewbase Collective** (design-deploy-workshop-ms5mfqce)
- Colin Lowenberg representa a **Tavily**, pero figura en **Nebius** (bay-builders-hackathon-ms5sgpk3)
- Aviral Bharadwaj representa a **RocketRide**, pero figura en **Devnovate** (bay-builders-hackathon-ms5sgpk3)
- Saurabh Khire representa a **Govia**, pero figura en **Crewbase Collective** (bay-builders-hackathon-ms5sgpk3)
- Colin Lowenberg representa a **Tavily**, pero figura en **Nebius** (wizard-hackathon-ms5th4d3)
- Saurabh Khire representa a **Homebrew Club**, pero figura en **Crewbase Collective** (wizard-hackathon-ms5th4d3)
- Rene Turcios representa a **Opsera**, pero figura en **Replit** (applied-ai-intelligence-hackathon-ms5uf6tt)
- Colin Lowenberg representa a **Tavily**, pero figura en **Nebius** (applied-ai-intelligence-hackathon-ms5uf6tt)

**LinkedIn con formato inválido:** 0

## Campos vacíos

- Eventos sin descripción: **2/21**
- Eventos sin tema: **15/21**
- Eventos sin link de Luma: **17/21**
- Organizaciones sin descripción: **76/116**
- Organizaciones sin logo: **42/116**
- Organizaciones sin website: **43/116**
- Personas sin LinkedIn: **0/114**
- Personas sin cargo: **0/114**
- Personas sin empresa: **0/114**
- Sponsors sin un contacto asignado: **12**

## Lo que la red ya permite (insumo para las recomendaciones)

**Organizaciones que más veces fueron sponsor:**
- Finchip AI: 11 eventos
- InsForge: 10 eventos
- Kylon: 9 eventos
- Nebius: 6 eventos
- RocketRide: 5 eventos
- Tenki: 4 eventos
- AdaL: 4 eventos
- Paritok: 4 eventos
- Synk: 4 eventos
- Ask the W: 4 eventos

**Personas que más se repiten entre eventos:**
- Saurabh Khire (Founder, Crewbase Collective): 21 eventos
- Ayush Ojha (Devrel, Wasmer): 17 eventos
- Amitabh Das (Founder, Agent OS): 13 eventos
- Abhi Vasanth (Senior Data Engineer, Pacific Gas and Electric Company): 13 eventos
- Colin Lowenberg (DevRel, Nebius): 8 eventos
- Pramod Thebe (Co-Founder, Hi Tuto): 8 eventos
- Vince Kohli (Strategic Advisor, Google Deepmind): 7 eventos
- Christina Bowllan (Founding Team, Kylon): 6 eventos
- Chelsey Huang (Co-Founder, Finchip AI): 6 eventos
- Merve Isler (Ecosystem Builder, AI Builders): 6 eventos
- Tony Chwang (Co Founder, InsForge): 6 eventos
- Aviral Bharadwaj (Founder, Devnovate): 5 eventos
