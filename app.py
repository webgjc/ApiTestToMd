from flask import Flask
from apitest.main import api
from view.main import view

app = Flask(__name__)

app.register_blueprint(api)
app.register_blueprint(view)

if __name__ == "__main__":
    app.run("0.0.0.0",80,debug=True)