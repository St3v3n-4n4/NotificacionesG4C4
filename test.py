from flask import Flask
 
#Creamos objeto Flask
app = Flask(__name__)
 
#Creamos nuestro primer servicio web
@app.route('/test', methods=['GET'])
def test():
    return "hello world"
 
@app.route('/saludar/<string:name>', methods=['GET'])
def saludar(name: str):
    return "hola " + name
 
#Ejecutamos el servidor
if __name__ == '__main__':
    app.run()