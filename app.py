from flask import Flask
from endpoints.facventa import facventa_endpoint
from endpoints.facasistencia import facasistencia_endpoint
from endpoints.facvisita import facvisita_endpoint
from endpoints.facruta import facruta_endpoint
from endpoints.facpresupuesto import facpresupuesto_endpoint

app = Flask(__name__)

# Registrar todos los endpoints
facventa_endpoint(app)
facasistencia_endpoint(app)
facvisita_endpoint(app)
facruta_endpoint(app)
facpresupuesto_endpoint(app) 

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
