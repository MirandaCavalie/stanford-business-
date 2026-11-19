# Plan de ejecución: Crewbase Copilot (Stanford 30×30 · Converge.AI)

**Deadline: miércoles 18 de noviembre, 11:59 PM PT.** Lo enviamos a las 9 PM para tener margen.

## Estado (miércoles 18 de noviembre, 00:15 PT)
- **La llamada con Saurabh ya se hizo** (ver `LLAMADA_RESULTADOS.md`). Su prioridad número uno es cargar a la gente nueva (unos 15 jueces por evento, uno por uno), con contactos dispersos en Excel, WhatsApp y LinkedIn.
- **Incidente (miércoles 18, madrugada):** el hosting de producción de Enter (`*.prod.enter.pro`) corta todas las conexiones (ERR_CONNECTION_RESET), también con dominios inventados. Es una falla de la plataforma, no de nuestra app; volver a publicar no lo arregló. **Link alternativo que funciona sin login:** https://da946762214b46049c66aa2e3a5f9580.live-preview.enter.pro
- **Prototipo publicado:** https://da946762214b46049c66aa2e3a5f9580.prod.enter.pro
- **Proyecto en Enter:** `enter.converge.ai/project/da946762214b46049c66aa2e3a5f9580`
- **Listo, con datos reales en Enter Cloud:**
  - El módulo A (la Red): personas y organizaciones con su historial, y la ficha de cada evento.
  - El módulo B (la Salud de los datos): **health score de 18/100 y 213 problemas abiertos**.
    - 2 duplicados, 2 erratas (NVDIA y Synk), 193 campos vacíos y 16 contactos que no coinciden con su empresa.
    - "Suggest with AI" con aprobación humana.
    - Historial de cambios con el antes y el después.
  - Para mirar no hace falta nada. Para cualquier cambio, incluidos los borradores de IA, se pide un passcode de organizador, que se crea en el primer cambio.
  - El módulo D (Recomendaciones), en la pestaña **Plan an event**:
    - Brief de ejemplo: "AI Agents Hackathon", 12 de diciembre, Frontier Tower, 80 builders.
    - Top 8 de sponsors, jueces y speakers, de una base de 57 sponsors, 78 jueces y 39 speakers.
    - El puntaje se calcula con código, no con IA, y se muestra desglosado: encaje con el tema (0–40), experiencia en el rol (0–25), recencia (0–15), frecuencia (0–10), bonus de conector (0–10) y cansancio (−15).
    - La IA solo etiqueta los temas (146 candidatos, guardados en caché) y escribe la razón en una frase, citando eventos reales.
    - Aceptar, Descartar y "Add someone" quedan registrados en `recommendation_decisions`. El borrador muestra la shortlist y la tasa de aceptación.
    - Ejemplo: Colin Lowenberg (Nebius) sale primero entre los jueces con 90 puntos, porque juzgó 4 veces y trajo sponsors en 8 eventos. Entre los sponsors, el primero es InsForge con 89.
  - El módulo E (Texto para Luma), en la sub-pestaña **Luma copy** de cada borrador:
    - Genera 2 títulos, 2 ganchos, una descripción de 2 o 3 párrafos, la agenda, 3 tracks y las secciones de sponsors y de jueces/speakers con su empresa y cargo. Cierra con el llamado a la acción.
    - Copia el tono de los 3 eventos pasados de Crewbase más parecidos.
    - No inventa nada: lo que falta queda como `[TBD: ...]` y solo lista a los aceptados en la shortlist.
    - Checklist de calidad calculada con código: el ejemplo está en 5 de 9, porque falta la hora.
    - Cada sección se edita, se regenera y se copia por separado, y hay un botón "Copy all for Luma".
    - Cada versión se guarda en `luma_drafts` con el texto original de la IA, para medir cuánto edita el organizador.
    - El brief de ejemplo trae una versión ya generada, con un aviso de que los sponsors y jueces no están confirmados.
  - El módulo F (Portada), en la sub-pestaña **Cover** de cada borrador:
    - **Framia** genera solo el fondo, sin texto, logos ni personas.
    - La app pone encima, con código, el título del texto para Luma, la fecha, la sede, la marca de Crewbase y los logos reales de los sponsors aceptados.
    - Exporta un PNG de 1600×900 con "Download PNG". Hay 2 estilos ("Bold dark" y "Light minimal") y el prompt queda guardado con cada portada.
    - Limitación: Framia solo lo puede usar el agente de Enter, no la app publicada. Por eso la portada de ejemplo es de Framia, pero "Regenerate background" dentro de la app usa el modelo de imágenes de Enter. Para el demo podemos preparar con Framia un set de fondos.
  - El módulo G (el **agente Crewbase Copilot en Covey**):
    - Tiene instrucciones propias, acceso a la web para leer los datos reales (los JSON del repo y el link de la app) y 3 preguntas sugeridas: "Let's plan our next hackathon", "Who brought the most sponsors to Crewbase?" y "What should I fix first in our data?".
    - Probado: "AI agents hackathon, 12 de diciembre, 4 jueces" devolvió una tabla de jueces con el puntaje desglosado y razones con eventos reales. Colin Lowenberg sale primero, igual que en la app.
    - Por su cuenta avisó que Colin y Tony Chwang también son sponsors y propuso cambiarlos por jueces independientes. También señaló problemas de datos sin tocar nada.
    - No tiene plugins: Gmail pide permiso de la cuenta y Enter y Framia no aparecen como plugins del agente.
    - No se puede compartir con link. Para que Saurabh lo use habría que conectarlo como canal (WhatsApp, Slack o Discord).
  - **Mejoras para mostrarle a Saurabh:**
    - **Home** es ahora la página de inicio. Cuenta la historia con los números reales: 21 eventos, 116 organizaciones, 114 personas, 517 participaciones y un health score de 18 con 213 problemas. Muestra los top sponsors, las personas más activas y los 4 pasos del flujo con sus links. La Red pasó a su propia pestaña (`/network`).
    - **Outreach**, la cuarta sub-pestaña de cada borrador:
      - Invitaciones personales por email y por DM: 12 de ejemplo, para 3 sponsors y 3 jueces.
      - Cada una cita la historia real de la persona con Crewbase. Ejemplo para Colin: "You judged the Build your Co Founder Hackathon on September 28…".
      - Hace un pedido claro y sin montos inventados. Cada borrador se edita, se copia y tiene un interruptor "Mark as sent" que queda registrado en `outreach_log`, para medir la tasa de respuesta.
      - Nada se envía desde la app.
    - En la portada, los logos de los sponsors se ven más grandes y parejos (Kylon ya no sale diminuto).
  - **Impact** (`/impact`), la página para el criterio de impacto de negocio (40%):
    - **Antes:** 6 datos que carga el organizador con su passcode (horas por evento, horas para escribir el texto de Luma, horas buscando partners, sponsors contactados y confirmados, eventos por mes). Mientras no los cargue, dicen "Not set yet". No hay números inventados.
    - **Después, medido en vivo:** el health score (de 18 hasta el valor actual), la completitud de los registros, la tasa de aceptación de recomendaciones, cuánto del texto de Luma se queda y cuánto se edita, y el embudo de outreach (borrador → enviado → respondió → confirmó).
    - **Proyección:** las horas ahorradas por evento y por año, con la fórmula a la vista y un supuesto editable (30% por defecto). Solo aparece cuando hay datos del "antes".
    - Una sección "Works beyond Crewbase".
    - En Outreach se sumaron los estados Replied y Confirmed, que quedan registrados.
  - **Módulo H: Add people** (`/add-people`), la respuesta a su prioridad número uno:
    - Se pega texto desordenado (WhatsApp, Excel o links de LinkedIn) y la IA saca una fila por persona: nombre, email, LinkedIn, cargo, empresa y rol.
    - Cada fila se cruza con la red y queda marcada como New, Already in network (con su historial) o Possible duplicate. Los campos que faltan quedan marcados; no se inventa nada.
    - Se edita en la misma tabla, el organizador aprueba y se guarda en la red y en el evento.
    - **Export en el formato exacto de su portal** (JSON y CSV), también desde cualquier evento.
    - El ejemplo público (botón "Use sample paste") muestra una extracción guardada, sin passcode: 9 filas, de las cuales 4 son nuevas, 4 ya estaban en la red y 1 es un posible duplicado.
  - **WinterHack 2026** (18 de diciembre, AWS Builders Loft), su evento real, es ahora el primer brief. Tiene recomendaciones, texto para Luma, portada y 18 borradores de outreach de ejemplo.
  - Los jueces tienen los badges **Investor** y **Big name**, que no cambian el puntaje. **LinkedIn** se sumó como canal de outreach.
  - **Segundo agente en Covey: "Crewbase Growth"**, para el crecimiento de Saurabh (lo que contó en la llamada: sponsors solo por contactos, quiere jueces VC, poco alcance en LinkedIn y todavía sin X).
    - Busca sponsors nuevos que encajen con cada evento, propone jueces VC del Bay Area, arma los posts de LinkedIn y X (incluido el lanzamiento de su cuenta de X), encuentra dónde reclutar builders y redacta el pitch de sponsorship.
    - Cada sugerencia lleva un link a la fuente y se cruza con los datos de Crewbase para no pedirle dos veces a la misma empresa. Nunca publica ni envía nada.
    - Preguntas sugeridas: "Find new sponsors for WinterHack", "Suggest VC judges for WinterHack" y "Draft our LinkedIn and X launch posts".
    - **Probado:** para WinterHack devolvió 8 sponsors nuevos (LiveKit, Convex, Vapi, Airbyte, Temporal, Modal, fal y Runway), con su ronda o programa de créditos, el rol a contactar y la fuente, más 2 de respaldo (Twelve Labs y Supabase).
    - Ojo: según la llamada, Runway ya está confirmado para este hackathon, pero todavía no figura en los datos públicos.
  - **Comms** (`/comms` y una pestaña en cada evento): por evento y por grupo (jueces, sponsors, speakers o una selección propia), una secuencia de 4 emails por persona: invitación, confirmación con la logística, recordatorio del día anterior y agradecimiento con los ganadores y sus demos.
    - Cada email se escribe con la historia real de la persona en Crewbase. Lo que falta queda como [TBD].
    - Tabla con el estado de cada persona (borrador → aprobado → borrador en Gmail → enviado → respondió → confirmó), embudo del evento y botones "Approve all" y "Fill thank-you results".
    - Ejemplo público: 24 emails para WinterHack. El agradecimiento ya trae a los ganadores del leaderboard.
  - **Connections** (`/connections`): Gmail, WhatsApp y LinkedIn, cada uno sin conectar y con lo que habilita. Cada email tiene botones Email (mailto o borrador en Gmail), WhatsApp (`wa.me` con el texto ya escrito) y LinkedIn (abre el perfil y copia el mensaje). Las personas tienen un campo de teléfono, y Add people saca los teléfonos de los chats de WhatsApp. Nunca se envía nada automáticamente.
  - **Event day** (`/event-day`):
    - Formulario público de entregas, sin login.
    - Links privados para que cada juez evalúe desde el celular, con 4 criterios editables.
    - Leaderboard en vivo con el promedio por criterio y por track.
    - **Un reporte por sponsor** con los proyectos que usaron su herramienta, las demos, los repos, los puntajes y el LinkedIn de cada equipo.
    - Ejemplo: 8 proyectos ficticios de WinterHack, evaluados por los 3 jueces de ejemplo.
  - **Revenue** (con passcode): cash y créditos de API de cada sponsor, su estado (propuesto → acordado → facturado → pagado), los fees de los jueces, y los totales por evento y por mes. Empieza vacío, sin montos inventados.
  - **Luma:** "Push to Luma" crea o actualiza el evento con su API key de Luma Plus, y "Import attendees" trae a los inscriptos a la red. Funciona cuando él cargue su key en Connections.
  - **Follow-ups** (`/follow-ups`): la lista de pendientes de networking, calculada con los datos de la app.
    - Hoy tiene 49 agradecimientos pendientes, 11 relaciones que se están enfriando (3 o más eventos y nada en 60 días), 13 presentaciones sugeridas entre sponsors y equipos, y 0 mensajes sin respuesta.
    - Cada pendiente trae un borrador con IA y los botones Email, WhatsApp y LinkedIn. Se puede posponer o marcar como hecho, y queda registrado. Los totales aparecen en Home.
  - **Tour guiado** ("Take the 2-minute tour" en Home): 7 pasos que recorren Add people, Data Health, las recomendaciones de WinterHack, el texto para Luma y la portada, Comms, el día del evento con un reporte de sponsor, e Impact. No pide passcode. Se probaron los 7 pasos.
  - **API pública de solo lectura** (Connections → API), sin key: `https://br-brave-loon-b10ab69e.supabase.aidap-global.ap-southeast-1.bytepluses.com/functions/v1/public-api`.
    - Rutas: `/network/summary`, `/people`, `/organizations`, `/events`, `/events/{id}/recommendations`, `/comms-status`, `/leaderboard` y `/followups`.
    - Nunca expone emails, teléfonos, cuerpos de mensajes, montos ni keys. Solo GET y hasta 120 pedidos por minuto.
  - **Los dos agentes de Covey ya leen esta API en vivo.** Probado: Copilot respondió con el health score, el top 4 de jueces de WinterHack con los mismos puntajes que la app, y los 3 pendientes más importantes de la semana.
  - Ajustes: se sacaron las etiquetas en mayúsculas sobre los títulos, Home ya no queda resaltado en otras páginas, y el paso 1 del tour carga solo el ejemplo.
  - **Pasada de calidad:** el menú quedó agrupado en Home, Network, Plan, Impact y More. Se revisó cada página en celular (375 px). La corté antes de que terminara la verificación final, para no pasarnos de tiempo ni de créditos; la vista previa funciona sin errores.
  - El resumen semanal de Covey ahora lee la API en vivo.
