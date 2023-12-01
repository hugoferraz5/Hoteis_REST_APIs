from flask import Flask, jsonify
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import User, UserRegister, UserLogin, UserLogout, UserConfirm
from resources.site import Site, Sites
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone' # garantir a integridade e a autenticidade dos tokens gerados
app.config['JWT_BLACKLIST_ENABLED'] = True # revoga tokens(joga eles na lista negra) após o logout e antes dele expirar o prazo
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=1)
jwt = JWTManager(app) # gerenciar os tokens no app flask
api = Api(app)

@app.before_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blocklist_loader # verificar se um token está na blacklist
def verifica_blacklist(self, token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader # verificar se um token está válido qd fazemos uma requisição
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({'message': 'You have been logged out.'}), 401

api.add_resource(Hoteis, "/hoteis")
api.add_resource(Hotel, "/hoteis/<string:hotel_id>")
api.add_resource(User, "/usuarios/<int:user_id>")
api.add_resource(UserRegister, "/cadastro")
api.add_resource(UserLogin, "/login")
api.add_resource(UserLogout, "/logout")
api.add_resource(Sites, "/sites")
api.add_resource(Site, "/sites/<string:url>")
api.add_resource(UserConfirm, "/confirmacao/<int:user_id>")


if __name__ == "__main__":
    from sql_alchemy import banco

    banco.init_app(app)
    app.run(debug=True)

# http://127.0.0.1:5000/hoteis
