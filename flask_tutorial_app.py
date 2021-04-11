#
# Simple Flask app
#
from flask import Flask
from flask import request, abort, make_response, jsonify
from clickhouse_driver import Client

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

@app.route('/get_most_recent_stats_params', methods=['GET'])
def get_most_recent_stats_params():
    table = request.args.get('table')
    params = request.args.get('params')

    client = Client(host='localhost', port=9090)
    query = f"""
    SELECT {params} from {table}
    """

    res = client.execute(query)

    # return(f"PARAM1 {param1} PARAM2 {param2}\n")
    return jsonify(res)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found. Bad luck!'}), 404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
