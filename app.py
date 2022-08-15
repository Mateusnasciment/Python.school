from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec

server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title= 'teste um' )
spec.register(server)

@server.get('/pessoas') #,rots,endpoints,recursos
def buscar_pessoas() :
    return 'tudo ok'


server.run()


