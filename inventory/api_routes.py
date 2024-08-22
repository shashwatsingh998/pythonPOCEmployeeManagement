from flask_restx import Api,Resource
from inventory.db import mongo



api=Api(doc='/api/docs')

@api.route("/employees")
class Employees(Resource):
    def get(self):
        employees=mongo.db.employees.find()
        employee_list=[]
        for employee in employees:
            employee_list.append({
                'id':str(employee['_id']),
                'name':employee['name'],
                'salary':employee['salary'],
                'position':employee['position']
            })
        return {'employees':employee_list}

