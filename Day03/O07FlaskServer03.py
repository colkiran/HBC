import json

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

players = {
    'sachin' : {'name': 'Sachin Tendulkar', 'age': 36, 'odi': 18500, 'test': 16700, 't20': 1800 },
    'ponting': {'name': 'Ricky Ponting', 'age':32, 'odi': 12450, 'test': 11200, 't20': '2100'},
    'lara' : {'name': 'Brain Lara', 'age': 39, 'odi': 11480, 'test': 12900, 't20': 1200}
}
class Players(Resource):

    def get(self, player):
        return {player: players[player]}

    def put(self, player):
        players[player]['team'] = request.form['team']
        return {player: players[player]}

    def patch(self, player):
        data1 = request.json
        data = json.loads(data1)
        players[player][list(data.keys())[0]] = data[list(data.keys())[0]]
        return players[player]

    def post(self, player):
        data1  = request.json
        data = json.loads(data1)
        players[player] = data
        return players

    def delete(self, player):
        if player in players:
            del players[player]
            return {'result': players}
        else:
            return {'KeyError': "Invalid key, Please enter a valid key...."}


api.add_resource(Players, "/getplayers/<string:player>")

if __name__ == '__main__':
    app.run(debug=True, use_reloader = True)
