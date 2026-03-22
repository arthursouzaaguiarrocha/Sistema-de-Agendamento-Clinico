from flask import Flask
from app.routes.paciente_routes import paciente_bp

app = Flask(__name__)

app.register_blueprint(paciente_bp)

if __name__ == "__main__":
    app.run(debug=True)