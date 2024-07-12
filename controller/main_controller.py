from flask import Flask, render_template
from service.item_service import ItemService
from service.user_service import UserService

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/items')
def items():
    item_service = ItemService()
    items = item_service.get_all_items()
    return render_template('item_list.html', items=items)

@app.route('/users/<int:user_id>')
def user_profile(user_id):
    user_service = UserService()
    user = user_service.get_user_by_id(user_id)
    return render_template('user_profile.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
