from flask import Flask, render_template
from markupsafe import Markup
import plotly.express as px
import plotly
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

# @app.route("/dashboards")
# def dashboards():
#     # Example datasets
#     df = px.data.gapminder().query("country=='Canada'")
#     df2 = px.data.iris()

#     # Charts
#     fig1 = px.line(df, x="year", y="lifeExp", title="Life Expectancy in Canada")
#     fig2 = px.bar(df, x="year", y="pop", title="Population in Canada")
#     fig3 = px.scatter(df2, x="sepal_width", y="sepal_length", color="species",
#                       title="Iris Flower Dataset")

#     # Convert to JSON
#     charts = [fig1, fig2, fig3]
#     graphJSON = [json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder) for fig in charts]

#     return render_template("dashboards.html", plots=graphJSON)