#
# Simple Flask app
#
from flask import Flask
from flask import request, abort, make_response, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/do_something/<int:my_param>', methods=['POST'])
def do_something(my_param):
    return(f"PARAMETER {my_param}\nPOST DATA: {request.json}\n")

@app.route('/do_something_with_params', methods=['GET'])
def do_something_with_params():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    return(f"PARAM1 {param1} PARAM2 {param2}\n")

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found. Bad luck!'}), 404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
