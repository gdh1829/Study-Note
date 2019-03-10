from flask import Flask, render_template, Response, request
import requests
import hashlib
import redis

# init Flask
app = Flask(__name__, template_folder='./templates')
cache = redis.StrictRedis(host='redis', port='6379', db=0)
salt = "UNIQUE_SALT"
default_name = 'Dev Ko Blogs'

# route
@app.route('/')
def hello_world():
    return 'Hello Docker!\n1,2,3\n'

@app.route('/index', methods = ['GET', 'POST'])
def get_mainpage():
    name = default_name
    if request.method == 'POST':
        name = request.form['name']
    salted_name = salt + name
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest()
    return render_template('index.html', name=name, name_hash=name_hash)

@app.route('/dnmonster/<name>')
def get_identicon(name):
    image = cache.get(name)
    if image is None:
        print("Cache miss", flush=True)
        dnmonster = requests.get('http://dnmonster:8080/monster/' + name + '?size=30')
        image = dnmonster.content
        cache.set(name, image)
    return Response(image, mimetype='image/png')


# init Python web server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
