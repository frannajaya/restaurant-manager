from fastapi import APIRouter

from library.constant.api_constant import HEALTH

route = APIRouter()


@route.get(HEALTH)
async def health():
  # add all dependency to this health check
  return {
    "message": "Hello World"
  }
