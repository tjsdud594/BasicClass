from flask import Flask, render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('myapp_req.html')


@app.route('/login', methods=['post'])
def login():

    return render_template('myapp_res.html')

if __name__ == '__main__':
    app.run(debug=True)