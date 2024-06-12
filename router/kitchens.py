from fastapi import APIRouter

from library.constant.api_constant import V1_KITCHEN

route = APIRouter()


@route.get(V1_KITCHEN)
async def root():
  return {"message": "Hello World"}
