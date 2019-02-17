from flask import Flask
# init Flask
app = Flask(__name__)

# route
@app.route('/')
def hello_world():
    return 'Hello Docker!\n1,2,3\n'

# init Python web server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
