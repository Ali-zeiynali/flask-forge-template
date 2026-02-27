# Frontend Landing Page

The template includes a simple landing page served at `/`.

## Purpose

- Confirm the app is running
- Provide quick links to health/docs/repository
- Show runtime metadata (environment, version, database engine)

## Files

- `src/web/__init__.py`
- `src/web/routes.py`
- `src/web/templates/index.html`

## Customization

1. Edit `src/web/templates/index.html` for content/design changes.
2. Update `DOCS_URL`, `GITHUB_URL`, and `CI_STATUS` in `.env`.
3. Remove web blueprint registration from `src/app.py` if you want API-only mode.
