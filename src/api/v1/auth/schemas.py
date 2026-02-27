from __future__ import annotations

from typing import TypedDict


class RegisterRequest(TypedDict):
    email: str
    full_name: str
    password: str


class LoginRequest(TypedDict):
    email: str
    password: str


class TokenResponse(TypedDict):
    access_token: str
    refresh_token: str


class RefreshResponse(TypedDict):
    access_token: str


class MeResponse(TypedDict):
    id: int
    email: str
    full_name: str
    is_active: bool
    roles: list[str]
