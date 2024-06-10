from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import requests

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Simulated database
boletas = []
despachos = []
estados = []

# Endpoint para obtener boletas
@app.route('/api/boleta', methods=['GET'])
def get_boletas():
    return jsonify(boletas)

# Endpoint para obtener despachos
@app.route('/api/despacho', methods=['GET'])
def get_despachos():
    return jsonify(despachos)

# Endpoint para guardar el estado de envío
@app.route('/api/guardarEstado', methods=['POST'])
def guardar_estado():
    data = request.get_json()
    for item in data:
        estado = next((estado for estado in estados if estado['id'] == item['id']), None)
        if estado:
            estado['estado'] = item['estado']
        else:
            estados.append(item)
    return jsonify({'message': 'Estados guardados correctamente'})

# Run the Flask app
if __name__ == '__main__':
    # Example data
    app.run(debug=True, port=5003)