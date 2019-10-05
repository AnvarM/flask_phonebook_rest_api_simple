from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route('/')
def test():
    return "Test flask app"

app.run(port=5000)

