from flask import Blueprint, request, jsonify
import requests

facpresupuesto_endpoint = Blueprint("facpresupuesto", __name__)

HEADERS = {"Accept": "application/json", "X-Empresa-Codigo": "1"}

@facpresupuesto_endpoint.route("/facpresupuesto")
def facpresupuesto():
    fi = request.args.get("FechaInicio")
    ff = request.args.get("FechaFin")
    url = f"http://34.217.254.222/ReportServer/api/FacSalvietti/getFacPresupuesto?FechaInicio={fi}&FechaFin={ff}"
    r = requests.post(url, auth=("alex", "123"), headers=HEADERS)
    return jsonify(r.json())
 