from flask import Flask, request
from flask_restful import Api, Resource
import requests
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

url_cliente = "http://localhost:5000/api/cliente"
url_producto = "http://localhost:5000/api/producto"

class Factura(Resource):
    def post(self):
        objRespuesta = {
            "id_cliente": 0,
            "nombre_cliente": "",
            "direccion_cliente": "",
            "total_venta": 0,
            "productos": []
        }

        json = request.get_json()
        id_cliente = json["id_cliente"]
        productos = json["productos"]

        cliente_response = requests.get(url_cliente + "/" + str(id_cliente))
        if cliente_response.status_code == 200:
            cliente_json = cliente_response.json()
            objRespuesta["id_cliente"] = cliente_json["id"]
            objRespuesta["nombre_cliente"] = cliente_json["razonSocial"]
            objRespuesta["direccion_cliente"] = cliente_json["direccion"]

            total_venta = 0
            for item in productos:
                producto_response = requests.get(url_producto + "/" + str(item["id_producto"]))
                if producto_response.status_code == 200:
                    producto_json = producto_response.json()
                    total_venta += producto_json["precio"] * item["cantidad"]
                    objRespuesta["productos"].append({
                        "id_producto": producto_json["id"],
                        "nombre": producto_json["nombre"],
                        "cantidad": item["cantidad"],
                        "precio": producto_json["precio"],
                        "total": producto_json["precio"] * item["cantidad"]
                    })
            objRespuesta["total_venta"] = total_venta
        else:
            return {"message": "Cliente no encontrado"}, 404

        return objRespuesta, 201

api.add_resource(Factura, "/api/boleta")

if __name__ == "__main__":
    app.run(debug=True, port=5001)


    