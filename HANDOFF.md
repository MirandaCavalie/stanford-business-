# Handoff para Miranda (miércoles 18 de noviembre, noche)

Deadline: **11:59 PM PT de hoy**. Lo que sigue es lo que hicimos Alejandro y Claude esta tarde, lo que encontramos y lo que queda de tu lado.

## Links
- **Prototipo que funciona:** https://da946762214b46049c66aa2e3a5f9580.live-preview.enter.pro (abre sin login, también con rutas directas).
- **Producción sigue caída:** `*.prod.enter.pro` corta la conexión. Usar el link de preview en el formulario.
- **Passcode de organizador:** el que definiste hoy. Hay que rotarlo después del envío.

## Lo que queda de tu lado
1. **Grabar el video** con `VIDEO_SCRIPT.md`, que ahora tiene cinco bloques en vez de nueve. El bloque de Covey dura 5 segundos y solo se puede grabar desde tu cuenta: los agentes no aparecen en la cuenta de Alejandro aunque esté en el workspace.
2. **Enviar el formulario** con el link de preview. Se puede editar hasta el deadline, así que conviene mandarlo temprano.
3. **Preguntarle a Saurabh dos cosas** (ver "De las notas de la llamada").
4. **Confirmar cómo va el nombre de Alejandro** en el one-pager (quedó como "Alejandro Gonzalez").

## Bug encontrado: Data Health no guardaba
- Con el passcode correcto, todo guardado en Data Health devolvía 401 ("Unlock organizer editing first") y la página se volvía a bloquear. Lo reprodujimos con el arreglo NVDIA → NVIDIA y con el merge de Ali Amjad.
- En la misma sesión, aceptar un juez en Plan sí guardaba, así que el passcode y el token estaban bien.
- Le mandamos el arreglo a Enter a las ~8:30 PM PT, con la instrucción de no dejar cambios de prueba en los datos. **Estado: ver la última respuesta en el chat de Enter.**
- Hasta confirmar el arreglo, no grabar el paso "Accept fix on Synk → Snyk" del bloque 2.

## Cambios en los datos de la app
- Colin Lowenberg quedó **aceptado como juez en WinterHack** (fue la prueba de que Plan sí guarda). Aparece en la shortlist y la tasa de aceptación marca 100% con 1 decisión.
- No se cambió nada más. Data Health sigue en 213 problemas abiertos y 0 resueltos.

## Impact sigue en ceros
Es la pantalla del criterio de impacto de negocio (40%). Antes de grabar el bloque 5 hace falta actividad real:
- Aprobar en Data Health el merge de Ali Amjad y los dos typos (cuando el bug esté arreglado).
- Aceptar dos o tres jueces y un sponsor en WinterHack.
- No marcamos ningún outreach como enviado, porque no se envió nada. Si quieres que el embudo muestre algo, que sea con mensajes que sí salgan.
- La línea base ("Edit baseline") sigue vacía: Saurabh no dio horas.

## El cronómetro
Saurabh no dio horas, pero sí el proceso: unos 15 jueces, cada uno con nombre, email, usuario, LinkedIn e imagen, uno por uno.
- Alejandro cronometra cargar a mano 15 registros con esos campos desde una lista desordenada, y después el mismo lote con Add people.
- El resultado va en `VIDEO_SCRIPT.md` (reemplaza STOPWATCH_MANUAL y STOPWATCH_PASTE) y en la tabla del one-pager, presentado como una prueba nuestra.
- Si no da tiempo, se cortan esas dos frases del guion.

## De las notas de la llamada
- **El reporte de sponsor estaba mal vendido.** Saurabh dijo que a los sponsors les entrega una demo en vivo o la URL del producto, "not a separate report". El one-pager y el guion ya no dicen que el reporte es "lo que los sponsors pagan"; dicen que es un link con las demos en vivo, que es lo que él ya les debe.
- **Para preguntarle:**
  - Si "Finch" es Finchip AI. La app lo pone primero en el ranking de sponsors de WinterHack; si ya firmó, es una validación que vale una frase en el video.
  - Cuál es el sponsor principal de USD 1,100 (la transcripción dice "Braven(?)").
- **Runway ya es sponsor** de WinterHack, pero el agente Growth lo sugiere como nuevo.
- **Él ya tiene casi lista su automatización de invitaciones a jueces.** Comms conviene presentarlo como el contenido personalizado y el seguimiento, no como el envío.
- **El bloqueo de Luma y el calentamiento de correo** los sugeriste tú en la llamada, no él. Mejor no presentarlos como un dolor que él reportó.

## Cambios en el repo
- `ONE_PAGER.md`: link de preview, la sección de solución pasó de 8 bloques a 6, el reclamo del reporte de sponsor corregido, sin corchetes en la tabla, créditos en ~1,400. Tiene unas 900 palabras; al pasarlo al formato de envío hay que comprobar que quepa en una página.
- `VIDEO_SCRIPT.md`: cinco bloques con WinterHack como hilo.
- La frase de los conectores quedó más cauta: los 16 casos son 6 personas, 4 de los casos son el propio Saurabh, y ninguno está confirmado en Data Health.

## Cosas que vimos en la app y no tocamos
- **Ranking de WinterHack plano:** casi todos tienen 5/40 en encaje de tema, así que el orden sale de frecuencia y recencia. Ningún juez del top 8 tiene el badge Investor.
- **Bonus de conector todo o nada:** Merve Isler recibe los mismos 10 puntos por 1 caso que Colin por 8, y su caso es un community partner, no un sponsor.
- **Luma copy:** Colin Lowenberg y Merve Isler salen como jueces y también como speakers.
- **Outreach a sponsors:** pide "hosting the venue" aunque la sede ya es AWS Builders Loft.
- **API pública:** dice 194 problemas abiertos y la app 213.
- **Pantallas que se ven a medio conectar en cámara:** Connections (cuatro integraciones sin conectar), Comms (0 de 3 con correo, 57 datos en TBD) y Follow-ups (49 tarjetas casi iguales). Por eso no están en el guion.

## De Discord
- Cada empresa revisa los envíos de su reto, así que Saurabh va a leer esto.
- Lani (Converge) ofrece revisar antes de enviar si la etiquetan en `#team-19`.
- Nadie ha reportado la caída de producción en `#report-a-bug`.
- Tip de Lani: menos texto explicativo en la interfaz y un flujo completo en vez de muchas funciones.