- **Pendiente de Miranda:** crear el passcode de organizador ("Unlock editing" en la app) antes de compartir el link, porque el primero que edita lo define.
- Verificado en la vista previa: Comms, Event day, el reporte de sponsor y Connections funcionan sin passcode y sin errores en la consola. Revenue y Luma no se pudieron probar, porque no hay passcode ni API key.
- **Documentos para el envío:** `ONE_PAGER.md` (borrador en inglés) y `VIDEO_SCRIPT.md` (guion de 3 minutos con la narración y los clics). Los dos esperan los números de Saurabh.
- **Resumen semanal en Covey (Scheduled), creado con aprobación de Miranda:** la tarea "Crewbase weekly network and data health digest" corre todos los lunes a las 8 AM, y la primera es el 23 de noviembre de 2026. Revisa los 5 arreglos de datos que más rinden, los sponsors y jueces que llevan más de 60 días sin venir, y 3 personas para invitar al próximo evento. No envía mensajes ni cambia datos.
- **Créditos:** Covey y Enter usan el mismo saldo: los dos bajaron igual todo el día, y Covey siempre muestra 200 más. Desglose: 132 en los módulos A y B, 111 en el D, 56 en el E, 101 en el F (incluida la imagen de Framia), 8 en la prueba del agente, 100 en Home y Outreach, 59 en Impact 137 en Add people y WinterHack 28 en el agente Growth y la republicación, 311 en Comms, Connections, Event day, Revenue y Luma, 217 en Follow-ups, el tour y la API, y 130 en la pasada de calidad. Total: **1,390 de los 1,500**. No se construye más. La IA dentro de la app usa la key "Crewbase-Network-and-Data-Health" de AI All.
- **Siguiente:** grabar el video siguiendo `VIDEO_SCRIPT.md`, que ya abre con Add people y usa WinterHack. Después, pasar `ONE_PAGER.md` al formato del envío y mandar el formulario con los links públicos.

