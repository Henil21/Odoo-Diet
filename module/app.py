from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from module import db,User
from module import app


# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# # In-memory user storage (for demonstration purposes)
# users = {}


# @login_manager.user_loader
# def load_user(user_id):
#     if user_id in users:
#         return User(user_id)
#     return None

# @app.route('/')
# def index():
#     if current_user.is_authenticated:
#         return render_template('index.html', name=users[current_user.id]['name'])
#     return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         # Redirect authenticated users to the homepage
#         return redirect(url_for('index'))

#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
        
        
#         # Assuming users is a dictionary with email as key and user info as value
#         # This should be replaced with a database query in a production application
#         user = User.query.filter_by(email=email).first()
        
#         if user and check_password_hash(user.password, password):
#             login_user(user)
#             return redirect(url_for('index'))
#         else:
#             flash('Invalid email or password')

#     return render_template('login.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         name = request.form['name']
#         user = User.query.filter_by(email=email).first()
#         if user:
#             flash('Email address already exists')
#         else:
#             new_user = User(email=email, password=generate_password_hash(password), name=name)
#             db.session.add(new_user)
#             db.session.commit()
#             flash('Account created successfully. Please log in.')
#             return redirect(url_for('login'))
#     return render_template('signup.html')

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))

@app.route('/api/calculate', methods=['POST'])
@login_required
def calculate():
    data = request.json
    age = data['age']
    gender = data['gender']
    height = data['height']
    weight = data['weight']
    activity_level = data['activity_level']
    dietary_preferences = data['dietary_preferences']
    allergies = data['allergies']
    goal = data['goal']

    # Calculate BMR
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    activity_multiplier = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725
    }

    caloric_needs = bmr * activity_multiplier[activity_level]

    # Generate meal plan
    if dietary_preferences == 'vegetarian':
        meal_plan = {
            'breakfast': "Oatmeal with fruits and nuts",
            'lunch': "Quinoa salad with vegetables",
            'dinner': "Vegetable stir-fry with tofu",
            'snacks': "Greek yogurt with honey, Mixed nuts"
        }
    elif dietary_preferences == 'vegan':
        meal_plan = {
            'breakfast': "Smoothie with almond milk, spinach, and banana",
            'lunch': "Chickpea salad with avocado",
            'dinner': "Lentil soup with whole grain bread",
            'snacks': "Fruit salad, Hummus with carrot sticks"
        }
    elif dietary_preferences == 'keto':
        meal_plan = {
            'breakfast': "Scrambled eggs with avocado",
            'lunch': "Grilled chicken salad with olive oil",
            'dinner': "Salmon with asparagus",
            'snacks': "Cheese slices, Almonds"
        }
    else:
        meal_plan = {
            'breakfast': "Eggs and toast",
            'lunch': "Chicken sandwich with salad",
            'dinner': "Grilled fish with vegetables",
            'snacks': "Apple slices with peanut butter, Yogurt"
        }

    return jsonify({'caloric_needs': caloric_needs, 'meal_plan': meal_plan})


