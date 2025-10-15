from app import app, db
from models import Usuario
from utils import hash_password

with app.app_context():
    db.create_all()

    admin = Usuario.query.filter_by(matricula="0001").first()

    if not admin:
        admin = Usuario(
            matricula="0001",
            nome="Administrador do Sistema",
            email="admin@recife.pe.gov.br",
            senha=hash_password("admin123"),
            role="admin"
        )
        db.session.add(admin)
        db.session.commit()
        print("✅ Admin criado (matrícula=0001, senha=admin123).")
    else:
        admin.senha = hash_password("admin123")
        admin.role = "admin"
        db.session.commit()
        print("🔑 Admin já existia; senha/role atualizados.")
