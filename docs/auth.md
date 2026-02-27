# Authentication

## Endpoints

- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/auth/refresh`
- `POST /api/auth/logout`
- `GET /api/auth/me`

Versioned aliases exist under `/api/v1/auth/*`.

## Notes

- Access/refresh tokens are JWT-based.
- Password hashing uses Argon2.
- Refresh requires refresh token.
- Logout revokes the current access token in memory blocklist.
