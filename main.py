from fastapi import FastAPI

from router import customers, kitchens, roots

app = FastAPI()

app.include_router(roots.route)
app.include_router(kitchens.route)
app.include_router(customers.route)
