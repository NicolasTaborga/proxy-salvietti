import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# ---------------------------
# CONFIG GENERAL
# ---------------------------
HEADERS = {
    "Accept": "application/json",
    "X-Empresa-Codigo": "1"
}

# ---------------------------
# ENDPOINT FACVENTA
# ---------------------------
@app.route("/facventa")
def facventa():
    fi = request.args.get("FechaInicio")
    ff = request.args.get("FechaFin")

    url = f"http://34.217.254.222/ReportServer/api/FacSalvietti/getFacVenta?FechaInicio={fi}&FechaFin={ff}"

    r = requests.post(url,
                      auth=("alex", "123"),
                      headers=HEADERS)

    return jsonify(r.json())


# ---------------------------
# ENDPOINT FACPRESUPUESTO
# ---------------------------
@app.route("/facpresupuesto")
def facpresupuesto():
    fi = request.args.get("FechaInicio")
    ff = request.args.get("FechaFin")

    url = f"http://34.217.254.222/ReportServer/api/FacSalvietti/getFacPresupuesto?FechaInicio={fi}&FechaFin={ff}"

    r = requests.post(url,
                      auth=("alex", "123"),
                      headers=HEADERS)

    return jsonify(r.json())


# ---------------------------
# MAIN
# ---------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

