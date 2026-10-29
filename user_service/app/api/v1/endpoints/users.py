from fastapi import APIRouter, status

user_router = APIRouter(prefix="/user", tags=["Users Services"])

@user_router.post("/", status_code=  status.HTTP_200_OK)
def user_create(user):

