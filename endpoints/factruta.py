from flask import Blueprint, request, jsonify
import requests

facruta_endpoint = Blueprint("facruta", __name__)

HEADERS = {"Accept": "application/json", "X-Empresa-Codigo": "1"}

@facruta_endpoint.route("/facruta")
def facruta():
    fi = request.args.get("FechaInicio")
    ff = request.args.get("FechaFin")
    url = f"http://34.217.254.222/ReportServerProduccion/api/FacSalvietti/getFacRuta?FechaInicio={fi}&FechaFin={ff}"
    r = requests.post(url, auth=("alex", "123"), headers=HEADERS)
    return jsonify(r.json())
