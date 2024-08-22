from flask import Blueprint, render_template, request, redirect, url_for, session,g
from bson.objectid import ObjectId
from inventory.db import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    print(g.user,"1")
    employees = mongo.db.employees.find()
    return render_template('index.html', employees=employees)

@main.route('/employee/<id>')
def employee(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    employee = mongo.db.employees.find_one_or_404({'_id': ObjectId(id)})
    return render_template('employee.html', employee=employee)

@main.route('/add', methods=['GET', 'POST'])
def add_employee():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        name = request.form['name']
        position = request.form.get('position')
        salary = request.form.get('salary')
        mongo.db.employees.insert_one({'name': name, 'position': position, 'salary': salary})
        return redirect(url_for('main.index'))
    return render_template('add_employee.html')

@main.route('/edit/<id>', methods=['GET', 'POST'])
def edit_employee(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    employee = mongo.db.employees.find_one_or_404({'_id': ObjectId(id)})
    if request.method == 'POST':
        name = request.form.get('name')
        position = request.form.get('position')
        salary = request.form.get('salary')
        mongo.db.employees.update_one({'_id': ObjectId(id)}, {'$set': {'name': name, 'position': position, 'salary': salary}})
        return redirect(url_for('main.employee', id=id))
    return render_template('edit_employee.html', employee=employee)

@main.route('/delete/<id>', methods=['POST'])
def delete_employee(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    mongo.db.employees.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('main.index'))

