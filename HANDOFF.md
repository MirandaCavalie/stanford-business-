# Handoff para Miranda (miércoles 18 de noviembre, 8:35 PM PT)

Deadline del envío: **hoy a las 11:59 PM PT**, sin extensiones. Este documento tiene todo lo pendiente, en orden. Si se lo pasas a tu agente, que siga la sección "Pendiente, en orden" de arriba abajo.

## Estado en una línea
La app funciona en el link de preview, el bug de guardado de Data Health ya está arreglado y verificado, y los documentos están actualizados. Impact ya tiene actividad real y el one-pager ya está en PDF de una página. Falta: el video, subir el PDF con link público y el formulario.

## Links
- **Prototipo (usar este en el envío):** https://da946762214b46049c66aa2e3a5f9580.live-preview.enter.pro. Abre sin login, también con rutas directas como `/add-people`.
- **Producción sigue caída:** `https://da946762214b46049c66aa2e3a5f9580.prod.enter.pro` corta la conexión (comprobado a las 7:30 PM PT). No usarlo.
- **Proyecto en Enter:** `enter.converge.ai/project/da946762214b46049c66aa2e3a5f9580`
- **Formulario de envío:** https://docs.google.com/forms/d/e/1FAIpQLSfI1_LcWKcYTHSCMG5zE6mTXwDrnn3iLH_g40fhvxoLOPhFLw/viewform
- **Passcode de organizador:** el que definiste hoy. Rotarlo después del envío ("Change passcode" en Data Health).

## Pendiente, en orden

### 1. Impact con actividad real: hecho
Ya no hace falta hacer nada aquí. Quedó así (ver "Cambios en los datos de la app"):
- Recomendaciones: 80% de aceptación sobre 5 decisiones.
- Texto de Luma: 60% del borrador de IA conservado, 2 versiones guardadas.
- Data Health: 2 problemas resueltos de 213.
- El embudo de outreach sigue en 0 a propósito: no se envió ningún mensaje y la página dice "No invented numbers". No marcar nada como enviado si no salió.
- **No tocar** en Data Health el arreglo Synk → Snyk ni el duplicado Sartorial / Satorial: se aprueban en cámara (bloque 2 del guion).
- La línea base ("Edit baseline") se queda vacía salvo que Saurabh dé las horas.

### 2. Cronómetro (opcional, 10 minutos; lo hace Alejandro)
Saurabh no dio horas, pero sí el proceso: unos 15 jueces, cada uno con nombre, email, usuario, LinkedIn e imagen, uno por uno.
- Cronometrar la carga a mano de 15 registros con esos campos desde una lista desordenada, y después el mismo lote con Add people.
- Poner los dos tiempos en `VIDEO_SCRIPT.md`, donde dice `STOPWATCH_MANUAL` y `STOPWATCH_PASTE`, y en la primera fila de la tabla de `ONE_PAGER.md`. Presentarlo como una prueba nuestra, no como un dato de Saurabh.
- **Si no se hace, borrar del guion las dos frases que tienen esas marcas** ("We timed that: …" y "Same list: …"). No pueden salir en el video tal cual.

### 3. Grabar el video (3:00 como máximo)
- Seguir `VIDEO_SCRIPT.md`: cinco bloques con WinterHack como hilo.
- Desbloquear la edición antes de grabar, para que los clics de Accept funcionen.
- El bloque 5 incluye 5 segundos del agente Crewbase Copilot en Covey. **Solo se puede grabar desde la cuenta de Miranda:** los agentes y la tarea programada no aparecen en la cuenta de Alejandro, aunque esté en el workspace.
- Subir el video con permiso "Anyone with the link".

### 4. Subir el one-pager
- `ONE_PAGER.pdf` está en la raíz del repo: una página, generado desde `ONE_PAGER.md`.
- Subirlo a Google Drive y compartirlo con "Anyone with the link". No lo pudimos subir nosotros: el conector de Drive de Alejandro no tiene permiso de escritura.
- Confirmar cómo va el nombre de Alejandro (quedó como "Alejandro Gonzalez"). Si cambia, editar `ONE_PAGER.md` y regenerar el PDF.

