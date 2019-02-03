from flask import Flask
from flask_restful import Resource, Api
from api.hello import Hello

app = Flask(__name__)
api = Api(app)



api.add_resource(Hello, '/hello')

api.add_resource(connect, '/obd/connectç')

if __name__ == '__main__':
    app.run(debug=True, port=2000)

