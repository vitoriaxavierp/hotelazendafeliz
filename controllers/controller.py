from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.models import db, Usuario, Perfil, TipoQuarto, Quarto
from flask_login import login_user, logout_user, current_user, login_required

main = Blueprint('main', __name__)

@main.route('/')
def index():    
    return render_template('index.html')

# -----------------------------
# CRUD de USUÁRIOS
# -----------------------------

@main.route('/usuarios')
@login_required
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios/listar.html', usuarios=usuarios)

@main.route('/usuarios/novo', methods=['GET', 'POST'])
@login_required
def novo_usuario():
    perfis = Perfil.query.all()

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        perfil_id = request.form['perfil']

        novo = Usuario(nome_completo=nome, email=email, senha_hash=senha, perfil_id=perfil_id)
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('main.listar_usuarios'))

    return render_template('usuarios/novo.html', perfis=perfis)

@main.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    perfis = Perfil.query.all()

    if request.method == 'POST':
        usuario.nome_completo = request.form['nome']
        usuario.email = request.form['email']
        usuario.senha_hash = request.form['senha']
        usuario.perfil_id = request.form['perfil']
        db.session.commit()
        return redirect(url_for('main.listar_usuarios'))

    return render_template('usuarios/editar.html', usuario=usuario, perfis=perfis)

@main.route('/usuarios/excluir/<int:id>')
@login_required
def excluir_usuario(id):
    if current_user.perfil.nome_perfil != 'Administrador':
        flash('Apenas administradores podem excluir usuários.', 'warning')
        return redirect(url_for('main.listar_usuarios'))
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('main.listar_usuarios'))


# -------------------------------------
# CRUD DE TIPOS DE QUARTO
# -------------------------------------

@main.route('/tipos_quarto')
@login_required
def listar_tipos_quarto():
    tipos = TipoQuarto.query.all()
    return render_template('tipos_quarto/listar.html', tipos=tipos)

@main.route('/tipos_quarto/novo', methods=['GET', 'POST'])
@login_required
def novo_tipo_quarto():
    if request.method == 'POST':
        nome = request.form['nome']
        capacidade = request.form['capacidade']
        preco = request.form['preco']
        descricao = request.form['descricao']

        novo = TipoQuarto(nome_tipo=nome, capacidade_maxima=capacidade, preco_diaria_base=preco, descricao=descricao)
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('main.listar_tipos_quarto'))

    return render_template('tipos_quarto/novo.html')

@main.route('/tipos_quarto/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_tipo_quarto(id):
    tipo = TipoQuarto.query.get_or_404(id)
    if request.method == 'POST':
        tipo.nome_tipo = request.form['nome']
        tipo.capacidade_maxima = request.form['capacidade']
        tipo.preco_diaria_base = request.form['preco']
        tipo.descricao = request.form['descricao']
        db.session.commit()
        return redirect(url_for('main.listar_tipos_quarto'))
    return render_template('tipos_quarto/editar.html', tipo=tipo)

@main.route('/tipos_quarto/excluir/<int:id>')
@login_required
def excluir_tipo_quarto(id):
    tipo = TipoQuarto.query.get_or_404(id)
    db.session.delete(tipo)
    db.session.commit()
    return redirect(url_for('main.listar_tipos_quarto'))


# -------------------------------------
# CRUD DE QUARTOS
# -------------------------------------

@main.route('/quartos')
@login_required
def listar_quartos():
    quartos = Quarto.query.all()
    return render_template('quartos/listar.html', quartos=quartos)

@main.route('/quartos/novo', methods=['GET', 'POST'])
@login_required
def novo_quarto():
    tipos = TipoQuarto.query.all()
    if request.method == 'POST':
        numero = request.form['numero']
        id_tipo = request.form['tipo']
        status = request.form['status']
        localizacao = request.form['localizacao']

        novo = Quarto(numero_quarto=numero, id_tipo=id_tipo, status_limpeza=status, localizacao=localizacao)
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('main.listar_quartos'))

    return render_template('quartos/novo.html', tipos=tipos)

@main.route('/quartos/editar/<string:numero>', methods=['GET', 'POST'])
@login_required
def editar_quarto(numero):
    quarto = Quarto.query.get_or_404(numero)
    tipos = TipoQuarto.query.all()

    if request.method == 'POST':
        quarto.id_tipo = request.form['tipo']
        quarto.status_limpeza = request.form['status']
        quarto.localizacao = request.form['localizacao']
        db.session.commit()
        return redirect(url_for('main.listar_quartos'))

    return render_template('quartos/editar.html', quarto=quarto, tipos=tipos)

@main.route('/quartos/excluir/<string:numero>')
@login_required
def excluir_quarto(numero):
    quarto = Quarto.query.get_or_404(numero)
    db.session.delete(quarto)
    db.session.commit()
    return redirect(url_for('main.listar_quartos'))

# -------------------------------------
# LOGIN E LOGOUT
# -------------------------------------

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = Usuario.query.filter_by(email=email, senha_hash=senha).first()

        if usuario:
            login_user(usuario)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Usuário ou senha incorretos.', 'danger')
    
    return render_template('login.html')


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout realizado.', 'info')
    return redirect(url_for('main.login'))