## 1. La tesis en una frase
El activo de Crewbase es su **red de relaciones**: quién participó en qué evento, con qué rol y con qué resultado. Hoy está dispersa y en la cabeza de Saurabh. **Crewbase Copilot la convierte en conocimiento reutilizable y la usa para planear cada evento nuevo en minutos.** Recomienda partners con razones y redacta el texto para Luma. El organizador siempre revisa y aprueba.

## 2. Qué construimos (la mejor solución dentro del tiempo que hay)

Hay que demostrar **un solo flujo completo con datos reales**: los 21 eventos, 116 organizaciones, 114 personas y 517 participaciones de su web.

| # | Módulo | Qué hace en el demo | Área del brief |
|---|---|---|---|
| A | **Red de relaciones** | Directorio de personas y organizaciones con su historial ("Ayush Ojha: 17 eventos como host, juez y speaker"). Ficha de cada evento. | 1 · Gestión unificada |
| B | **Salud de los datos** | Cola de arreglos: fusionar a Ali Amjad, corregir Synk → Snyk, completar las 76 descripciones que faltan con IA, aclarar los 16 contactos que no coinciden. Cada arreglo se aprueba con un clic. | 1 · Calidad de los registros |
| C | **Nuevo evento → plan** | El organizador escribe el brief ("hackathon de agentes, 12 de diciembre, Frontier Tower, 80 builders"). El sistema arma un plan con tema, audiencia, tracks y lo que hace falta. | 2 |
| D | **Recomendaciones explicables** | Una lista de sponsors, jueces y speakers ordenada por puntaje, con la **razón** de cada uno. Se puede aceptar, quitar o agregar. | 2 · Decisiones de partners |
| E | **Estudio de texto para Luma** | Genera el título, el gancho, la descripción, la agenda y las secciones de sponsors y jueces a partir de los ya confirmados. Incluye una checklist de calidad, variantes, edición y un botón para copiar. | 3 · Texto de Luma |
| F | **Portada** | Framia genera la portada con los logos de los sponsors confirmados. | 3 |
| G | **Copilot en el chat** | Un agente en Covey: "planeemos el próximo hackathon" lleva por C, D y E. Además arma borradores de outreach en Gmail sin enviarlos. | Interfaz |

