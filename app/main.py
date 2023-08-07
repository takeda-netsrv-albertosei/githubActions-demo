from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv() #getting environment variables from .env

app = Flask(__name__)

@app.route('/<random_string>')
def return_backwards_string(random_string):
    return "".join(reversed(random_string))


@app.route('/get-mode')
def get_mode():
    return os.environ.get("MODE") #retrieves from .env

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


    