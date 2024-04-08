from flask import Flask
from backend.routers.file_router import file_router

app = Flask(__name__)
app.register_blueprint(file_router, url_prefix='/')


if __name__ == '__main__':
    app.run()

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
