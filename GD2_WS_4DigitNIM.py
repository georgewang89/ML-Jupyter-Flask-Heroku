from flask import Flask,jsonify,request
from Model.Dataseed import tasks
from Model.Petal import Petal
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)


@app.route('/get/task', methods=['GET'])
def getTask():
    """
    Ini adalah Endpoint untuk mengambil seluruh data yang ada.
    ---
    tags:
        - Rest Controller
    parameter:
    responses:
        200:
            description: Success Get All Data
    """
    return jsonify({'tasks': tasks})


@app.route('/input/task', methods=['POST'])
def inputTask():
    """
    Ini Adalah Endpoint Untuk Menambahkan Data Task
    ---
    tags:
        - Rest Controller
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Petal
          required:
            - petalLength
            - petalWidth
            - sepalLength
            - sepalWidth
          properties:
            petalLength:
              type: int
              description: Please input with valid Sepal and Petal Length-Width.
              default: 0
            petalWidth:
              type: int
              description: Please input with valid Sepal and Petal Length-Width.
              default: 0
            sepalLength:
              type: int
              description: Please input with valid Sepal and Petal Length-Width.
              default: 0
            sepalWidth:
              type: int
              description: Please input with valid Sepal and Petal Length-Width.
              default: 0
    responses:
        200:
            description: Success Input
    """
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
    """
    Ini Adalah Endpoint Untuk Mengupdate Data Task
    ---
    tags:
        - Rest Controller
    parameters:
      - in: path
        name: id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          id: Product
          required:
            - petalLength
            - petalWidth
            - sepalLength
            - sepalWidth
          properties:
            petalLength:
              type: int
              description: Please input with valid Sepal and Petal Length-Width.
              default: 0
            petalWidth:
              type: int
              description: Please input with valid Sepal and Petal Length-Width.
              default: 0
            sepalLength:
              type: int
              description: Please input with valid Sepal and Petal Length-Width.
              default: 0
            sepalWidth:
              type: int
              description: Please input with valid Sepal and Petal Length-Width.
              default: 0
    responses:
        200:
            description: Success Update
    """
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
    """
    Ini Adalah Endpoint untuk menghapus data tertentu.
    ---
    tags:
        - Rest Controller
    parameters:
        - in: path
          name: id
          required: true
          type: integer

    responses:
        200:
            description: Success Delete
    """
    del tasks[id]

    return jsonify({'message': 'success delete'})

app.run(debug=True)