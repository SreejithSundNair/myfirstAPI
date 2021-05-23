from flask import Flask, jsonify, request, render_template

app = Flask(__name__)   # Application name


# Web browser: Always blank route name, and method is GET
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def math_operation():
    if (request.method == 'POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if (operation == 'add'):
            r = num1 + num2
            result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'sub'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'mul'):
            r = num1 * num2
            result = 'the multiplication of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'div'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('results.html', result=result)


@app.route('/via_postman', methods=['POST']) # for calling the API from postman
def math_operation_via_postman():
    if (request.method=='POST'):
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation == 'add'):
            r = num1+num2
            result = 'the sum of '+str(num1)+ ' and '+str(num2)+' is '+str(r)
        if (operation == 'sub'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'mul'):
            r = num1 * num2
            result = 'the multiplication of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'div'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)

if __name__ ==  '__main__':
    print('The app is working')
    app.run()