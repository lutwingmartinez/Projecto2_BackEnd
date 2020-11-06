from flask import Flask, jsonify, request
from flask import json
from flask_cors import CORS
from Usuarios import Usuario #importa el paquete(carpeta y archivo)

app = Flask(__name__)
CORS(app)
Registrados = []
Registrados.append(Usuario("Usuario", "Maestro","admin", "admin"))

@app.route('/')
def principal():
    return jsonify({"mensaje":"Aqui va el contenido"})

@app.route('/registro') #este es un get por defecto
def registro_Usuarios():
    global Registrados
    Individuales = []
    for Registrado in Registrados:
        Individual = {
            'nombre':Registrado.getNombre(),
            'apellido': Registrado.getApellido(),
            'userName': Registrado.getUserName(),
            'contrasena': Registrado.getContrasena()
        }
        Individuales.append(Individual)
    return jsonify(Individuales)

@app.route('/registro/', methods=['POST'])
def agregarRegistro():
    global Registrados
    existe = False

    for Registrado in Registrados:
        if Registrado.getUserName() == request.json['userName']:
            existe = True
            break

    if existe == True:
        return jsonify({"mensaje": "User already registered"})

    else:
        nuevo = Usuario(request.json['nombre'], request.json['apellido'], request.json['userName'], request.json['contrasena'])
        Registrados.append(nuevo)
        return jsonify({"mensaje":"Usuario agregado"})

@app.route('/registro/<string:userName>', methods=['GET'])
def obtenerUsuario(userName):
    global Registrados
    Individuales = []
    for Registrado in Registrados:
        if Registrado.getUserName() == userName:        
            Individuales = {
                'nombre':Registrado.getNombre(),
                'apellido': Registrado.getApellido(),
                'userName': Registrado.getUserName(),
                'contrasena': Registrado.getContrasena()
            }
            break       
    
    return jsonify(Individuales)

@app.route('/registro/<string:userName>', methods=['PUT'])
def modificarUsuario(userName):
    global Registrados
    for indice in range(len(Registrados)):
        if Registrados[indice].getUserName() == userName:
            Registrados[indice].setNombre(request.json['nombre']),
            Registrados[indice].setApellido(request.json['apellido']),
            Registrados[indice].setUserName(request.json['userName']),
            Registrados[indice].setContrasena(request.json['contrasena']) 
            break
    return jsonify({"mensaje":"Usuario modificado"})

@app.route('/registro/<string:userName>', methods=['DELETE'])
def eliminarUsuario(userName):   
    global Registrados
    for indice in range(len(Registrados)):
        if Registrados[indice].getUserName() == userName:
            del Registrados[indice]
            break
    return jsonify({"mensaje":"Usuario eliminado"})

#aqui se finalizan las atribuciones que podra hacer el usuario maestro

#aqui empieza el inicio de sesion
@app.route('/inicio_sesion', methods = ['POST']) #el post deja agregar nuevos usuarios
def inicio_sesion():
    global Registrados
    Individuales = []
    userName = request.json['userName']
    contrasena = request.json['contrasena']
    for registrado in Registrados:

        if userName == Registrados[0].getUserName() and contrasena == Registrados[0].getContrasena():
            Individuales = {
                'mensaje': 'bienvenido admin',
                'reason': registrado.getUserName()
            }
            break
        elif userName == registrado.getUserName() and contrasena == registrado.getContrasena():
            Individuales = {
                'mensaje': 'bienvenido',
                'reason': registrado.getUserName()
            }

        elif userName == registrado.getUserName() and contrasena != registrado.getContrasena():
            Individuales = {
                'mensaje': 'fallaste',
                'reason': 'Tu contrasena es invalida'
            }
            

        elif userName != registrado.getUserName() and contrasena != registrado.getContrasena():
            Individuales = {
                'mensaje': 'fallaste',
                'reason': 'Tu usuario no existe'
            }
            
        
        else:
            Individuales = {
                'mensaje': 'fallaste',
                'reason': 'Aun no te has registrado'
            }

    return jsonify(Individuales)

#aqui acaba el inicio de sesion

if __name__ ==  '__main__':
    app.run(debug=True)