from flask import Blueprint, render_template

dept = Blueprint('dept', __name__, template_folder='templates')

departments = [
    {"id": 1, "name": "Departamentul Ingineria Mediului, Inginerie Mecanică si Agroturism"},
    {"id": 2, "name": "Departamentul Inginerie şi Management, Mecatronică"},
    {"id": 3, "name": "Departamentul Ingineria şi Managementul Sistemelor Industriale"},
    {"id": 4, "name": "Departamentul de Energetică şi Stiinţa Calculatoarelor"},
    {"id": 5, "name": "Departamentul Inginerie Chimică şi Alimentară"}
]

@dept.route('/dept/<int:dept_id>')
def dept_page(dept_id):
    # Find the department with the given ID
    dept = next((d for d in departments if d['id'] == dept_id), None)
    if dept is None:
        return "Department not found", 404
    return render_template('dept.html', department=dept)

@dept.route('/departament_1')
def departament_1():
    return render_template('departament_1.html')

@dept.route('/departament_2')
def departament_2():
    return render_template('departament_2.html')

@dept.route('/departament_3')
def departament_3():
    return render_template('departament_3.html')

@dept.route('/departament_4')
def departament_4():
    return render_template('departament_4.html')

@dept.route('/departament_5')
def departament_5():
    return render_template('departament_5.html')
                           

# Register the Blueprint with the Flask app
def create_dept_blueprint(app):
    app.register_blueprint(dept)
    