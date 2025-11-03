# Hotel Fazenda Feliz 🌾

Sistema web para gerenciamento de hotel, desenvolvido em **Python + Flask + SQLite**, com controle de acesso por perfil, cadastro de usuários e gerenciamento de quartos e tipos de quarto.

Projeto acadêmico com foco em desenvolvimento web, banco de dados e autenticação.

---

## Funcionalidades

- Login e autenticação com Flask-Login  
- Controle de acesso por perfil  
- CRUD de Usuários  
- CRUD de Tipos de Quarto  
- CRUD de Quartos  
- Criação automática do usuário Administrador  
- Interface com templates Jinja2  

### 👥 Perfis do Sistema

| Perfil | Permissões |
|-------|------------|
| **Administrador** | Acesso total |
| **Recepcionista** | Reservas, check-in/out (em desenvolvimento) |
| **Camareira** | Atualização de status de limpeza |
| **Hóspede** | Acesso futuro a reservas próprias |

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|-----------|-----------|
| Python | Linguagem principal |
| Flask | Framework web |
| Flask-Login | Autenticação e sessões |
| Flask-SQLAlchemy | ORM para banco |
| SQLite | Banco local |
| HTML + CSS | Interface |
| Jinja2 | Templates |

---

## 📂 Estrutura do Projeto
```hotelfazendafeliz/
│── app.py
│── config.py
│── hotel.db
│── requirements.txt
│── README.md
├── controllers/
│   └── controller.py
├── models/
│   └── models.py
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── usuarios/
│   │   ├── listar.html
│   │   ├── novo.html
│   │   └── editar.html
│   ├── quartos/
│   │   ├── listar.html
│   │   ├── novo.html
│   │   └── editar.html
│   └── tipos_quarto/
│       ├── listar.html
│       ├── novo.html
│       └── editar.html
└── static/        
    ├── css/
    ├── js/
    └── img/```



---

## 🚀 Como Rodar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/hotelfazendafeliz.git
cd hotelfazendafeliz

2️⃣ Criar ambiente virtual
python -m venv .venv


Ativar:

Windows

.\.venv\Scripts\activate


Linux/Mac

source .venv/bin/activate

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Executar a aplicação
python app.py


Acesse em:
http://127.0.0.1:5001

🔐 Login Inicial
Email	Senha
admin@hotel.com	admin


⭐ Se você gostou deste projeto, considere deixar uma estrela no repositório!


