from fastapi import FastAPI
from core.config import settings
# from db.base_class import Base
# from db.base import Base
from db.session import engine
from apis.base import api_router
from apps.base import app_router
from fastapi.staticfiles import StaticFiles

# def create_tables():
#     Base.metadata.create_all(bind=engine)

def include_routers(app):
    app.include_router(api_router)
    app.include_router(app_router)

def configure_static_files(app: FastAPI):
    app.mount("/static", StaticFiles(directory="static"),name="static")

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    # create_tables()
    include_routers(app)
    configure_static_files(app)
    return app

app = start_application()

# @app.get("/")
# def hello():
#     return {"msg": "Hello Fast API "}
