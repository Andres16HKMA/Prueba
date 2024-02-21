import json
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from azure.communication.email import EmailClient
import cuadros3x3
app = Flask(__name__)
a=cuadros3x3.Cuadros()
load_dotenv()
with open("ejemploTablero.json") as sudoku:
    tablero = json.load(sudoku)
    
    

@app.route('/validar', methods=['POST'])
def validarCuadro():
    
    if a.validador(tablero):
        # Si el número es válido, enviar el correo electrónico con el tablero
        return jsonify({'message': 'no hay error'}), 200
    else:
        return jsonify({'message': 'El dato no puede ser ubicado, cambie de posición'}), 400
    

if __name__ == '__main__':
    # Utiliza Waitress como servidor en lugar del servidor de desarrollo de Flask para producción
    from waitress import serve

    print("Server running ")
    serve(app, host='0.0.0.0', port=5000)

