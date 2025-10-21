from fastapi import FastAPI, status, Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


#Middleware para controlar los errores
class HTTPErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app:FastAPI) -> None:
        super().__init__(app)  #le pasamos como parametro a nuestra app su metodo inicializador
        
    async def dispatch(self, request: Request , call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)  
            #Este middleware continua con la siguiente ejecucion 
            #que seria nuestro http y la funcion que tenga definida
        except Exception as e:
            content = f"exc: {str(e)}"
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return JSONResponse(content=content, status_code=status_code)
    