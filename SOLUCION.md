# Crewbase: diagnóstico y solución ideal

Este documento tiene tres partes: el diagnóstico de cómo funciona Crewbase hoy, la decisión de construir o comprar, y la mejor solución posible sin límite de tiempo. Cómo armarla con Converge.AI va en la sección 4.

Lo marcado con **[validar]** es un supuesto que hay que confirmar con Saurabh.

---

## 1. Diagnóstico del flujo actual

| # | Pregunta | Lo que sabemos o suponemos |
|---|---|---|
| 1 | **Volumen** | Más de 21 eventos entre mayo y octubre de 2026, unos 4 por mes, con un pico de 10 en junio. Hay 114 personas y más de 78 organizaciones en la base. Cada evento involucra entre 5 y 15 stakeholders (sponsors, jueces, speakers, hosts) **[validar]**. |
| 2 | **Canales de entrada** | Los formularios de Get Involved (sponsorship, judging, partnership, host, voluntariado), las inscripciones de Luma, Discord, LinkedIn, el email events@, WhatsApp, conversaciones en persona y, sobre todo, **la memoria de Saurabh**. Son muchos canales y cada uno necesita su propia forma de extraer la información. |
| 3 | **Formato** | Es mixto. Los formularios son estructurados. Los perfiles de LinkedIn, los hilos de email, los logos, las fotos y los textos de Luma no lo son. |
| 4 | **Destino** | Su web (crewbasecollective.com, que es una app propia con eventos, personas y sponsors), la página del evento en Luma y los mensajes de outreach. |
| 5 | **Aprobación** | El brief lo dice explícitamente: todo pasa por revisión humana. La IA sugiere y el organizador decide. Nada se publica de forma automática. |
| 6 | **Costo del error** | **Medio, y sobre todo reputacional.** Un logo o un cargo mal escrito en público daña la relación con un sponsor. Invitar al inversor equivocado gasta una oportunidad de contacto. Un mal texto en Luma baja las inscripciones. Por eso el sistema propone y el organizador aprueba. |
| 7 | **Casos reales** | Hay que pedirle a Saurabh tres: un caso simple (un mixer en Homebrew Club), uno complejo (Universal Hackathon, con muchos sponsors y jueces) y uno que haya fallado. **Ya hay fallas visibles en su web:** Ali Amjad aparece dos veces, hay erratas como "Synk" en vez de Snyk, "NVDIA" o "Heat of GTM", y la página de Sponsors aparece vacía. |

**Conclusión del diagnóstico:** los tres dolores del brief (la carga manual, la elección de partners y el texto de Luma) son síntomas de un mismo problema. **El activo más valioso de Crewbase es su red de relaciones** (quién participó en qué evento, con qué rol y cómo le fue), y esa red no está registrada en ningún lado: vive en la cabeza de una persona. Mientras siga ahí, cada evento empieza de cero.

---

## 2. Decisión: construir, comprar o no automatizar

| Criterio (5 = conviene construir) | Puntaje | Por qué |
|---|---|---|
| Especificidad | 4 | Un CRM genérico guarda contactos, pero no sabe que un DevRel de Daytona encaja en un hackathon de agentes, ni conoce la voz de Crewbase. |
| Volumen y urgencia | 3 | Unos 4 eventos al mes con un equipo mínimo. El tiempo que se ahorra por evento es alto, aunque el volumen total es moderado. |
| Costo de comprar | 3 | Un CRM como Attio o HubSpot, más una herramienta de enriquecimiento como Clay, más Luma, costaría entre $100 y $300 al mes y seguiría necesitando trabajo manual para conectarlos. Ninguna combinación resuelve las recomendaciones ni el texto. |
| Tiempo hasta tener valor | 4 | Un registro unificado más las recomendaciones más el texto de Luma resuelve cerca del 80% del dolor con un prototipo. |
| Mantenimiento | 2 | Es el riesgo principal: Crewbase es básicamente una persona. La solución tiene que mantenerse sola y no requerir un desarrollador. |

**Decisión: construir**, pero sobre una plataforma existente (Converge, como piden las reglas) y no con código desde cero. La parte genérica, que es guardar contactos, no se reinventa. Lo que se construye es lo específico de Crewbase: el matching entre eventos y stakeholders, la voz de la marca y el ciclo de aprendizaje.

**Si el volumen creciera 10 veces** (unos 40 eventos al mes, varios organizadores o ciudades), la decisión se mantiene, pero la base de datos de relaciones tendría que vivir en una base real con permisos por organizador. Además, el flujo se volvería un producto que se puede vender a otras comunidades como AI Collective o BuildClub, que ya son partners de Crewbase.

