from flask import Blueprint, request, jsonify
from app.services.paciente_service import listar_pacientes, criar_paciente

paciente_bp = Blueprint('paciente', __name__, url_prefix='/pacientes')

@paciente_bp.route('/', methods=['GET'])
def get_pacientes():
    return jsonify(listar_pacientes())

@paciente_bp.route('/', methods=['POST'])
def add_paciente():
    data = request.json
    paciente = criar_paciente(data)
    return jsonify(paciente)