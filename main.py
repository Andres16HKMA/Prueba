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
def validar_numero():
    
    if a.validador(tablero):
        # Si el número es válido, enviar el correo electrónico con el tablero
        return jsonify({'message': 'no hay error'}), 200
    else:
        return jsonify({'message': 'El dato no puede ser ubicado, cambie de posición'}), 400
