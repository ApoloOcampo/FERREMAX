## 1.API-CSharp (puerto:5000)
En Visual Studio (VS):

Existen dos controllers
- Cliente
- Producto

- Ejecutar desde CMD dentro de la carpeta .\API-Csharp\Ferremax\Ferremax.API el comando
- dotnet run -d Ferremax.API.csproj
  
## 2.API-Logistica (puerto:5002)
En Visual Studio (VS):
- despacho
- envio
- retiro

- Ejecutar desde CMD dentro de la carpeta .\API-Logistica\logistica\logistica.API el comando
- dotnet run -d logistica.API.csproj

## 3.API-Flask
apiFactura: Es para la creación de la factura.
guardarEstado: Es para guardar el estado del despacho.

- Ejecutar desde CMD dentro de la carpeta .\FERREMAX\API-Flask los comandos
- pip install -r requirements.txt

  EJECUTAR API apiFactura (puerto:5001)
- desde CMD en la ruta .\FERREMAX\API-Flask ejecutar
- python apiFactura.py

  EJECUTAR API guardarEstado (puerto:5003)
- desde CMD en la ruta .\FERREMAX\API-Flask ejecutar
- python guardarEstado.py


## FRONT
Página WEB
- Ejecutar desde CMD dentro de la carpeta .\FERREMAX\FRONT el comando
- code .
- y ejecutar con live server


          POST de prueba

"http://localhost:5000/api/cliente"
{
    "id":1,
    "razonSocial":"persona1",
    "rut":"1-1",
    "direccion":"av 1",
    "telefono":"+56982451238",
    "email":"persona1@gmail.com",
    "activo":true
}

{
    "id":2,
    "razonSocial":"persona2",
    "rut":"2-2",
    "direccion":"av 2",
    "telefono":"+56982451238",
    "email":"persona2@gmail.com",
    "activo":true
}

{
    "id":3,
    "razonSocial":"persona3",
    "rut":"3-3",
    "direccion":"av 3",
    "telefono":"+56982451238",
    "email":"persona3@gmail.com",
    "activo":false
}

{
    "id":4,
    "razonSocial":"persona4",
    "rut":"4-4",
    "direccion":"av 4",
    "telefono":"+56982451238",
    "email":"persona4@gmail.com",
    "activo":true
}


http://localhost:5000/api/producto

{
    "id":1,
    "nombre":"producto 1",
    "categoria":"herramientas",
    "precio":1000,
    "enStock": true
}

{
    "id":2,
    "nombre":"producto 2",
    "categoria":"herramientas",
    "precio":2000,
    "enStock": false
}

{
    "id":3,
    "nombre":"producto 3",
    "categoria":"herramientas",
    "precio":3000,
    "enStock": true
}

{
    "id":4,
    "nombre":"producto 4",
    "categoria":"herramientas",
    "precio":4000,
    "enStock": true
}


http://localhost:5002/api/despacho

{
    "id": 1,
    "tipo": "en preparación"
}

{
    "id": 2,
    "tipo": "en despacho"
}

{
    "id": 3,
    "tipo": "entregado"
}

{
    "id": 4,
    "tipo": "entregado"
}
