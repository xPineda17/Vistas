from flaskr import create_app
from .Modelos import db, Cancion, Album, Usuario, Medio, AlbumSchema
from flask_restful import Api
from flask_migrate import Migrate
from .Vistas import VistaCanciones, VistaCancion, VistaUsuario, VistaUsuarios, VistaAlbum, VistaAlbumes

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

migrate = Migrate()
migrate.init_app(app, db, compare_type=True)
api = Api(app)

api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/canciones/<int:id_cancion>')
api.add_resource(VistaUsuarios, '/usuarios')
api.add_resource(VistaUsuario, '/usuarios/<int:id_usuario>')
api.add_resource(VistaAlbumes, '/albumes')
api.add_resource(VistaAlbum, '/albumes/<int:id_album>')
