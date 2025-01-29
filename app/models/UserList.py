from pydantic import BaseModel, EmailStr, HttpUrl, RootModel


class User(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl


class UserList(RootModel):
    root: list[User]