**Extras si sobra tiempo:**
- Un portal para que el sponsor suba su logo y apruebe su texto.
- Un resumen semanal de la salud de los datos con Covey Scheduled.
- Enriquecer perfiles con Firecrawl.

**Fuera de alcance:** publicar automáticamente en Luma, enviar emails solo, juegos (Combos) y pagos.

### Lógica de las recomendaciones (explicable, no una caja negra)
`puntaje = encaje con el tema (etiquetas por LLM) + experiencia en ese rol + participación reciente + frecuencia − cansancio (si se le pidió hace menos de 3 semanas) + bonus de conector (si trae a otros sponsors)`

Después, un LLM escribe la razón en una frase usando esos mismos datos. El organizador edita y **sus ediciones quedan registradas** (es el ciclo de aprendizaje y la métrica de aceptación).

## 3. Dónde vive cada pieza en Converge

```
Saurabh ──chat──▶ COVEY · agente "Crewbase Copilot"
                     ├─ plugin ENTER  → construye y opera la app
                     ├─ plugin FRAMIA → portada y piezas para redes
                     ├─ plugin Gmail / WhatsApp / Discord → borradores de outreach
                     └─ Firecrawl / Browser Use (extras) → enriquecer perfiles, cargar en Luma
                     
ENTER PRO · app "Crewbase Copilot" (link público para el envío)
   Base de datos: events · organizations · people · participations   ← data/seed/*.csv
   Pantallas: Red · Salud de datos · Nuevo evento → Recomendaciones → Texto para Luma
   LLM: Claude (seleccionable en Enter)
```

