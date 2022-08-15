from urllib import response
from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec
from pydantic import BaseModel


class Endpoint(BaseModel):
    id: int
    nome: str
    idade: int

server = Flask(__name__)
spec = FlaskPydanticSpec ('flask', title='live')
spec.register(server)

@server.get('/endpoint') #,rots,endpoints,recursos
@spec.validate(resp=Response(Http_200=endpoint))
def buscar_pessoas():
    return 'tudo ok'


server.run()


