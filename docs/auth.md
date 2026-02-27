# Authentication Guide

Authentication is implemented with `Flask-JWT-Extended` and Argon2 password hashing.

## Flow

1. Register (`POST /api/auth/register`) or seed/create users through CLI.
2. Login (`POST /api/auth/login`) to get access and refresh tokens.
3. Use access token for protected endpoints.
4. Refresh access token via `POST /api/auth/refresh` with refresh token.
5. Revoke current access token via `POST /api/auth/logout`.

## Notes

- `GET /api/auth/me` returns the authenticated user profile.
- Logout uses in-memory token revocation, which is suitable for a template/dev setup.
- Existing legacy `scrypt` password hashes are still verifiable; new hashes use Argon2.
