from flask import Flask, render_template
from markupsafe import Markup
import plotly.express as px
import plotly
import json
import plotly.io as pio

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/dashboards")
def dashboards():
    figure_files = [
        "static/figures/diabetes_scatter.json",
        "static/figures/diabetes_hist.json",
        "static/figures/diabetes_box.json"
    ]
    
    charts = []
    for f in figure_files:
        with open(f, "r") as infile:
            fig_dict = json.load(infile)
            # No need for PlotlyJSONEncoder here
            charts.append(fig_dict)
    
    return render_template("dashboards.html", plots=charts)