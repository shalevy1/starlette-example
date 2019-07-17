import wikipedia

from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse


class WikipediaSummary(HTTPEndpoint):
    async def get(self, request):
        summary = wikipedia.summary(request.path_params['title'])
        return JSONResponse({'summary': summary})
