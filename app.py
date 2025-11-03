from flask import Flask
from config import Config
from models.models import db, Usuario, Perfil
from controllers.controller import main
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(Config) 

db.init_app(app)
app.register_blueprint(main)
print(">>> Blueprints registrados:", app.blueprints)

login_manager = LoginManager(app)
login_manager.login_view = 'main.login'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        if Perfil.query.count() == 0:
            perfis = ["Administrador", "Recepcionista", "Camareira", "Hóspede"]
            for p in perfis:
                db.session.add(Perfil(nome_perfil=p))
            db.session.commit()
            print("Perfis criados com sucesso!")

        if Usuario.query.count() == 0:
            admin_perfil = Perfil.query.filter_by(nome_perfil="Administrador").first()
            admin = Usuario(
                nome_completo="Admin",
                email="admin@hotel.com",
                senha_hash="admin",
                perfil_id=admin_perfil.id
            )
            db.session.add(admin)
            db.session.commit()
            print("✅ Usuário administrador criado:")
            print("   Email: admin@hotel.com")
            print("   Senha: admin")

    print("🔎 Rotas registradas:")
    for rule in app.url_map.iter_rules():
        print(rule)

    app.run(debug=True, port=5001)