### 5. Enviar el formulario
- Un envío por equipo. Se puede editar hasta el deadline, así que conviene mandarlo en cuanto haya video, aunque después se ajuste.
- Links: el video, el prototipo (el de preview) y el one-pager. Abrir los tres en una ventana de incógnito antes de enviar.
- Cada integrante tiene que haber firmado el participant agreement: https://consent.wefluens.com/

### 6. Si sobra tiempo
- **Preguntarle a Saurabh:**
  - Si "Finch" es Finchip AI. Ya está aceptado como sponsor en la shortlist de WinterHack; si no es él, cambiarlo antes de grabar.
  - Cuál es el sponsor principal de USD 1,100 (la transcripción dice "Braven(?)").
- **Discord:** reportar la caída de `*.prod.enter.pro` en `#report-a-bug` (nadie lo ha hecho) y etiquetar a Lani en `#team-19`, que ofreció revisar antes de enviar.

## Hecho esta tarde (Alejandro y Claude)

### Bug de Data Health: arreglado y verificado
- **Síntoma:** con el passcode correcto, todo guardado en Data Health devolvía 401 ("Unlock organizer editing first") y la página se volvía a bloquear. Plan sí guardaba.
- **Causa (reporte de Enter):** los guardados de Data Health llamaban a `invokeBackend` directo, que no adjunta el token de organizador. Plan usaba `callOrganizer`, que sí lo adjunta. "Change passcode" tenía la misma falla.
- **Arreglo:** todos los guardados protegidos pasan por `callOrganizer`: aprobar typo, merge de persona, merge de organización, descartar, sugerir campo, guardar campo, responder un mismatch y cambiar passcode. Costó unos 30 créditos; el saldo quedó en 3,677.
- **Verificado por nosotros en el link de preview:** el arreglo NVDIA → NVIDIA y el merge de Ali Amjad respondieron 200 y la cola bajó.
- **No verificado por nosotros:** guardar en Add people, la línea base de Impact y Revenue. Enter los confirmó leyendo el código, no ejecutándolos.

### Cambios en los datos de la app
- **Data Health:** typo NVDIA → NVIDIA aprobado y duplicado de Ali Amjad fusionado (se conservó el registro con 2 eventos). Quedó en 211 problemas abiertos y 2 resueltos; el health score sigue en 18, porque dos arreglos sobre 213 no alcanzan a moverlo.
- **WinterHack, shortlist:** aceptados Colin Lowenberg, Merve Isler y Vince Kohli como jueces y Finchip AI como sponsor; descartada Chelsey Huang como jueza (es cofundadora de Finchip AI, el sponsor aceptado).
- **WinterHack, texto de Luma:** se generó una versión nueva con IA a partir de la shortlist, se le puso el horario real (9:30 AM - 8:30 PM) y se guardó. La checklist quedó en 8 de 9.
- **Event day de WinterHack:** como el único sponsor aceptado es Finchip AI, el único link de sponsor que aparece es el de Finchip AI. El guion ya lo usa en lugar del de Nebius.

### Cambios en el repo
- `VIDEO_SCRIPT.md`: de nueve segmentos a cinco bloques. Connections, Follow-ups, Revenue, la API y el tour quedaron fuera del video.
- `ONE_PAGER.md`:
  - Link de preview en lugar del de producción.
  - La sección de solución pasó de ocho bloques a seis.
  - Tabla de valor sin corchetes.
  - Créditos en ~1,400.
  - El riesgo de Luma dice que el push está construido pero sin probar, porque falta su API key.
- **Reclamo del reporte de sponsor corregido** en los dos archivos (ver abajo).
- **Frase de los conectores más cauta:** los 16 casos son 6 personas, 4 de los casos son el propio Saurabh, y ninguno está confirmado en Data Health.

