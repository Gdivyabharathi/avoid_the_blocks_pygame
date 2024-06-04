 
from flask import Blueprint, render_template
home_bp = Blueprint('home', __name__)
@home_bp.route('/')
def index():
    return render_template('home.html')#, endpoints=endpoints)

@home_bp.route('/services')
def index0():
    return render_template('services.html')#, endpoints=endpoints)

@home_bp.route('/login')
def index1():
    return render_template('login.html')#, endpoints=endpoints)

@home_bp.route('/reviews')
def index2():
    return render_template('reviews.html')#, endpoints=endpoints)

@home_bp.route('/about')
def index3():
    return render_template('aboutus.html')#, endpoints=endpoints)

@home_bp.route('/menu')
def index4():
    return render_template('menu.html')#, endpoints=endpoints)