**Plan B si Enter no puede importar los datos o no publica con link público:** usar Supabase como base de datos a través del plugin de Covey, mantener la interfaz en Enter, y si hace falta usar Google Sheets como base. Antes de pasar a código fuera de Converge, preguntar a los mentores.

## 4. Cronograma

### Martes 17 (hoy)
| Hora (PT) | Tarea | Responsable |
|---|---|---|
| Ahora → 7 PM | **Prueba técnica de Converge:** iniciar sesión, invitar al equipo, revisar los créditos. En Enter, crear la app e **importar `data/seed/*.csv`**. Verificar que publica con link público y que se puede elegir Claude. Revisar si "Create plugin" de Covey acepta MCP. | Constructor |
| 7 → 9:30 PM | Módulos A y B (la red y la salud de los datos) con los datos reales | Constructor |
| 7 → 9:30 PM | Agente de Covey: instrucciones, conexión con el plugin de Enter y una prueba de Framia | Agente y creativo |
| 7 → 9:30 PM | Esqueleto de la página de resumen y guion del video | Pitch |
| **10 PM** | **Llamada con Saurabh** (`LLAMADA_SAURABH.md`) | Todo el equipo |
| 10:30 PM | Volcar la línea base y la prioridad en este plan. Ajustar el alcance si su prioridad número uno es otra. | Pitch |

