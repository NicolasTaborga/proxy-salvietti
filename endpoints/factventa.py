from flask import Blueprint, request, jsonify
import requests

facventa_endpoint = Blueprint("facventa", __name__)

HEADERS = {"Accept": "application/json", "X-Empresa-Codigo": "1"}

@facventa_endpoint.route("/facventa")
def facventa():
    fi = request.args.get("FechaInicio")
    ff = request.args.get("FechaFin")
    url = f"http://34.217.254.222/ReportServerProduccion/api/FacSalvietti/getFacVenta?FechaInicio={fi}&FechaFin={ff}"
    r = requests.post(url, auth=("alex", "123"), headers=HEADERS)
    return jsonify(r.json())
