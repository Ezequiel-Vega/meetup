from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    message = 'Hola desde el servidor de flask!!!'
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)