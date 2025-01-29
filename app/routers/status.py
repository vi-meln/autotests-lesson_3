from http import HTTPStatus
from fastapi import APIRouter
from app.database.engine import check_availability
from app.models.Status import Status

router = APIRouter()


@router.get("/status", status_code=HTTPStatus.OK)
def status() -> Status:
    return Status(database=check_availability())
