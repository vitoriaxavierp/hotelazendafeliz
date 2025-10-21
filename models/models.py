from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ---------------------------
# TABELAS DO PROJETO
# ---------------------------

class Perfil(db.Model):
    __tablename__ = 'perfis'
    id = db.Column(db.Integer, primary_key=True)
    nome_perfil = db.Column(db.String(50), unique=True, nullable=False)

    usuarios = db.relationship('Usuario', backref='perfil', lazy=True)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(200), nullable=False)
    perfil_id = db.Column(db.Integer, db.ForeignKey('perfis.id'), nullable=False)


class TipoQuarto(db.Model):
    __tablename__ = 'tipos_quarto'
    id_tipo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_tipo = db.Column(db.String(50), unique=True, nullable=False)
    capacidade_maxima = db.Column(db.Integer, nullable=False)
    preco_diaria_base = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.Text)


class Quarto(db.Model):
    __tablename__ = 'quartos'
    numero_quarto = db.Column(db.String(10), primary_key=True, unique=True)
    id_tipo = db.Column(db.Integer, db.ForeignKey('tipos_quarto.id_tipo'), nullable=False)
    status_limpeza = db.Column(db.String(20), default='Sujo', nullable=False)
    localizacao = db.Column(db.String(50))

    tipo = db.relationship('TipoQuarto', backref='quartos')


class Hospede(db.Model):
    __tablename__ = 'hospedes'
    id_hospede = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_completo = db.Column(db.String(150), nullable=False)
    documento = db.Column(db.String(50), unique=True, nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    id_usuario_sistema = db.Column(db.Integer, db.ForeignKey('usuarios.id'))


class Reserva(db.Model):
    __tablename__ = 'reservas'
    id_reserva = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_hospede_principal = db.Column(db.Integer, db.ForeignKey('hospedes.id_hospede'), nullable=False)
    numero_quarto = db.Column(db.String(10), db.ForeignKey('quartos.numero_quarto'))
    data_checkin = db.Column(db.Date, nullable=False)
    data_checkout = db.Column(db.Date, nullable=False)
    status_reserva = db.Column(db.String(30), nullable=False)
    valor_total = db.Column(db.Float, nullable=False)

    hospede = db.relationship('Hospede', backref='reservas')
    quarto = db.relationship('Quarto', backref='reservas')


class Servico(db.Model):
    __tablename__ = 'servicos'
    id_servico = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_servico = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)


class Fatura(db.Model):
    __tablename__ = 'faturas'
    id_fatura = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_reserva = db.Column(db.Integer, db.ForeignKey('reservas.id_reserva'), nullable=False)
    data_emissao = db.Column(db.DateTime, nullable=False)
    valor_servicos = db.Column(db.Float, nullable=False)
    valor_diarias = db.Column(db.Float, nullable=False)
    status_pagamento = db.Column(db.String(20), nullable=False)

    reserva = db.relationship('Reserva', backref='fatura')


class ItemFatura(db.Model):
    __tablename__ = 'itens_fatura'
    id_item = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_fatura = db.Column(db.Integer, db.ForeignKey('faturas.id_fatura'), nullable=False)
    id_servico = db.Column(db.Integer, db.ForeignKey('servicos.id_servico'), nullable=False)
    quantidade = db.Column(db.Integer, default=1, nullable=False)
    preco_unitario_registro = db.Column(db.Float, nullable=False)
    data_consumo = db.Column(db.DateTime, nullable=False)

    fatura = db.relationship('Fatura', backref='itens')
    servico = db.relationship('Servico', backref='itens')
