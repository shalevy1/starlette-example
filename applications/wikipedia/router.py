from starlette.routing import Router, Route
from applications.wikipedia.endpoints import WikipediaSummary


wikipedia_router = Router([
        Route('/summary/{title}', endpoint=WikipediaSummary, methods=['GET', ])
])
