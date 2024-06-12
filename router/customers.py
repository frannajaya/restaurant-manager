from fastapi import APIRouter

from library.constant.api_constant import V1_CUSTOMER

route = APIRouter()


@route.get(V1_CUSTOMER)
async def root():
  return {"message": "Hello World"}
