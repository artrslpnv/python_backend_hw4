from flask import Flask
from dotenv import dotenv_values
from flask import jsonify

from flask import request

app = Flask(__name__)

def get_port()-> int:
    config = dotenv_values(".env")
    if "PORT" in config:
        return config["PORT"]
    return 5000




from controllers import operation

@app.route("/sum")
def runner():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'sum': operation(a, b)})



@app.route("/author")
def author():
    author = {
        "name": "Artur",
        "course": 4,
        "age": 22,
    }
    return jsonify(author)




@app.route("/")
def server_info() -> str:
    return "My server"


if __name__ == "__main__":
    app.run(debug=True, port=get_port())
