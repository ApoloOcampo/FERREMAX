from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import requests

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Simulación de base de datos
facturas_db = {}

class Factura(Resource):
    def get(self, factura_id=None):
        if factura_id is None:
            return jsonify(list(facturas_db.values()))  # Devolver todas las facturas
        factura = facturas_db.get(factura_id)
        if factura:
            return jsonify(factura)
        return {"message": "Factura no encontrada"}, 404

# Endpoints de APIs de cliente y producto
url_cliente = "http://localhost:5000/api/cliente"
url_producto = "http://localhost:5000/api/producto"

class Factura(Resource):
    def get(self, factura_id=None):
        if factura_id is None:
            return jsonify(facturas_db)
        factura = facturas_db.get(factura_id)
        if factura:
            return jsonify(factura)
        return {"message": "Factura no encontrada"}, 404

    def post(self):
        json = request.get_json()
        id_cliente = json["id_cliente"]
        id_producto = json["id_producto"]

        cliente_response = requests.get(url_cliente + "/" + str(id_cliente))
        producto_response = requests.get(url_producto + "/" + str(id_producto))

        if cliente_response.status_code == 200 and producto_response.status_code == 200:
            cliente_json = cliente_response.json()
            producto_json = producto_response.json()

            factura_id = len(facturas_db) + 1
            objRespuesta = {
                "id": factura_id,
                "id_producto": producto_json["id"],
                "precio": producto_json["precio"],
                "cantidad": json["cantidad"],
                "total_venta": producto_json["precio"] * int(json["cantidad"]),
                "id_cliente": cliente_json["id"],
                "nombre_cliente": cliente_json["razonSocial"],
                "direccion_cliente": cliente_json["direccion"]
            }

            facturas_db[factura_id] = objRespuesta
            return objRespuesta, 201
        return {"message": "Error en la consulta de cliente o producto"}, 400

    def put(self, factura_id):
        if factura_id not in facturas_db:
            return {"message": "Factura no encontrada"}, 404

        json = request.get_json()
        factura = facturas_db[factura_id]

        if "id_cliente" in json:
            id_cliente = json["id_cliente"]
            cliente_response = requests.get(url_cliente + "/" + str(id_cliente))
            if cliente_response.status_code == 200:
                cliente_json = cliente_response.json()
                factura["id_cliente"] = cliente_json["id"]
                factura["nombre_cliente"] = cliente_json["razonSocial"]
                factura["direccion_cliente"] = cliente_json["direccion"]
            else:
                return {"message": "Error en la consulta del cliente"}, 400

        if "id_producto" in json:
            id_producto = json["id_producto"]
            producto_response = requests.get(url_producto + "/" + str(id_producto))
            if producto_response.status_code == 200:
                producto_json = producto_response.json()
                factura["id_producto"] = producto_json["id"]
                factura["precio"] = producto_json["precio"]
            else:
                return {"message": "Error en la consulta del producto"}, 400

        if "cantidad" in json:
            factura["cantidad"] = json["cantidad"]
            factura["total_venta"] = factura["precio"] * int(json["cantidad"])

        facturas_db[factura_id] = factura
        return factura

    def delete(self, factura_id):
        if factura_id in facturas_db:
            del facturas_db[factura_id]
            return {"message": "Factura eliminada"}
        return {"message": "Factura no encontrada"}, 404

api.add_resource(Factura, "/api/boleta", "/api/boleta/<int:factura_id>")

@app.route('/obtener_datos', methods=['GET'])
def obtener_datos():
    response = jsonify(list(facturas_db.values()))
    response.headers.add('Access-Control-Allow-Origin', '*')  # Permitir el acceso a la API desde cualquier origen
    return response



if __name__ == '__main__':
    app.run(debug=True, port=5001)