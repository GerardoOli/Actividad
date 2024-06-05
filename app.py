from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
    <head><title>Información Personal</title></head>
    <body style="font-family: Arial, sans-serif; background-color: #f0f8ff; text-align: center; padding: 20px;">
        <div style="background-color: #fff; padding: 20px; border-radius: 10px; display: inline-block;">
            <img src="https://img.freepik.com/vector-premium/icono-perfil-usuario-estilo-plano-ilustracion-vector-avatar-miembro-sobre-fondo-aislado-concepto-negocio-signo-permiso-humano_157943-15752.jpg" alt="Foto de Perfil" style="border-radius: 50%; width: 150px; height: 150px; margin-bottom: 20px;">
            <h3 style="color: #333;">Gerardo Olivares Aguilar</h3>
            <h3 style="color: #333;">Grado: 9 Grupo: B</h3>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
