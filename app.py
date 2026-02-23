import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Déposez votre code à partir d'ici :

@app.route("/contact")
def MaPremiereAPI():
    # Exercice 6 : Pointage vers un fichier élaboré (Design Créatif)
    return render_template("contact.html")

@app.get("/paris")
def api_paris():
    # Exercice 2 : Données Météo Paris
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])

    n = min(len(times), len(temps))
    result = [
        {"datetime": times[i], "temperature_c": temps[i]}
        for i in range(n)
    ]

    return jsonify(result)

@app.route("/rapport")
def mongraphique():
    # Exercice 3 & 4 : Rapport Graphique
    return render_template("graphique.html")

@app.route("/histogramme")
def monhistogramme():
    # Exercice 5 : Histogramme
    return render_template("histogramme.html")

@app.route("/atelier")
def monatelier():
    # Séquence 4 : Atelier libre (Vitesse du vent à Marseille avec Gauge Chart)
    return render_template("atelier.html")

@app.get("/marseille/vent")
def api_marseille_vent():
    # Données pour l'atelier (Vitesse du vent à Marseille)
    url = "https://api.open-meteo.com/v1/forecast?latitude=43.2965&longitude=5.3698&current=wind_speed_10m"
    response = requests.get(url)
    data = response.json()
    
    speed = data.get("current", {}).get("wind_speed_10m", 0)
    return jsonify({"city": "Marseille", "wind_speed": speed, "unit": "km/h"})

# Ne rien mettre après ce commentaire
    
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
