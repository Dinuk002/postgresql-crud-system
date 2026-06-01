from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

@app.route('/greet/<int:number1>/<int:number2>')
def add(number1,number2):
    return f'{number1+number2}'

@app.route('/handle_url_params')
def handle_params():
    greeting=request.args['greeting']
    name=request.args['name']

if __name__ == "__main__":
    app.run(debug=True)