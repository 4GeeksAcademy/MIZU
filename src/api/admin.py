import os
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import db, Cliente, Servicio, Reserva, Transaccion, HistorialVisita

class CustomModelView(ModelView):
    def __init__(self, model, session, **kwargs):
        super().__init__(model, session, **kwargs)

class ClienteModelView(CustomModelView):
    column_exclude_list = ['bookings', 'visits']
    form_excluded_columns = ['bookings', 'visits']
    column_searchable_list = ['full_name', 'email', 'phone', 'dni_nie']
    column_filters = ['acquisition_channel']

class ServicioModelView(CustomModelView):
    column_exclude_list = ['bookings', 'visits']
    form_excluded_columns = ['bookings', 'visits']

class ReservaModelView(CustomModelView):
    column_searchable_list = ['status', 'date', 'time']
    column_filters = ['status', 'date']

class TransaccionModelView(CustomModelView):
    column_searchable_list = ['payment_status', 'amount_paid', 'stripe_session_id']
    column_filters = ['payment_status', 'transaction_date']

class HistorialVisitaModelView(CustomModelView):
    column_searchable_list = ['visit_date', 'additional_comments']
    column_filters = ['visit_date']

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='Mizu Admin', template_mode='bootstrap3')

    # Add your models here
    admin.add_view(ClienteModelView(Cliente, db.session))
    admin.add_view(ServicioModelView(Servicio, db.session))
    admin.add_view(ReservaModelView(Reserva, db.session))
    admin.add_view(TransaccionModelView(Transaccion, db.session))
    admin.add_view(HistorialVisitaModelView(HistorialVisita, db.session))