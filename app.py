from flask import Flask, render_template, session, url_for, redirect
from Web_App import create_app
from flask_babel import Babel, gettext as _
from flask import redirect
from flask_bootstrap import Bootstrap
import os

app = create_app()

babel = Babel(app)
bootstrap = Bootstrap(app)

@app.route('/index')
def index():
    user = "Stefania" 
    return render_template('index.html', user=user)

@app.route('/language/<language_code>')
def set_language(language_code):
    if language_code:
        session['language'] = language_code
        return redirect(url_for('index'))

@app.before_request
def before_request():
    if 'language' in session:
        app.config['BABEL_DEFAULT_LOCALE'] = session['language']

@app.route('/more-info')
def more_info():
    return render_template('more-info.html')

@app.context_processor
def context_processor():
    languages = [
        {'name': 'English', 'code': 'en'},
        {'name': 'Español', 'code': 'es'},
        {'name': 'Romanian', 'code': 'ro'},
        {'name': 'Français', 'code': 'fr'},
    ]
    departments = [
        {"id": 1, "name": "Departamentul Ingineria Mediului, Inginerie Mecanică si Agroturism"},
        {"id": 2, "name": "Departamentul Inginerie şi Management, Mecatronică"},
        {"id": 3, "name": "Departamentul Ingineria şi Managementul Sistemelor Industriale"},
        {"id": 4, "name": "Departamentul de Energetică şi Stiinţa Calculatoarelor"},
        {"id": 5, "name": "Departamentul Inginerie Chimică şi Alimentară"}
    ]
    return dict(languages=languages, departments=departments)

# Configure Babel
app.config['BABEL_TRANSLATION_DIRECTORIES'] = os.path.join(os.path.dirname(__file__), 'translations')
babel.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)


    