from flask import Flask, render_template
from markupsafe import Markup
import plotly.express as px
import plotly
import json
import plotly.io as pio

# Import the dict of Plotly figures
from visualisations import figures

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/dashboards")
def dashboards():
    charts = []
    for fig_name, fig in figures.items():
        # Convert Plotly Figure to dict for Jinja
        charts.append(fig.to_dict())
    return render_template("dashboards.html", plots=charts)

# if __name__ == "__main__":
#     app.run(debug=True)
    
# @app.route("/dashboards")
# def dashboards():
    
#     # Read pre-saved JSON figures
#     figure_files = [
#         "static/figures/diabetes_scatter.json",
#         "static/figures/diabetes_hist.json",
#         "static/figures/diabetes_box.json"
#     ]
    
#     charts = []
#     for f in figure_files:
#         # Read figure JSON as dict
#         fig_dict = json.load(open(f, 'r'))
#         # Serialize with Plotly encoder for browser
#         charts.append(json.dumps(fig_dict, cls=plotly.utils.PlotlyJSONEncoder))
    
#     return render_template("dashboards.html", plots=charts)