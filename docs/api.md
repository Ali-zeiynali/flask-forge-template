# API

## Health

### `GET /api/health`

Response:

```json
{"status": "ok"}
```

## Users

Base schema for successful responses:

```json
{
    "success": true,
    "data": {},
    "meta": {}
}
```

Base schema for error responses:

```json
{
    "success": false,
    "error": {
        "code": "invalid_payload",
        "message": "Request body is required."
    }
}
```

### `POST /api/users`

Request:

```json
{
    "email": "john@example.com",
    "full_name": "John Doe",
    "is_active": true
}
```

### `GET /api/users/{id}`

Returns a single user.

### `GET /api/users?page=1&per_page=10`

Returns paginated users with `meta`:

```json
{
    "page": 1,
    "per_page": 10,
    "total": 1,
    "pages": 1
}
```

### `PATCH /api/users/{id}`

Allowed fields: `email`, `full_name`, `is_active`.

### `DELETE /api/users/{id}`

Returns HTTP `204 No Content`.
