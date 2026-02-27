# Configuration

## Environment variables

- `FLASK_ENV`: `development`, `testing`, `production`
- `APP_NAME`: app name used in config
- `SECRET_KEY`: Flask secret key
- `DATABASE_URL`: SQLAlchemy connection string
- `LOG_LEVEL`: logging level, default `INFO`

## Defaults

- Development DB: `sqlite:///./dev.db`
- Testing DB: in-memory SQLite

## Config selection

`get_config` selects config from explicit app-factory argument first, then `FLASK_ENV`, and falls back to development.
