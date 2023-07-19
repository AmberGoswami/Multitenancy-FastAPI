from fastapi import FastAPI,Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from .api.tenant import tenant_controller
from .api.authentication import auth_controller
from .api.public import public_controller
# models.Base.metadata.create_all(bind=engine)

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tenant_controller.router)
app.include_router(auth_controller.router)
app.include_router(public_controller.router)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")