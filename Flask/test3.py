from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/getInfo', methods=['POST'])
def task():
    
    data = request.get_json("glosarry")
    print(data.get("glossary").get("GlossDiv"))
    return "Hello"


if __name__ == '__main__':
   app.run(host = "127.0.0.1", port = 4000, debug = True)