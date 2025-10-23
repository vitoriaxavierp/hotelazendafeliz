from flask import Flask
from config import Config
from models.models import db
from controllers.controller import main
from models.models import Perfil



app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(main)
print(">>> Blueprints registrados:", app.blueprints)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if Perfil.query.count() == 0:
            perfis = ["Administrador", "Recepcionista", "Camareira", "Hóspede"]
            for p in perfis:
                db.session.add(Perfil(nome_perfil=p))
        db.session.commit()
        print("Perfis criados com sucesso!")

    print("Rotas registradas:")
    for rule in app.url_map.iter_rules():
        print(rule)
    app.run(debug=True, port=5001)