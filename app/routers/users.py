from http import HTTPStatus
from fastapi import APIRouter, HTTPException
from app.database import users
from app.models.User import User, UserCreate, UserUpdate

router = APIRouter(prefix="/api/users")


@router.get("/{user_id}", status_code=HTTPStatus.OK)
def get_user(user_id: int) -> User:
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")
    user = users.get_user(user_id)

    if not user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return {
        "id": user.id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "avatar": user.avatar
    }


@router.get("/", status_code=HTTPStatus.OK)
def get_users() -> list[User]:
    return users.get_users()


@router.post("/", status_code=HTTPStatus.CREATED)
def create_user(user: User) -> User:
    try:
        UserCreate.model_validate(user.model_dump())
        new_user = users.create_user(user)
        return {
            "id": new_user.id,
            "email": new_user.email,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "avatar": new_user.avatar
        }
    except Exception:
        raise HTTPException(status_code=400, detail=f"Request body sent incorrectly")


@router.patch("/{user_id}", status_code=HTTPStatus.OK)
def update_user(user_id: int, user: User) -> User:
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")
    UserUpdate.model_validate(user.model_dump())
    edit_user = users.update_user(user_id, user)
    return {
        "id": edit_user.id,
        "email": edit_user.email,
        "first_name": edit_user.first_name,
        "last_name": edit_user.last_name,
        "avatar": edit_user.avatar
    }


@router.delete("/{user_id}", status_code=HTTPStatus.OK)
def delete_user(user_id: int):
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")
    users.delete_user(user_id)
    return {"message": "User deleted"}
