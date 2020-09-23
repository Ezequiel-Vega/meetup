from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__, 
   static_folder='../frontend/dist/static',
   template_folder='../frontend/dist'
)

@app.route('/api/v1/message')
def message():
   return jsonify('Nuevo mensaje desde el servidor Flask')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
   return render_template('index.html')

if __name__ == "__main__":
   app.run(port=3000, debug=True)