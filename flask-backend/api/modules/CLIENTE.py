import functools
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from model.CLIENTE import (
    get_CLIENTE,
    get_CLIENTES,
    create_cliente,
    get_cliente_by_name,
    update_cliente,
    delete_cliente,
)

bp = Blueprint('CLIENTE', __name__, url_prefix='/CLIENTE')
CORS(bp)

@bp.route('/', methods=['GET'])
def list():
    retorno = get_CLIENTE()
    return jsonify(retorno)

@bp.route('/<int:idCliente>', methods=['GET'])
def get(idCliente):
    return jsonify(get_CLIENTES(idCliente))

@bp.route('/by_name/<Nombre>', methods=['GET'])
def get_by_name(Nombre):
    return jsonify(get_cliente_by_name(Nombre))

@bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    idCliente=data['idCliente']
    Nombre = data['Nombre']
    Apellido = data['Apellido']
    Telefono = data['Telefono']
    Direccion = data['Direccion']
    Nombre_Mascota = data['Nombre_Mascota']
    return jsonify(create_cliente(idCliente, Nombre, Apellido,Telefono, Direccion, Nombre_Mascota))

@bp.route('/<int:idCliente>', methods=['PUT'])
def update(idCliente):
    data = request.get_json()
    Nombre = data['Nombre']
    Apellido = data['Apellido']
    Telefono = data['Telefono']
    Direccion = data['Direccion']
    return jsonify(update_cliente(Nombre, Apellido,Telefono, Direccion,idCliente))

@bp.route('/<int:idCliente>', methods=['DELETE'])
def delete(idCliente):
    return jsonify(delete_cliente(idCliente))
