from flask import Flask, render_template, session, url_for
from Web_App import create_app
from flask_babel import Babel, gettext as _
from flask import redirect
import sys
import os
import locale

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs' 
babel = Babel(app)

app = create_app()

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


@app.context_processor
def context_processor():
    languages = [
        {'name': 'English', 'code': 'en'},
        {'name': 'Español', 'code': 'es'},
        {'name': 'Romanian', 'code': 'ro'},
        {'name': 'Français', 'code': 'fr'},
    ]
    return dict(languages=languages)

# Configure Babel
app.config['BABEL_TRANSLATION_DIRECTORIES'] = os.path.join(os.path.dirname(__file__), 'translations')
babel.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)


    