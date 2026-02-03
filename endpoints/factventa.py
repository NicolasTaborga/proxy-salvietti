from flask import request, jsonify
import requests

def facventa_endpoint(app):
    HEADERS = {"Accept": "application/json", "X-Empresa-Codigo": "1"}

    @app.route("/facventa")
    def facventa():
        fi = request.args.get("FechaInicio")
        ff = request.args.get("FechaFin")

        url = f"http://34.217.254.222/ReportServerProduccion/api/FacSalvietti/getFacVenta?FechaInicio={fi}&FechaFin={ff}"

        r = requests.post(url, auth=("alex", "123"), headers=HEADERS)
        return jsonify(r.json())
