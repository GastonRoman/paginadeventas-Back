#  Importar las herramientas
# Acceder a las herramientas para crear la app web
from itertools import product
from flask import Flask, request, jsonify

# Para manipular la DB
from flask_sqlalchemy import SQLAlchemy

# Módulo cors es para que me permita acceder desde el frontend al backend
from flask_cors import CORS

# Crear la app
app = Flask(__name__)

# permite acceder desde el frontend al backend
CORS(app)

# Configurar a la app la DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://usuario:contraseña@localhost:3306/nombre_de_la_base_de_datos'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost:3306/paginadeventas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crear un objeto db, para informar a la app que se trabajará con sqlalchemy
db = SQLAlchemy(app)


# Definir la tabla 
class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto=db.Column(db.String(50))
    imagen=db.Column(db.String(400))
    descripcion=db.Column(db.String(400))
    categoria=db.Column(db.String(50))
    precio=db.Column(db.Integer)
    
    

def __init__(self,producto,imagen,descripcion,categoria,precio):   #crea el  constructor de la clase
        self.producto=producto   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.imagen=imagen 
        self.descripcion=descripcion
        self.categoria=categoria
        self.precio=precio
        
           
# 8. Crear la tabla al ejecutarse la app
with app.app_context():
    db.create_all()

# Crear ruta de acceso
# / es la ruta de inicio
@app.route("/")
def index():
    return f'App Web para registrar productos'

# Crear un registro en la tabla Productos
@app.route("/registro", methods=['POST']) 
def registro():
    # {"nombre": "Felipe", ...} -> input tiene el atributo name="nombre"
    producto = request.json["producto"]
    imagen=request.json['imagen']
    descripcion=request.json['descripcion']
    categoria=request.json['categoria']
    precio=request.json['precio']
    
    

    nuevo_registro = Productos(producto=producto,imagen=imagen,descripcion=descripcion,categoria=categoria,precio=precio)
    db.session.add(nuevo_registro)
    db.session.commit()

    return "Solicitud de post recibida"


 # Retornar todos los registros en un Json
@app.route("/productos",  methods=['GET'])
def productos():
    # Consultar en la tabla todos los registros
    # all_registros -> lista de objetos
    all_registros = Productos.query.all()

    # Lista de diccionarios
    data_serializada = []
    
    for objeto in all_registros:
        data_serializada.append({"id":objeto.id, "producto":objeto.producto, "imagen":objeto.imagen, "descripcion":objeto.descripcion,"categoria":objeto.categoria, "precio":objeto.precio})

    return jsonify(data_serializada)
   

# # Modificar un registro
# @app.route('/update/<id>', methods=['PUT'])
# def update(id):
#     # Buscar el registro a modificar en la tabla por su id
#     productos = Productos.query.get(id)

#     # {"nombre": "Felipe"} -> input tiene el atributo name="nombre"
#     producto= request.json["producto"]
#     imagen=request.json['imagen']
#     descripcion=request.json['descripcion']
#     precio=request.json['precio']
    
    

#     productos.producto=producto
#     productos.imagen=imagen
#     productos.descripcion=descripcion
#     productos.precio=precio
    
    
#     db.session.commit()

#     data_serializada = [{"id":productos.id, "producto":productos.producto, "imagen":productos.imagen, "descripcion":productos.descripcion, "precio":productos.precio}]
    
#     return jsonify(data_serializada)

# Ruta para actualizar un producto por su ID
@app.route('/update/<int:id>', methods=['PUT'])
def update_producto(id):
    try:
        # Obtener el producto por su ID
        producto = Productos.query.get(id)

        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404

        # Actualizar los atributos del producto con los datos recibidos
        data = request.json
        producto.producto = data.get("producto", producto.producto)
        producto.imagen = data.get("imagen", producto.imagen)
        producto.descripcion = data.get("descripcion", producto.descripcion)
        producto.categoria = data.get("categoria", producto.categoria)
        producto.precio = data.get("precio", producto.precio)

        # Guardar los cambios en la base de datos
        db.session.commit()

        # Preparar la respuesta JSON con los datos actualizados
        data_serializada = {
            "id": producto.id,
            "producto": producto.producto,
            "imagen": producto.imagen,
            "descripcion": producto.descripcion,
            "categoria": producto.categoria,
            "precio": producto.precio
        }
        
        return jsonify(data_serializada), 200
    
    except Exception as e:
        # Manejar cualquier error que pueda ocurrir
        return jsonify({"error": str(e)}), 500

   
@app.route('/borrar/<id>', methods=['DELETE'])
def borrar(id):
    
    # Se busca a la productos por id en la DB
    productos = Productos.query.get(id)

    # Se elimina de la DB
    db.session.delete(productos)
    db.session.commit()

    data_serializada = [{"id":productos.id, "producto":productos.producto, "imagen":productos.imagen, "descripcion":productos.descripcion,"categoria":productos.categoria, "precio":productos.precio}]

    return jsonify(data_serializada)


if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False)
