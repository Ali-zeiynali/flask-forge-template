# RBAC Guide

## Default roles and permissions

Roles seeded by `flask forge seed`:

- `admin`
- `staff`
- `user`

Permissions seeded by default:

- `users:read`
- `users:write`
- `roles:read`
- `roles:write`
- `permissions:read`
- `permissions:write`

## Enforcement helpers

Decorators from `src/core/authz.py`:

- `@require_auth`
- `@require_roles(*roles)`
- `@require_permissions(*permissions)`
- `@require_owner_or_permission(permission, owner_param="user_id")`

## How to add new permissions

1. Add permission name to your role matrix in `DEFAULT_ROLE_PERMISSIONS` (`src/cli.py`).
2. Run `python -m flask --app flaskforge.wsgi:app forge seed`.
3. Protect endpoints with `@require_permissions("your:new-permission")`.
4. Add tests to confirm allowed/denied behavior.
