# Sajjad Rehab — MCP server

A read-only informational MCP service for Sajjad Rehabilitation & Therapy Centre.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 8000
```

- Health check: `http://localhost:8000/health`
- MCP streamable HTTP: `http://localhost:8000/mcp`

## Deploy to Render

1. Upload these files to a GitHub repository.
2. Render → New → Blueprint → select repository and deploy `render.yaml`.
3. Verify `https://YOUR-RENDER-HOST/health` returns `status: ok`.
4. Test the `/mcp` endpoint with MCP Inspector. Replace the placeholder URL in `mcp.json` with the real HTTPS endpoint.
5. Host privacy policy, terms and support pages on the verified Sajjad Rehab domain. Verify domain ownership and publisher identity.
6. Prepare the plugin metadata, required icon assets, five positive and three negative review cases, and demo video following the official plugin package guide. Upload the **submission ZIP** (not this source ZIP) in ChatGPT Plugins.

## Important

This is a deployable MCP **server source package**, not an approved or submission-ready plugin listing. The plugin manifest, screenshots, review assets and public HTTPS URL must be finalized after hosting. The directory does not guarantee a dofollow backlink or SEO benefit.

## Privacy

Tools are read-only and accept no patient identity or medical record fields. Do not log health data or add booking writes without consent, authentication, and a separate privacy/security review.

## Source links

- https://www.sajjadrehab.in/
- https://www.sajjadrehab.in/contact
- https://www.sajjadrehab.in/book-appointment
- https://developers.openai.com/plugins/deploy/submission
