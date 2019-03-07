from flask import Flask, jsonify, request
from flask_cors import CORS
from OperationCenter import OperationCenter

app = Flask(__name__)
CORS(app)

def __new__(self):
    pass

@app.route('/inputQueries', methods=['POST'])
def inputQueries():
    content = request.get_json()
    # print(content)
    operationCenter = OperationCenter()
    operationCenter.intakeUserInput(content)
    return "Query received"

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=4444)