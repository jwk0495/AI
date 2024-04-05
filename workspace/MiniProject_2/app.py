from flask import Flask, request, jsonify
app = Flask(__name__)

jsonList = dict()

@app.route('/test', methods = ['POST','GET'])
def test():
    if request.method == 'POST':
        username = request.args.get('username')
        json = request.get_json()
        jsonList[username] = json
        print(jsonList)
        return jsonify(jsonList)

    return 'Hello World!!'
