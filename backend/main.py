from flask import Flask
from services.file_service import create_folders
import uvicorn

app = Flask(__name__)


@app.route('/')
def home():
    return {"Welcome": "Welcome to my Flask web app!"}


create_folders()


# if __name__ == '__main__':
#     app.run(debug=True)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
