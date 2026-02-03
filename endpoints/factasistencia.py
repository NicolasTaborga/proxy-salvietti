from flask import Blueprint, request, jsonify
import requests

facasistencia_endpoint = Blueprint("facasistencia", __name__)

HEADERS = {"Accept": "application/json", "X-Empresa-Codigo": "1"}

@facasistencia_endpoint.route("/facasistencia")
def facasistencia():
    fi = request.args.get("FechaInicio")
    ff = request.args.get("FechaFin")
    url = f"http://34.217.254.222/ReportServerProduccion/api/FacSalvietti/getFacAsistencia?FechaInicio={fi}&FechaFin={ff}"
    r = requests.post(url, auth=("alex", "123"), headers=HEADERS)
    return jsonify(r.json())
