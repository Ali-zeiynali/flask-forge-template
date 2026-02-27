from __future__ import annotations

from datetime import UTC, datetime

from extensions.db import db

user_roles = db.Table(
    "user_roles",
    db.Column(
        "user_id", db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    ),
    db.Column(
        "role_id", db.Integer, db.ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True
    ),
)

role_permissions = db.Table(
    "role_permissions",
    db.Column(
        "role_id", db.Integer, db.ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True
    ),
    db.Column(
        "permission_id",
        db.Integer,
        db.ForeignKey("permissions.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    full_name = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(UTC))
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )
    roles = db.relationship("Role", secondary=user_roles, back_populates="users", lazy="joined")

    def has_role(self, role_name: str) -> bool:
        return any(role.name == role_name for role in self.roles)

    def has_permission(self, permission_name: str) -> bool:
        return any(
            permission.name == permission_name
            for role in self.roles
            for permission in role.permissions
        )

    def to_dict(self) -> dict[str, object]:
        return {
            "id": self.id,
            "email": self.email,
            "full_name": self.full_name,
            "is_active": self.is_active,
            "roles": sorted({role.name for role in self.roles}),
        }


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    description = db.Column(db.String(255), nullable=True)
    users = db.relationship("User", secondary=user_roles, back_populates="roles")
    permissions = db.relationship("Permission", secondary=role_permissions, back_populates="roles")

    def to_dict(self) -> dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "permissions": sorted({permission.name for permission in self.permissions}),
        }


class Permission(db.Model):
    __tablename__ = "permissions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    description = db.Column(db.String(255), nullable=True)
    roles = db.relationship("Role", secondary=role_permissions, back_populates="permissions")

    def to_dict(self) -> dict[str, object]:
        return {"id": self.id, "name": self.name, "description": self.description}
