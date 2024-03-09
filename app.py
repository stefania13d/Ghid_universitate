from flask import Flask, render_template
from Web_App import create_app

app = Flask(__name__, static_url_path='/static')

app.route('/')
def home():
    return render_template('base.html')

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

   