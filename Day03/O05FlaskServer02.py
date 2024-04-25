
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api =Api(app)

products = {
    'pepsi': {'type': '2 ltr bottle', 'price': 120, 'qty': 50},
    'coke': {'type' :'500 ml bottle', 'price': 45, 'qty': 200},
    'sprite':{'type': '300 ml can', 'price': 50, 'qry': 100}
}

class Products(Resource):

    def get(self, product):
        return {product: products[product]}

api.add_resource(Products, "/getproduct/<product>")

if __name__ == '__main__':
    app.run(debug=True)
