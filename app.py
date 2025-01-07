from flask import Flask
from functions .data_retreiver import my_function
app = Flask(__name__)

##basic
@app.route('/')
def index():
    return 'Hello World'

##returns HTML (not best practice)
@app.route('/html')
def html():
    return '<h1>Here is a heading</h1>'


##slug
@app.route('/slug/<name>')
def slug(name):
    return '<h1>Hello {} </h1>'.format(name)


##returns data in dict/json form
@app.route('/data')
def data():
    data = {'First': 15, 'Second': 20, "Third": 25, "Fourth": 30, "Fifth": 35, "Sixth": 50}
    return data

##returns data in dict/json form
@app.route('/api')
def data_api():
    response = my_function()
    return response


## used to run later and prevent non main files from running
if __name__ == '__main__':  
   app.run()  