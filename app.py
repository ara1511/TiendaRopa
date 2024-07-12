from flask import Flask, render_template, redirect, url_for, flash, request
from abc import ABC, abstractmethod
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from service.item_service import ItemService
from service.user_service import UserService
from domain.item import Dress, Shirt, Item
from domain.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

users = {'ana@example.com': {'password': 'password123', 'name': 'Ana'}}


class Person(ABC):
    def __init__(self, name, email):
        self._name = name
        self._email = email

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @abstractmethod
    def get_role(self):
        pass

class User(UserMixin, Person):
    def __init__(self, email):
        super().__init__(users[email]['name'], email)
        self._password = users[email]['password']

    @property
    def password(self):
        return self._password

    @staticmethod
    def get(email):
        if email in users:
            return User(email)
        return None

    def get_role(self):
        return "User"

    @staticmethod
    def create(name, email, password):
        if email not in users:
            users[email] = {'password': password, 'name': name}
            return User(email)
        return None

@login_manager.user_loader
def load_user(email):
    return User.get(email)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.create(form.name.data, form.email.data, form.password.data)
        if user:
            login_user(user)
            flash('Registration successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Email already registered.', 'danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get(form.email.data)
        if user and user.password == form.password.data:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your email and password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/items')
def items():
    item_service = ItemService()
    items = item_service.get_all_items()
    return render_template('item_list.html', items=items)

@app.route('/users/<string:email>')
def user_profile(email):
    user = User.get(email)
    return render_template('user_profile.html', user=user)

def init_db():
    item_service = ItemService()
    item1 = Dress(id=1, name="Vestido de verano", price=19.99, category="Vestidos")
    item2 = Shirt(id=2, name="Camisa floral", price=14.99, category="Camisas")
    item_service.add_item(item1)
    item_service.add_item(item2)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
