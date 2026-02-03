from flask import Flask
from endpoints.facventa import facventa_endpoint
from endpoints.facasistencia import facasistencia_endpoint
from endpoints.facvisita import facvisita_endpoint
from endpoints.facruta import facruta_endpoint
from endpoints.facpresupuesto import facpresupuesto_endpoint

app = Flask(__name__)

# Registrar Blueprints
app.register_blueprint(facventa_endpoint)
app.register_blueprint(facasistencia_endpoint)
app.register_blueprint(facvisita_endpoint)
app.register_blueprint(facruta_endpoint)
app.register_blueprint(facpresupuesto_endpoint)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
