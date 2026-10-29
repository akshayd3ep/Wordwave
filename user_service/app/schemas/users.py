from pydantic import BaseModel, EmailStr, Field
import uuid

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    username: str = Field(pattern=r"^[A-Za-z0-9_]{3,30}$")
    display_name: str = Field(min_length=1, max_length=100)
    phone: str | None = Field(default=None, pattern=r"^\+[1-9][0-9]{6,14}$")
    preferred_language: str = "en"


class ProfileOut(BaseModel):          
    user_id: uuid.UUID
    username: str
    display_name: str
    preferred_language: str
    avatar_url: str | None

    # @field_validator("preferred_language")
    # @classmethod
    # def check_language(cls, v):
    #     if v not in SUPPORTED_LANGUAGES:
    #         raise ValueError("unsupported language")
    #     return v