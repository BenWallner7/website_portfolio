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
    
    # Load figures from disk
    fig1 = pio.read_json("static/figures/diabetes_scatter.json")
    fig2 = pio.read_json("static/figures/diabetes_hist.json")
    fig3 = pio.read_json("static/figures/diabetes_box.json")

    charts = [fig1, fig2, fig3]
    graphJSON = [json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder) for fig in charts]

    return render_template("dashboards.html", plots=graphJSON)