# We mean BUSINESS! · Stanford 30×30 Buildathon (Converge.AI)

Resumen del reto y de las reglas. Fuente: el brief del reto (PDF) y los mensajes de Discord del 17 de noviembre de 2026.

## Calendario (hora PT)

| Fecha | Qué pasa |
|---|---|
| Mar 17 nov · 10:00 | Kickoff online, se publican los retos |
| **Mié 18 nov · 23:59** | **Deadline de envío (fijo, sin extensiones)** |
| Jue 19 nov · 18:00 | Se anuncian los 8 finalistas |
| Vie 20 nov · 15:00 | Demo Day en Stanford, $5,000 en premios |

## Reglas

1. **Hay que construirlo con productos de Converge.AI.** Si no, no se acepta.
2. Resolver el problema real de la empresa asignada y hablar con su contacto pronto.
3. Un envío por equipo; se puede editar hasta el deadline.
4. Cada integrante firma el participant agreement: https://consent.wefluens.com/
5. Todos los integrantes deben estar en Discord y ver el canal #team-XX.

## Evaluación (cada criterio de 1 a 10)

- **Impacto de negocio: 40%**
- Ejecución: 30%
- Factibilidad: 20%
- Presentación: 10%

## Qué se envía

- Video demo de 3 minutos como máximo
- Link al prototipo funcionando
- Resumen de una página: problema de negocio, valor esperado, factibilidad de implementación, supuestos clave y cómo podría aplicarse en otros contextos
- Todos los links con permiso "Anyone with the link"
- Formulario: https://docs.google.com/forms/d/e/1FAIpQLSfI1_LcWKcYTHSCMG5zE6mTXwDrnn3iLH_g40fhvxoLOPhFLw/viewform

## Configuración de Converge.AI

- El contacto principal entra a https://covey.converge.ai/, hace clic en su workspace (abajo a la izquierda) y elige **Invite members**. Los compañeros aceptan con el mismo email con el que se registraron.
- En ese mismo menú se revisan los **Credits**. Deberían aparecer 5,000 créditos gratis; si no aparecen, avisar por Discord de inmediato.
- Los productos que aparecen en el brief son Covey (workspace de IA para equipos y agentes), Enter y Framia. Hay un cuarto logo que no se lee bien.

---

## La empresa: Crewbase

- **Industria:** gestión de eventos y comunidades
- **Web:** https://crewbasecollective.com
- **Contacto:** Saurabh Khire, dueño del negocio (saurabhskhire@gmail.com)
- Organizan hackathons, encuentros de founders, sesiones para buscar co-founder y otros eventos de comunidad en el Bay Area. Trabajan con sponsors, inversores, jueces, partners, hosts y participantes, y publican sus eventos en plataformas como **Luma**.

## El reto: Smarter Event Operations, de los registros de partners a la planificación de eventos guiada por IA

### Dolores actuales

1. **Carga manual repetida.** Para cada evento hay que escribir la descripción, subir la portada y los logos de partners, y volver a cargar perfiles y fotos de los participantes. Aunque algunos datos se reutilizan, el trabajo sigue siendo manual y la información termina inconsistente.
2. **La elección de partners depende de la memoria del organizador.** Decidir qué inversores o partners encajan con cada evento depende de lo que el organizador recuerda y de su red. El historial, los intereses y los temas no están organizados.
3. **Adaptar el texto para Luma es otra tarea repetitiva.** Cada vez hay que convertir los datos del evento en una página de registro clara y atractiva.

### Desafío central

Convertir la información de eventos y stakeholders en **conocimiento reutilizable de la organización**, usarla para **planificar alianzas** y **mejorar la comunicación de los eventos**, y que los organizadores **revisen y editen lo que proponga la IA** antes de usarlo.

### Áreas para explorar

1. **Gestión unificada de eventos y stakeholders.** Registros estructurados de inversores y partners: datos básicos, afiliaciones, historial de participación, logos y fotos. Menos carga repetida, sin que el organizador pierda el control sobre la calidad de los datos.
2. **Recomendaciones editables de inversores y partners.** Comparar el tema, la audiencia, el formato y las necesidades de partners de un evento nuevo con los perfiles y el historial de cada stakeholder. Recomendar con razones que se entiendan, y que el organizador pueda revisar, cambiar, quitar o agregar.
3. **Posicionamiento del evento y mejora del texto para Luma.** Sugerencias concretas para la página de registro: posicionamiento, relevancia para la audiencia, claridad y llamados a la acción. La edición queda en manos del organizador y no se publica nada automáticamente.

### Criterio de valor

Empezar con algo acotado, pero pensado de punta a punta: qué decisión mejora, qué pasa antes y después, cómo se mide el valor y si se puede llevar a otros equipos, ciudades, clientes o empresas.

### Impacto esperado y métricas sugeridas

| Impacto | Métricas |
|---|---|
| Preparar eventos más rápido y de forma consistente | Tiempo de preparación, pasos de carga repetidos, completitud de los registros, correcciones necesarias |
| Mejores decisiones sobre partners | Tasa de aceptación de recomendaciones, ediciones del organizador, respuesta al outreach, participaciones confirmadas |
| Mejor promoción y capacidad de crecer | Tiempo de revisión del texto, engagement en la página de registro, conversión a registro, eventos por organizador |

---

## Crewbase hoy (leído de crewbasecollective.com el 17 de noviembre de 2026)

- Comunidad de builders, founders y operadores del Bay Area. Organiza hackathons, pitch competitions, workshops, demos y mixers.
- La web muestra **21+ eventos, 78+ sponsors y partners, 114+ miembros**. Los eventos van de mayo a octubre de 2026, con un pico de unos 10 eventos en junio.
- Sedes que repiten: Homebrew Club (111 Maiden Ln), AWS Builders Loft (525 Market St), Frontier Tower (995 Market St), Sports Basement (Bryant St) y una en Santa Clara.
- La web ya tiene un modelo de datos: **Eventos** (tipo, fecha, sede), **Personas** (nombre, cargo, empresa y roles: HOST, SPONSOR, JUDGE, SPEAKER, PARTNER, VOLUNTEER) y la página de Sponsors & Partners, que aparece vacía.
- **Problemas de calidad de datos visibles:** registros duplicados (Ali Amjad aparece dos veces) y erratas en empresas y cargos ("Synk" en lugar de Snyk, "NVDIA", "Heat of GTM", "Ambdassedor", "Grwth"). Es evidencia directa del dolor número 1.
- Canales: Luma Calendar (https://luma.com/calendar/cal-3A00RBKfF0vkoAd), Discord, LinkedIn y events@crewbasecollective.com. Los enlaces de WhatsApp y X dicen "coming soon".
- Recibe pedidos por formularios: sponsorship, judging/speaking, partnership, member/host y volunteer.
