from flask import Blueprint, request, jsonify
import requests

facvisita_endpoint = Blueprint("facvisita", __name__)

HEADERS = {"Accept": "application/json", "X-Empresa-Codigo": "1"}

@facvisita_endpoint.route("/facvisita")
def facvisita():
    fi = request.args.get("FechaInicio")
    ff = request.args.get("FechaFin")
    url = f"http://34.217.254.222/ReportServerProduccion/api/FacSalvietti/getFacVisita?FechaInicio={fi}&FechaFin={ff}"
    r = requests.post(url, auth=("alex", "123"), headers=HEADERS)
    return jsonify(r.json())
