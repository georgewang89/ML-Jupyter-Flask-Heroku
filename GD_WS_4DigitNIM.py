from flask import Flask,jsonify,request
from Model.Dataseed import tasks
from Model.Petal import Petal

app = Flask(__name__)


@app.route('/get/task', methods=['GET'])
def getTask():
    return jsonify({'tasks': tasks})


@app.route('/input/task', methods=['POST'])
def inputTask():
    new_task = request.get_json()

    petalLength = new_task['petalLength']
    petalWidth = new_task['petalWidth']
    sepalLength = new_task['sepalLength']
    sepalWidth = new_task['sepalWidth']

    newPetal = Petal(petalLength,petalWidth,sepalLength,sepalWidth)

    tasks.append(newPetal.__dict__)

    return jsonify({'message': 'success'})


@app.route('/update/task/<int:id>', methods=['PUT'])
def updateTask(id):
    new_task = request.get_json()

    petalLength = new_task['petalLength']
    petalWidth = new_task['petalWidth']
    sepalLength = new_task['sepalLength']
    sepalWidth = new_task['sepalWidth']

    newPetal = Petal(petalLength, petalWidth, sepalLength, sepalWidth)
    tasks[id] = newPetal.__dict__

    return jsonify({'message': 'success update'})


@app.route('/delete/task/<int:id>', methods=['DELETE'])
def deleteTask(id):
    del tasks[id]

    return jsonify({'message': 'success delete'})

app.run(debug=True)