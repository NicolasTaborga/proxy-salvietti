from flask import request, jsonify
import requests

def facasistencia_endpoint(app):
    HEADERS = {"Accept": "application/json", "X-Empresa-Codigo": "1"}

    @app.route("/facasistencia")
    def facasistencia():
        fi = request.args.get("FechaInicio")
        ff = request.args.get("FechaFin")

        url = f"http://34.217.254.222/ReportServerProduccion/api/FacSalvietti/getFacAsistencia?FechaInicio={fi}&FechaFin={ff}"

        r = requests.post(url, auth=("alex", "123"), headers=HEADERS)
        return jsonify(r.json())