---

## 3. La solución ideal, sin límite de tiempo: el "Crewbase Brain"

**Idea central:** los datos se escriben una sola vez y se publican en muchos lugares. Un grafo de relaciones vivo alimenta todo lo demás: la web, Luma, el outreach y las recomendaciones. Cada evento que termina hace que el siguiente sea más fácil.

### Las 6 piezas

**1. Grafo de relaciones (la única fuente de verdad)**
- Entidades: Organizaciones, Personas, Eventos y Participaciones. Una participación registra el rol, el estado (pedido, confirmado, rechazado o sin respuesta), el aporte (dinero, créditos o sede) y cómo salió. A eso se suman los activos (logos y fotos con sus versiones) y los temas del evento.
- Reemplaza a la web como lugar donde viven los datos. La web, Luma y los mensajes leen de aquí.

**2. Captura sin carga manual**
- Cada formulario de Get Involved crea o actualiza un registro de forma automática.
- Si se pega un link de LinkedIn, una firma de email o una foto de una tarjeta, un agente completa el perfil: cargo, empresa, logo a partir del dominio y foto.
- **Detección de duplicados y erratas**: propone fusionar los dos Ali Amjad o cambiar "Synk" por "Snyk", y el organizador lo aprueba con un clic.
- Importa los eventos y las listas de invitados pasados de Luma.
- Una **cola de calidad** reúne en una bandeja los campos faltantes, los cargos desactualizados y los logos que faltan.

**3. Del brief al plan del evento**
- El organizador escribe dos líneas o deja un mensaje de voz, por ejemplo: "hackathon de agentes, 12 de diciembre, en Frontier Tower, para 80 builders".
- El agente lo convierte en un plan: tema, audiencia, formato, y qué hace falta (por ejemplo, 3 sponsors con créditos de API, 5 jueces técnicos, 1 sede y 2 comunidades que lo difundan).

**4. Recomendaciones explicables y editables** (el área de mayor impacto, porque los sponsors son los ingresos de Crewbase)
- Cruza las necesidades del evento con el grafo usando estas señales:
  - qué tan bien encaja con el tema
  - cuándo participó por última vez
  - con qué frecuencia responde y qué tan rápido
  - si ya se le pidió demasiadas veces
  - la diversidad del panel de jueces
- Cada recomendación viene con su razón. Por ejemplo: *"Borna Perak (DevRel, Daytona): fue sponsor y juez en 3 hackathons de agentes, el último el 7 de octubre, y respondió en menos de 48 horas."*
- Muestra los vacíos. Por ejemplo: "no tienes a nadie de seguridad; prospectos sugeridos: …".
- El organizador acepta, edita, quita o agrega. **Esas ediciones entrenan las recomendaciones siguientes.**

**5. Outreach y recolección de materiales**
- Redacta un mensaje personalizado para cada rol y contacto, en la voz de Crewbase.
- Cada evento tiene su pipeline: pedido, confirmado, materiales recibidos.
- Cada sponsor recibe un **link donde sube su logo y aprueba su texto**. Así se acaba perseguir materiales por email.

**6. Estudio de texto para Luma y promoción**
- Genera el título, el gancho, la descripción, la agenda y las secciones de sponsors y jueces **a partir de los stakeholders ya confirmados**, sin volver a escribirlos.
- Aprende la voz de Crewbase de sus mejores eventos pasados.
- Evalúa el texto con una lista de chequeo (claridad, audiencia, llamado a la acción, fecha y sede) y propone variantes.
- Genera la portada con los logos de los sponsors.
- El organizador edita y después copia o envía el texto a Luma. **Nunca se publica solo.**

### El ciclo que aprende (lo que lo diferencia)
Después de cada evento se registran las inscripciones y la asistencia de Luma, quién cumplió y el feedback de los sponsors. Eso mejora tanto las recomendaciones como el texto del evento siguiente.

### Interfaz
- **Un agente conversacional** en el canal que Saurabh ya usa (Slack, WhatsApp o Discord) para pedir cosas rápidas.
- **Un panel de revisión** para aprobar sugerencias, fusionar duplicados, editar recomendaciones y textos.

### Métricas (las mismas que pide el brief)
| Impacto | Antes, a medir con Saurabh | Después, objetivo |
|---|---|---|
| Preparar un evento | X horas y N pasos repetidos **[validar]** | menos de 1 hora y 0 datos cargados dos veces |
| Calidad de los registros | % completo y número de duplicados | 95% completo y 0 duplicados |
| Decisiones de partners | — | % de recomendaciones aceptadas, tasa de respuesta, confirmados por evento |
| Promoción | tiempo para escribir el texto | menos de 10 minutos; conversión de visitas a inscripciones en Luma |
| Escala | eventos por organizador | 2 a 3 veces más sin sumar gente |