## De las notas de la llamada (Fellow)
- **El reporte de sponsor estaba mal vendido.** Saurabh dijo que a los sponsors les entrega una demo en vivo o la URL del producto, "not a separate report". Ahora los documentos dicen que cada sponsor recibe un link con las demos en vivo hechas con su herramienta, que es lo que él ya les debe y hoy junta a mano.
- **Runway ya es sponsor** de WinterHack, pero el agente Growth lo sugiere como nuevo. No mostrar esa respuesta en el video.
- **Él ya tiene casi lista su automatización de invitaciones a jueces.** Presentar Comms como el contenido personalizado y el seguimiento, no como el envío.
- **El bloqueo de Luma y el calentamiento de correo** los sugirió Miranda en la llamada, no él. No presentarlos como un dolor que él reportó.
- **No dio ningún número de horas.** No inventar la línea base.

### Ranking de WinterHack y tres detalles: arreglados
Segundo pedido a Enter, a las 8:22 PM PT; terminó a las 8:40 PM PT. Con el anterior, el saldo quedó en 3,598 créditos.
- **Encaje de tema plano.** Casi todos tenían 5/40 en WinterHack.
  - **Causa (reporte de Enter):** las etiquetas de tema se guardaban en caché de forma global, no por brief, y el prompt que etiqueta ignoraba el tema del brief. Editar el tema tampoco limpiaba la caché.
  - **Arreglo:** etiquetas por brief, WinterHack recalculado contra su tema, y la caché se limpia cuando cambia el tema. La fórmula y las escalas no cambiaron.
  - **Verificado por nosotros:** en el top 8 el tema va ahora de 5 a 25 sobre 40.
    - Jueces: Colin Lowenberg 75; Amitabh Das, Merve Isler y Vince Kohli 60; Abhi Vasanth 59.
    - Sponsors: InsForge 69, RocketRide 67, Nebius 65, Apify 61, Finchip AI y Kylon 60.
- **Bonus de conector graduado:** 4, 7 o 10 puntos por 1, 2 o 3 o más casos. Solo cuentan casos con rol de sponsor y no cuenta Saurabh. Merve Isler pasó de 10 a 0, porque su caso era un community partner.
- **Texto de Luma:** una persona ya no sale como jueza y speaker a la vez. No lo verificamos nosotros.
- **Invitaciones a sponsors:** ya no piden "hosting the venue" si el brief tiene sede. No lo verificamos nosotros.
- **Ojo al grabar:** las tarjetas de la shortlist muestran el puntaje del momento en que se aceptó (Colin 65, Finchip AI 55), no el nuevo. La lista de recomendaciones de abajo sí muestra los puntajes nuevos.
- **Finchip AI ya no sale primero entre los sponsors** (quedó quinto, con 60). La frase opcional del guion "Its top sponsor pick is one he had already signed" ya no aplica; la quitamos.

## Visto en la app y no tocado
Nada de esto bloquea el envío. No construir más salvo que algo se rompa.
- **API pública:** dice 194 problemas abiertos y la app 211.
- **Pantallas que se ven a medio conectar en cámara:** Connections (cuatro integraciones sin conectar), Comms (0 de 3 con correo, 57 datos en TBD) y Follow-ups (49 tarjetas casi iguales). Por eso no están en el guion.
- **Ningún juez del top 8 tiene el badge Investor;** el guion no lo menciona.
- **La pasada final de calidad se canceló a medias.** Recorrimos 12 rutas en escritorio sin encontrar nada roto; después revisamos el leaderboard, el link de sponsor de Finchip AI y seis páginas a 375 px, sin scroll horizontal.

## De Discord
- Cada empresa revisa los envíos de su reto, así que Saurabh va a leer esto.
- Tip de Lani para el video: contexto del negocio, un flujo completo de principio a fin, el impacto y cómo aplica a otros negocios. Un demo claro vale más que muchas funciones sueltas.
- Los agentes de Covey no se pueden embeber ni llamar por API; Converge recomienda construir el agente dentro de Enter.
