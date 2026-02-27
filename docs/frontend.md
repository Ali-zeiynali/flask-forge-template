# Frontend Landing

The template now ships with a lightweight web blueprint that serves a modern dark landing page at `/`.

## Structure

- `src/web/__init__.py`
- `src/web/routes.py`
- `src/web/templates/index.html`

## Design system

- TailwindCSS is loaded from CDN (`https://cdn.tailwindcss.com`) to avoid a local build step.
- Landing uses a responsive grid, dark theme palette, card-based status indicators, and inline SVG artwork.
- No external image dependency is required.

## Content blocks

- Hero title/subtitle for project identity.
- CTA links:
  - API Health (`/api/health`)
  - Docs (`DOCS_URL` config)
  - GitHub (`GITHUB_URL` config)
- Runtime status cards for environment, app version, database engine, auth mode, and CI status.

## Customization

1. Edit `src/web/templates/index.html` for visual changes.
2. Update `DOCS_URL`, `GITHUB_URL`, and `CI_STATUS` in environment config.
3. Optionally disable the web route by removing `web_bp` registration in `src/app.py`.
