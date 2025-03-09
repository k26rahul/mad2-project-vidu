from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return 'hello from app.py, in wsl'


app.run(debug=True)
