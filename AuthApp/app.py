from flask import Flask, url_for, render_template, abort
from flask_login import LoginManager, login_required
from AuthApp.models import user


app = Flask(__name__)
app.config.from_object('AuthApp.config.authDevelConfig')
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return user(user_id)


@app.route('/private')
@login_required
def view_private():
    return render_template('private.html')