### Miércoles 18
| Hora (PT) | Tarea |
|---|---|
| 9 AM → 1 PM | Módulos C y D (el plan del evento y las recomendaciones) |
| 1 → 4 PM | Módulo E (el texto para Luma) y F (la portada con Framia). El Copilot G conectado de punta a punta. |
| 4 → 5 PM | **Congelar funciones.** Prueba completa con el escenario del demo. Corregir errores. |
| 5 → 7 PM | Grabar el **video de 3 minutos como máximo** y escribir el **resumen de una página** |
| 7 → 9 PM | Revisar los links ("Anyone with the link") y **enviar** |
| 9 → 11:59 PM | Margen para cambios. El formulario se puede editar hasta el deadline. |

## 5. Lo que se envía
1. **El prototipo:** el link público de la app en Enter, y el link del agente de Covey si se puede compartir.
2. **El video (3 minutos como máximo):**
   - 0:00–0:20 · El problema, con sus números: "X horas por evento, y todo vive en la cabeza de una persona".
   - 0:20–0:50 · La salud de los datos: sus duplicados y vacíos reales, arreglados con un clic.
   - 0:50–2:10 · "Planeemos el hackathon de diciembre": brief, recomendaciones con razones, el organizador edita, texto para Luma y portada.
   - 2:10–2:40 · Impacto: antes y después, en horas, aceptación y conversión.
   - 2:40–3:00 · Escala a otras comunidades (AI Collective, BuildClub) y por qué es factible: corre sobre Converge con sus datos de hoy.
3. **El resumen de una página:** el problema, el valor esperado, la factibilidad, los supuestos y cómo se aplica en otros contextos (ver `SOLUCION.md`).

## 6. Cómo cubrimos cada criterio de evaluación
| Criterio | Peso | Cómo lo ganamos |
|---|---|---|
| Impacto de negocio | 40% | La línea base que nos dé Saurabh frente al resultado medido en el demo. Las recomendaciones apuntan a sus ingresos (los sponsors). |
| Ejecución | 30% | Funciona con **sus datos reales** y de punta a punta, no con datos inventados. |
| Factibilidad | 20% | Vive en Converge. Sus datos ya están estructurados. Hay revisión humana en todo. El costo es de créditos, no de un desarrollador. |
| Presentación | 10% | Un caso concreto ("el hackathon de diciembre en 10 minutos") y una cita de Saurabh. |

## 7. Riesgos
| Riesgo | Cómo lo mitigamos |
|---|---|
| Enter no importa CSV o no publica con link público | Lo probamos primero, hoy. Plan B: Supabase o Sheets a través de Covey. |
| Nos quedamos sin créditos (tenemos 5,000) | Medir cuánto gasta la prueba técnica. Usar Framia solo para la versión final. |
| Saurabh prioriza otra cosa | El alcance es modular: se reordenan C, D y E sin rehacer A. |
| Las recomendaciones no convencen | Mostrar el puntaje y la razón, y validar en la llamada con un caso real ("¿invitarías a estos 5?"). |
