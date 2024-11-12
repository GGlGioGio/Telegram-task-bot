from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Task Tracker Bot!'

if __name__ == '__main__':
    app.run(debug=True)
