import click
from api.models import db, Cliente

"""
In this file, you can add as many commands as you want using the @app.cli.command decorator
Flask commands are useful to run cron jobs or tasks outside of the API but still in integration 
with your database, for example: Import the price of bitcoin every night at 12 am
"""
def setup_commands(app):
    
    """ 
    This is an example command "insert-test-users" that you can run from the command line
    by typing: $ flask insert-test-clients 5
    Note: 5 is the number of clients to add
    """
    @app.cli.command("insert-test-clients") # name of our command
    @click.argument("count") # argument of our command
    def insert_test_clients(count):
        print("Creating test clients")
        for x in range(1, int(count) + 1):
            client = Cliente(
                nombre_completo=f"Test Client {x}",
                telefono=f"123456789{x}",
                direccion=f"Address {x}",
                dni_nie=f"DNI{x}",
                canal_adquisicion="test_channel"
            )
            db.session.add(client)
            db.session.commit()
            print("Client: ", client.nombre_completo, " created.")

        print("All test clients created")

    @app.cli.command("insert-test-data")
    def insert_test_data():
        print("Inserting test data...")
        # You can add logic to insert test data for other models here
        print("Test data inserted.")