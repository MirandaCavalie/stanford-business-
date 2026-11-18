# Converge.AI: qué herramientas tenemos

Explorado el 17 de noviembre de 2026 en las páginas públicas de covey.converge.ai, sin iniciar sesión. Lo que requiere cuenta queda marcado como **[con login]**.

## Covey: el workspace y el orquestador

Secciones de la barra lateral: **New task** (chat con el agente), **Scheduled** (tareas programadas), **Agents**, **Marketplace**, **Assets** y **Projects**. Las acciones rápidas de la página de inicio son Make slides, Deep research, Create websites y Schedule task.

### Agents
- Se puede crear un agente desde cero ("Set it up once, and your agent keeps the work moving") o partir de una plantilla.
- Plantillas útiles para Crewbase:
  - **Knowledge Expert** (Notion): responde con citas a partir de documentos.
  - **Sales Researcher** (Salesforce, HubSpot): perfila empresas y stakeholders.
  - **Operations Analyst** (Sheets, BigQuery): valida datos y detecta anomalías.
  - **Campaign Strategist**, **Social Media Writer**, **Content Remix Writer** y **Email Writer** (Gmail).

### Plugins (Marketplace)
| Categoría | Plugins |
|---|---|
| **Oficiales de Converge** | **Enter** (apps, webs y agentes full-stack), **Framia** (anuncios, video, kit de marca), **Combos** (juegos), **Browser Use** (Covey usa tu Chrome local, con tus sesiones abiertas) |
| Productividad | Airtable, Google Sheets, Docs, Drive, Slides, Calendar, Notion, HubSpot, Confluence, Linear, Outlook, OneDrive, Teams, QuickBooks, Google Analytics, Search Console |
| **Comunicación** | **Gmail, WhatsApp, Discord, Slack, Telegram, Instagram, X**, Zoom, Lark, Feishu |
| Creatividad | Canva, Figma, Contentful, Wix, Twitch |
| Herramientas para desarrolladores | **Firecrawl**, **Supabase**, GitHub, GitLab, Stripe, BigQuery, ClickHouse, Databricks, Sentry |
| Gestión | Jira, Asana, monday.com |
| Negocio | **Mailchimp**, Pipedrive, Intercom, Zendesk, Zoho Desk, Google Ads, Meta Ads, TikTok Ads |

- **No hay plugin de Luma.** Las opciones son **Browser Use** (Covey maneja Luma desde tu Chrome) o copiar y pegar el texto revisado.
- Hay un botón **Create** para crear plugins propios **[con login]**. Falta confirmar si acepta MCP o API.

## Enter Pro: el constructor de la app
Según su sitio y los comunicados de prensa:
- Crea apps web, herramientas internas y agentes describiéndolos en lenguaje natural.
- Incluye base de datos, autenticación, hosting, pagos y analytics.
- Tiene un Plan Mode que diseña el modelo de datos y los permisos antes de programar, y un editor visual de formularios, reportes y flujos.
- Permite elegir el modelo (Claude, GPT, Gemini o Grok), publicar al instante y tiene un Agent Builder.
- Es un plugin dentro de Covey, así que un agente de Covey puede pedirle a Enter que construya o modifique la app.

## Framia: lo creativo
- Imagen, video y audio en un canvas con agentes, y kits de marca con logos consistentes.
- MCP en `mcp-api.framia.pro/multimodal/mcp`, con OAuth. También es plugin dentro de Covey.

## Combos
- Juegos con IA. No aporta al problema central.

---

## Cómo encaja con la solución (ver SOLUCION.md)

| Pieza del "Crewbase Brain" | Herramienta de Converge |
|---|---|
| Grafo de relaciones (base de datos) | **Enter** (base de datos propia), o **Supabase** o **Airtable** a través de Covey |
| Panel de revisión, portal para sponsors, formularios | **Enter** (app publicada con link) |
| Captura de la bandeja de entrada y de los formularios | **Covey + Gmail / Discord / WhatsApp** y tareas programadas en **Scheduled** |
| Enriquecer perfiles (LinkedIn, logo, descripción) | **Covey + Firecrawl** o **Browser Use** |
| Detectar duplicados y erratas | Agente de Covey (estilo **Operations Analyst**) sobre la base de datos |
| Recomendaciones explicables | Agente de Covey o lógica dentro de **Enter** (LLM con datos del grafo) |
| Outreach a sponsors y jueces | **Covey + Gmail / WhatsApp / Discord** (borradores; un humano los envía) |
| Texto para Luma | Agente de Covey, más **Browser Use** para cargarlo en Luma tras la revisión |
| Portada y piezas para redes | **Framia** |
| Difusión | **Covey + X / Instagram / Discord / Mailchimp** |
| Video demo del hackathon | **Framia** |

## Por revisar con sesión iniciada
1. Si **Create plugin** acepta MCP o API (para conectar la base de datos de Enter con el agente de Covey).
2. Si los agentes de Covey se pueden compartir o publicar, por ejemplo para que Saurabh los use.
3. Si **Scheduled** puede dispararse con eventos (por ejemplo, un formulario nuevo) o solo por horario.
4. Cuántos créditos gasta cada acción. Tenemos 5,000.
5. Si Enter genera un link público para el prototipo (lo exige el envío).
