from flask import Flask
from const_data import obj
import json

app = Flask(__name__)

@app.route('/')
def home():
    data = json.dumps(obj, ensure_ascii=False)
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
