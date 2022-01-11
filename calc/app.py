from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def math_add():

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)

    return str(result)

@app.route('/sub')
def math_sub():

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)

    return str(result)

@app.route('/mult')
def math_mult():

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)

    return str(result)

@app.route('/div')
def math_div():

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)

    return str(result)

operations = {
  "add": add,
  "sub": sub,
  "mult": mult,
  "div": div,
}

@app.route('/math/<operator>')
def do_math(operator):
  a = int(request.args.get('a'))
  b = int(request.args.get('b'))
  result = operations[operator](a, b)

  return str(result)