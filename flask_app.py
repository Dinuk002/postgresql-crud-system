from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

@app.route('/greet/<int:number1>/<int:number2>')
def add(number1,number2):
    return f'{number1+number2}'


@app.route('/requests')
def handle_requests():
    return render_template('index.html')

@app.route('/return' ,methods=['POST'])
def retunr_data():
    name=request.form['name']
    email=request.form['email']
    if name=="Dinuk" and email=="dinuk@example.com":
        return f'Name: {name}, Email: {email}'
    return "Invalid credentials"


@app.route('/handle_url_params')
def handle_params():
    greeting=request.args['greeting']
    name=request.args['name']
    return f'{greeting},{name}'





if __name__ == "__main__":
    app.run(debug=True)