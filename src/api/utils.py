from flask import jsonify, url_for

class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

def generate_sitemap(app):
    unique_endpoints = set()
    for rule in app.url_map.iter_rules():
        if has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            if url != "/" and "/admin/" not in url:
                unique_endpoints.add(url)

    links_html = "".join(["<li style='padding: 10px 0 5px 0;'><a style='text-decoration: none; color: #004e54; text-transform: uppercase;' href='" + y + "' onmouseover='this.style.color=\"darkred\"' onmouseout='this.style.color=\"#004e54\"' onclick='this.style.color=\"blue\"'>" + y + '</a></li>' for y in unique_endpoints])
    api_name = "Mizu API"
    additional_data_html = """
        <h2 style="margin: 20px 0px 10px 0px; font-size:40px;">ENDPOINTS REQUESTS GUIDE</h2>
        <div style="text-align: left; padding: 40px; margin: 20px 100px; background-color: #333; border-radius: 10px; color: white;">
            <p><strong>CREATE CLIENTE:</strong></p>
            <p><strong>method: POST</strong></p>
            <p><strong>path request:</strong> /clientes</p>
            <pre style="background-color: #f5f5f5; padding: 10px; border-radius: 5px; overflow: auto; color: black;">
                    {
                        "nombre_completo": "Nombre Completo",
                        "telefono": "123456789",
                        "direccion": "Calle Ejemplo, 123",
                        "dni_nie": "12345678X",
                        "canal_adquisicion": "online"
                    }
            </pre>

            <p><strong>CREATE SERVICIO:</strong></p>
            <p><strong>method: POST</strong></p>
            <p><strong>path request:</strong> /servicios</p>
            <pre style="background-color: #f5f5f5; padding: 10px; border-radius: 5px; overflow: auto; color: black;">
                    {
                        "nombre": "Masaje Relajante",
                        "descripcion": "Un masaje relajante para reducir el estrés.",
                        "precio": 50.0,
                        "duracion": 60
                    }
            </pre>

            <p><strong>CREATE RESERVA:</strong></p>
            <p><strong>method: POST</strong></p>
            <p><strong>path request:</strong> /reservas</p>
            <pre style="background-color: #f5f5f5; padding: 10px; border-radius: 5px; overflow: auto; color: black;">
                    {
                        "id_cliente": 1,
                        "id_servicio": 2,
                        "fecha": "2024-11-15",
                        "hora": "14:00:00",
                        "estado": "pendiente"
                    }
            </pre>

            <p><strong>CREATE TRANSACCION:</strong></p>
            <p><strong>method: POST</strong></p>
            <p><strong>path request:</strong> /transacciones</p>
            <pre style="background-color: #f5f5f5; padding: 10px; border-radius: 5px; overflow: auto; color: black;">
                    {
                        "id_reserva": 1,
                        "id_cliente": 1,
                        "estado_pago": "completado",
                        "monto_pagado": 50.0,
                        "id_sesion_pago_stripe": "cs_test_a1b2c3d4e5"
                    }
            </pre>
        </div>
    """
    return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{api_name}</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@700&family=Montserrat&family=Pixelify+Sans&display=swap" rel="stylesheet">
        </head>
        <body style="background-color: white; color: black; text-align: center; font-family: 'Montserrat', arial;">
        <div style="text-align: center;">
        <div style="position: fixed; bottom: 0; right: 0; margin: 40px;">
                <button style="font-family: 'Barlow', sans-serif; border-radius: 40px;background-color: #004e54; padding: 20px; box-shadow: 0px 0px 10px 0px white; transition: all 0.3s ease;"
                    onmouseover="this.style.backgroundColor='darkred'; this.style.boxShadow='0px 0px 20px 0px white';"
                    onmouseout="this.style.backgroundColor='#004e54'; this.style.boxShadow='0px 0px 10px 0px white';">
                    <a style="text-decoration: none; font-size: 20px; color: white;" href="/admin">ADMIN MODE</a>
                </button>
         </div>
        <h1>Welcome to {api_name}</h1>
          <img style="max-height : 400px; margin: 0px 0px 50px 0px;" src="https://yourdomain.com/mizu_logo.jpeg" />
         <p style="font-size:25px">API HOST <script>document.write('<input style="padding: 10px; margin-left: 20px; width: 300px" type="text" value="'+window.location.href+'" />');</script></p>
        <h2 style="margin: 50px 0px 10px 0px; font-size:60px;">ENDPOINTS</h2>
        <div>
        <ul style="text-align: center; font-size: 25px; list-style-type: none; padding-right:30px; margin-bottom: 150px;">{links_html}</ul>
        {additional_data_html}
        </div>
        </body>
        </html>
        """
