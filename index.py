from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key_here"

# Criar um usuário exemplo
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password

users = [User(1, "admin", "password")]

# Configurar o gerenciador de login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

# Rota para login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        for user in users:
            if user.username == username and user.check_password(password):
                login_user(user)
                return redirect(url_for("index"))
        return "Usuário ou senha inválidos", 401
    return render_template("login.html")

# Rota para logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

# Rota para página inicial (protegida por login)
@app.route("/")
@login_required
def index():
    return "Você está logado!"

if __name__ == "__main__":
    app.run(debug=True)
