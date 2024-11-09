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

class ServicioModelView(CustomModelView):
    column_exclude_list = ['bookings', 'visits']
    form_excluded_columns = ['bookings', 'visits']

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='Mizu Admin', template_mode='bootstrap3')

    # Add your models here
    admin.add_view(ClienteModelView(Cliente, db.session))
    admin.add_view(ServicioModelView(Servicio, db.session))
    admin.add_view(ModelView(Reserva, db.session))
    admin.add_view(ModelView(Transaccion, db.session))
    admin.add_view(ModelView(HistorialVisita, db.session))