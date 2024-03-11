from flask import Flask, render_template
from Web_App import create_app

app = Flask(__name__, static_url_path='/static')

app = create_app()

@app.route('/index')
def index():
    user = "Stefania" 
    return render_template('index.html', user=user) 
    

if __name__ == '__main__':
    app.run(debug=True)

    