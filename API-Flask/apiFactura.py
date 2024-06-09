from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
import requests

app = Flask(__name__)
api = Api(app)

# Permitir CORS para todas las rutas
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Simulación de base de datos
facturas_db = {}

url_cliente = "http://localhost:5000/api/cliente"
url_producto = "http://localhost:5000/api/producto"

class Factura(Resource):
    def get(self, factura_id=None):
        if factura_id is None:
            return jsonify(list(facturas_db.values()))  # Devolver todas las facturas
        factura = facturas_db.get(factura_id)
        if factura:
            return jsonify(factura)
        return {"message": "Factura no encontrada"}, 404

    def post(self):
        json = request.get_json()
        id_cliente = json["id_cliente"]
        productos = json["productos"]

        cliente_response = requests.get(url_cliente + "/" + str(id_cliente))
        if cliente_response.status_code != 200:
            return {"message": "Error en la consulta de cliente"}, 400

        cliente_json = cliente_response.json()
        factura_id = len(facturas_db) + 1
        total_venta = 0
        detalles = []

        for prod in productos:
            producto_response = requests.get(url_producto + "/" + str(prod["id"]))
            if producto_response.status_code != 200:
                return {"message": f"Error en la consulta del producto {prod['id']}"}, 400

            producto_json = producto_response.json()
            detalle = {
                "id_producto": producto_json["id"],
                "nombre_producto": producto_json["nombre"],
                "precio": producto_json["precio"],
                "cantidad": prod["cantidad"],
                "total": producto_json["precio"] * int(prod["cantidad"])
            }
            total_venta += detalle["total"]
            detalles.append(detalle)

        objRespuesta = {
            "id": factura_id,
            "id_cliente": cliente_json["id"],
            "nombre_cliente": cliente_json["razonSocial"],
            "direccion_cliente": cliente_json["direccion"],
            "total_venta": total_venta,
            "detalles": detalles
        }

        facturas_db[factura_id] = objRespuesta
        return objRespuesta, 201

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

        if "productos" in json:
            productos = json["productos"]
            total_venta = 0
            detalles = []

            for prod in productos:
                producto_response = requests.get(url_producto + "/" + str(prod["id"]))
                if producto_response.status_code != 200:
                    return {"message": f"Error en la consulta del producto {prod['id']}"}, 400

                producto_json = producto_response.json()
                detalle = {
                    "id_producto": producto_json["id"],
                    "nombre_producto": producto_json["nombre"],
                    "precio": producto_json["precio"],
                    "cantidad": prod["cantidad"],
                    "total": producto_json["precio"] * int(prod["cantidad"])
                }
                total_venta += detalle["total"]
                detalles.append(detalle)

            factura["detalles"] = detalles
            factura["total_venta"] = total_venta

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