### Cómo podría aplicarse en otros contextos
El mismo sistema le sirve a cualquier organizador de comunidades (AI Collective, BuildClub, GenAI Assembling), a equipos de DevRel que manejan sponsorships, a aceleradoras y a programas universitarios. Varios de ellos ya están en el grafo de Crewbase, así que son el primer canal de distribución.

---

## 4. Cómo construirlo con Converge.AI

### Qué ofrece Converge (investigado el 17 de noviembre de 2026)

Converge reúne sus productos sobre una **capa compartida de contexto de negocio** con una sola cuenta.

| Producto | Qué es | Qué hay confirmado | Rol en la solución |
|---|---|---|---|
| **Enter Pro** | Constructor con IA de apps web, herramientas internas y agentes | Incluye base de datos, autenticación, hosting, pagos y analytics. Tiene un Plan Mode que diseña el modelo de datos y los permisos antes de escribir código, y un editor visual de formularios, reportes y flujos. Permite elegir el modelo (Claude, GPT, Gemini o Grok) y publicar al instante. Funciona en el navegador, en la terminal o por CLI. Tiene un **Agent Builder**. | **El núcleo del producto:** el grafo de relaciones, el panel de revisión, los formularios de captura, el portal para sponsors, las recomendaciones y el estudio de texto para Luma. |
| **Covey** | Workspace de IA para equipos y agentes | Solo el título del sitio. Directorios no verificados dicen que reúne recursos, conversaciones, equipo y agentes configurables, con skills que llaman a Enter y Framia, y un plan gratis de 20,000 créditos al mes. | **La interfaz del organizador:** el agente de Crewbase con el que Saurabh habla ("nuevo evento: …") y que llama a la app de Enter y a Framia. También es donde colabora nuestro equipo y donde están los 5,000 créditos. |
| **Framia Pro** | Canvas creativo con agentes para imagen, video y audio | **Tiene MCP confirmado** (`mcp-api.framia.pro/multimodal/mcp`, con OAuth), además de un CLI y un plugin. Mantiene consistentes logos e imágenes entre piezas. | La **portada del evento con los logos de los sponsors**, clips para redes y el kit de marca de cada evento. También nos sirve para **el video demo de 3 minutos**. |
| **Combos** | Plataforma para crear juegos con IA (el agente "Boo") | Genera juegos jugables en el navegador que se pueden compartir. | No es parte del núcleo. Como extra opcional podría servir para un rompehielos o un "match de co-founders" en los eventos, pero no aporta al impacto de negocio. |
| Concat Pro | Marketing y crecimiento | Anunciado como "próximamente". | A futuro, la distribución y promoción de los eventos. |

### Arquitectura con Converge

```
Saurabh ──chat──▶  COVEY: Agente Crewbase (skills: crear evento, recomendar, redactar Luma, limpiar datos)
                         │                                   │
                         ▼                                   ▼
              ENTER PRO: app "Crewbase Brain"          FRAMIA (MCP)
              • Base de datos: Orgs, Personas,          • Portada con logos
                Eventos, Participaciones, Activos       • Clips y piezas para redes
              • Formularios Get Involved → registros
              • Portal del sponsor (sube logo y aprueba su texto)
              • Cola de calidad (duplicados, erratas)
              • Recomendaciones explicables (LLM + reglas)
              • Estudio de texto para Luma (variantes + checklist)
              • Panel de revisión y métricas
                         │
                         ▼
              Luma (copiar o enviar el texto revisado) · Web de Crewbase · Outreach
```

### Pendiente de validar (antes de diseñar)
1. **Covey:** qué puede hacer de verdad. ¿Tiene agentes con skills, integraciones con Slack, Lark o Gmail, y puede llamar a una app de Enter? Hay que revisarlo dentro del workspace o preguntarlo en #ask-mentors.
2. **Enter:** si la app publicada tiene un link público (es obligatorio para el envío) y si sus agentes pueden leer URLs externas para enriquecer perfiles.
3. **Framia MCP:** si podemos conectarlo, porque pide registrar el cliente de antemano.
4. **Luma:** si Crewbase tiene Luma Plus, que da acceso a la API para crear y editar eventos. Si no, el flujo termina en "copiar al portapapeles".
5. **Saurabh:** que nos pase los datos reales (los eventos y personas de su web, o mejor la base que usa detrás) y los tiempos actuales para tener la línea base.
