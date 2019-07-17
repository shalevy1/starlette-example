from starlette.applications import Starlette
from applications.wikipedia import wikipedia_router

from settings import DEBUG

app = Starlette()

app.debug = DEBUG

app.mount('/', app=wikipedia_router)
