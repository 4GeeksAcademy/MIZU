from flask import request, jsonify, Blueprint
from flask_cors import CORS
from api.models import db, Cliente, Servicio, Reserva, Transaccion, HistorialVisita
from api.utils import APIException

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

# Endpoint to get all clients
@api.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify([cliente.serialize() for cliente in clientes]), 200

# Endpoint to create a new client
@api.route('/clientes', methods=['POST'])
def add_cliente():
    data = request.get_json()
    try:
        nuevo_cliente = Cliente(
            nombre_completo=data.get('nombre_completo'),
            telefono=data.get('telefono'),
            direccion=data.get('direccion'),
            dni_nie=data.get('dni_nie'),
            canal_adquisicion=data.get('canal_adquisicion')
        )
        db.session.add(nuevo_cliente)
        db.session.commit()
        return jsonify(nuevo_cliente.serialize()), 201
    except Exception as e:
        db.session.rollback()
        raise APIException(f"Error al crear cliente: {str(e)}")

# Endpoint to get all services
@api.route('/servicios', methods=['GET'])
def get_servicios():
    servicios = Servicio.query.all()
    return jsonify([servicio.serialize() for servicio in servicios]), 200

# Endpoint to create a new reservation
@api.route('/reservas', methods=['POST'])
def add_reserva():
    data = request.get_json()
    try:
        nueva_reserva = Reserva(
            id_cliente=data.get('id_cliente'),
            id_servicio=data.get('id_servicio'),
            fecha=data.get('fecha'),
            hora=data.get('hora'),
            estado='pendiente'
        )
        db.session.add(nueva_reserva)
        db.session.commit()
        return jsonify(nueva_reserva.serialize()), 201
    except Exception as e:
        db.session.rollback()
        raise APIException(f"Error al crear reserva: {str(e)}")

# Endpoint to get all reservations
@api.route('/reservas', methods=['GET'])
def get_reservas():
    reservas = Reserva.query.all()
    return jsonify([reserva.serialize() for reserva in reservas]), 200

# Endpoint to update a transaction status via Stripe webhook
@api.route('/transacciones/<int:id_transaccion>', methods=['PATCH'])
def update_transaccion(id_transaccion):
    data = request.get_json()
    transaccion = Transaccion.query.get(id_transaccion)
    if not transaccion:
        raise APIException('Transaccion no encontrada', status_code=404)

    try:
        transaccion.estado_pago = data.get('estado_pago', transaccion.estado_pago)
        db.session.commit()
        return jsonify(transaccion.serialize()), 200
    except Exception as e:
        db.session.rollback()
        raise APIException(f"Error al actualizar transaccion: {str(e)}")

# Endpoint to add a visit to the history
@api.route('/historial_visitas', methods=['POST'])
def add_historial_visita():
    data = request.get_json()
    try:
        nueva_visita = HistorialVisita(
            id_cliente=data.get('id_cliente'),
            id_servicio=data.get('id_servicio'),
            fecha_visita=data.get('fecha_visita'),
            comentarios_adicionales=data.get('comentarios_adicionales')
        )
        db.session.add(nueva_visita)
        db.session.commit()
        return jsonify(nueva_visita.serialize()), 201
    except Exception as e:
        db.session.rollback()
        raise APIException(f"Error al crear historial de visita: {str(e)}")

# Endpoint to get all visits from the history
@api.route('/historial_visitas', methods=['GET'])
def get_historial_visitas():
    visitas = HistorialVisita.query.all()
    return jsonify([visita.serialize() for visita in visitas]), 200
