from flask import Flask, jsonify, request 

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/soma', methods=['GET'])
def soma():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

    result = a + b
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True)