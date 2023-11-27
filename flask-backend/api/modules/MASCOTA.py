import functools
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from model.MASCOTA import (
    get_MASCOTA,
    get_mascotas,
    create_mascota,
    update_mascota,
    delete_mascota,
)

bp = Blueprint('MASCOTA', __name__, url_prefix='/MASCOTA')
CORS(bp)

@bp.route('/', methods=['GET'])
def list():
    retorno = get_MASCOTA()
    return jsonify(retorno)

@bp.route('/<int:idMASCOTA>', methods=['GET'])
def get(idMASCOTA):
    return jsonify(get_mascotas(idMASCOTA))

@bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    Nombre_Mascota = data['Nombre_Mascota']
    Especie=data['Especie']
    Genero=data['Genero']
    Raza=data['Raza']
    Tipo_de_Sangre=data['Tipo_de_Sangre']
    Edad = data['Edad']
    Estado = data['Estado']
    return jsonify(create_mascota(Nombre_Mascota, Especie, Genero, Raza,Tipo_de_Sangre,Edad, Estado))

@bp.route('/<int:idMASCOTA>', methods=['PUT'])
def update(idMASCOTA):
    data = request.get_json()
    Nombre_Mascota = data['Nombre_Mascota']
    Edad = data['Edad']
    Estado = data['Estado']
    return jsonify(update_mascota(Nombre_Mascota,Edad, Estado, idMASCOTA))

@bp.route('/<int:idMASCOTA>', methods=['DELETE'])
def delete(idMASCOTA):
    return jsonify(delete_mascota(idMASCOTA))
