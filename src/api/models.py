from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    dni_nie = db.Column(db.String(50), unique=True, nullable=False)
    acquisition_channel = db.Column(db.String(50), nullable=True)
    bookings = db.relationship('Reserva', backref='cliente', lazy=True)
    visits = db.relationship('HistorialVisita', backref='cliente', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'phone': self.phone,
            'address': self.address,
            'dni_nie': self.dni_nie,
            'acquisition_channel': self.acquisition_channel,
        }

class Servicio(db.Model):
    __tablename__ = 'servicios'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duration in minutes
    bookings = db.relationship('Reserva', backref='servicio', lazy=True)
    visits = db.relationship('HistorialVisita', backref='servicio', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'duration': self.duration,
        }

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    servicio_id = db.Column(db.Integer, db.ForeignKey('servicios.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')
    transactions = db.relationship('Transaccion', backref='reserva', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'cliente_id': self.cliente_id,
            'servicio_id': self.servicio_id,
            'date': self.date.isoformat(),
            'time': self.time.strftime('%H:%M:%S'),
            'status': self.status,
        }

class Transaccion(db.Model):
    __tablename__ = 'transacciones'
    id = db.Column(db.Integer, primary_key=True)
    reserva_id = db.Column(db.Integer, db.ForeignKey('reservas.id'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    payment_status = db.Column(db.String(50), nullable=False, default='pending')
    amount_paid = db.Column(db.Float, nullable=False)
    stripe_session_id = db.Column(db.String(100), nullable=True)
    transaction_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def serialize(self):
        return {
            'id': self.id,
            'reserva_id': self.reserva_id,
            'cliente_id': self.cliente_id,
            'payment_status': self.payment_status,
            'amount_paid': self.amount_paid,
            'stripe_session_id': self.stripe_session_id,
            'transaction_date': self.transaction_date.isoformat(),
        }

class HistorialVisita(db.Model):
    __tablename__ = 'historial_visitas'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    servicio_id = db.Column(db.Integer, db.ForeignKey('servicios.id'), nullable=False)
    visit_date = db.Column(db.Date, nullable=False)
    additional_comments = db.Column(db.Text, nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'cliente_id': self.cliente_id,
            'servicio_id': self.servicio_id,
            'visit_date': self.visit_date.isoformat(),
            'additional_comments': self.additional_comments,
        }

# Ensure tables are created
def create_tables(app):
    with app.app_context():
        db.create_all()



# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return f'<User {self.email}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }