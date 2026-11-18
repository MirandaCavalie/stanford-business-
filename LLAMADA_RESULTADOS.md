# Resultados de la llamada con Saurabh (martes 17 de noviembre, 10 PM PT)

Fuente: notas de Fellow de la llamada y la captura de pantalla de su portal de administración.

## Lo que más le duele (prioridad número uno)
- **Cargar a la gente nueva en su portal.** Para cada evento carga a mano a cada juez, sponsor y speaker, con nombre, email, usuario, LinkedIn e imagen. Un evento típico tiene unos **15 jueces**, y cada uno es un registro que se escribe por separado.
- **Los contactos están dispersos** en planillas de Excel, en WhatsApp y en LinkedIn. Reutilizar datos que ya están cargados es fácil; **lo que traba es la gente nueva**, que aparece en casi todos los eventos.
- Confirmó la dirección que le propusimos: un **"segundo cerebro"** que sea la única fuente de verdad para contactos y eventos.
- **Lo que no le duele:** los logos y el diseño (los hace rápido en Figma). La portada con Framia baja de prioridad.

## Su portal de administración (captura)
- Es una app propia (`localhost:5174/admin`). Tiene las secciones Events, Sponsors & Partners, People y Settings.
- Cada evento tiene una pestaña de datos básicos y una pestaña por tipo de participante. Los datos básicos son: nombre, tipo, fechas, tema, horarios, sede, descripción, portada y links de Luma. Las pestañas son: Tracks, Sponsors, Partners, Prizes, Schedule, Speakers, Judges, Hosts, Volunteers, Associated, People, Links y Photos.
- Usa el mismo modelo de datos que su web pública, que es de donde sacamos la semilla:
  - Personas: `username`, `linkedin`, `title`, `companyName`.
  - Jueces: además, `role`.
  - Sponsors: `companyName`, `companyWebsite`, `companyLogo`, `companyDescription` y `representatives`.
  - **Esto significa que podemos generar los datos en su formato exacto.**
- **Evento que está armando:** "WinterHack 2026: Christmas and New Year Edition". Es un hackathon el **18 de diciembre de 2026**, de 9:30 AM a 8:30 PM, en el **AWS Builders Loft** (525 Market St). Por ahora tiene 0 sponsors, 0 jueces, 0 speakers y el tema vacío.

## Sponsors, jueces y crecimiento
- **Sponsors:**
  - Los consigue por relaciones personales.
  - Pagan en efectivo o en créditos de API, según su presupuesto.
  - Lo que se llevan al final es una demo en vivo o la URL de un producto armado por los participantes.
  - En el próximo hackathon hay un sponsor principal que pone USD 1,100 y otros que aportan herramientas de generación de video.
- **El tema del evento** sale de las herramientas de los sponsors y de una lluvia de ideas con Claude o GPT.
- **Jueces:**
  - Busca **jueces de fondos de inversión (VCs)**, porque dan prestigio y atraen asistentes.
  - **Les cobra a algunos jueces entre USD 100 y 500 de "support fee"**, que es una fuente de ingresos.
- **Trabaja solo** en sede, jueces y sponsors. Solo suma ayuda para el marketing.
- **Crewbase tiene más o menos un mes.** Su LinkedIn llega poco (más de 3,000 contactos) y todavía no tiene cuenta en X, aunque quiere abrirla.
- **Luma:**
  - **Tiene Luma Plus, que trae API.**
  - Si manda muchas invitaciones de golpe, Luma puede bloquear la cuenta. Hay que "calentar" un email propio (por ejemplo, hello@dominio) antes.
  - Está por automatizar él mismo el envío masivo de invitaciones a jueces.

## Lo que falta (no salió en las notas)
- Cuántas horas le lleva cada evento en total y cuántas el texto de Luma.
- Cuántos sponsors contacta por cada uno que confirma.
- Si los contactos que figuran con otra empresa son errores o son quien trajo al sponsor.

En el video y en el resumen lo decimos con sus propias palabras ("15 judges entered one by one") y no inventamos horas.

## Qué cambia en la solución
1. **Nueva prioridad, el módulo H "Smart intake":**
   - Pegar texto desordenado: una exportación de WhatsApp, filas de Excel, URLs de LinkedIn o una lista de nombres.
   - La IA lo convierte en registros con nombre, email, LinkedIn, cargo, empresa y rol.
   - Los compara con la red para no duplicar y marca los campos que faltan.
   - El organizador aprueba, y se exporta **en el formato de su portal**.
   - Es exactamente su paso más lento.
2. **El ejemplo del demo pasa a ser WinterHack 2026**, su evento real, en lugar del "AI Agents Hackathon".
3. **Recomendaciones de jueces:**
   - Marcar a los inversores (VCs) y a los nombres conocidos, porque es lo que él busca.
   - Registrar si el juez paga el support fee.
4. **Outreach:** sumar LinkedIn como canal, y más adelante X a través de Covey.
5. **Luma:** como tiene Luma Plus, lo que sigue es empujar el texto aprobado por la API de Luma. Por ahora queda como copiar y pegar, y lo mencionamos en la factibilidad.
6. **La portada (Framia)** queda, pero no es protagonista del video.
