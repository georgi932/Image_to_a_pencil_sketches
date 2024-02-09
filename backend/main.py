from flask import Flask
from routers.file_router import file_router

app = Flask(__name__)
app.register_blueprint(file_router)


if __name__ == '__main__':
    app.run(debug=True)
