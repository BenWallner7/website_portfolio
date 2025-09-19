import pandas as pd
import plotly.express as px
import plotly.io as pio
import os
import kagglehub

# Download datasets
# kagglehub.dataset_download('arezaei81/heartcsv', path='setup_dashboards/heart', force_download=True)
# kagglehub.dataset_download('owid/covid-19-data')

# Ensure folder exists
os.makedirs("static/figures", exist_ok=True)

# Diabetes Dashboard

diabetes_url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
df_diabetes = pd.read_csv(diabetes_url)

# Scatter plot
scatter_fig = px.scatter(df_diabetes, x="Glucose", y="BMI", color="Outcome",
                         title="Glucose vs BMI by Diabetes Outcome")
pio.write_json(scatter_fig, "static/figures/diabetes_scatter.json")
scatter_fig.write_image("static/figures/diabetes_scatter.jpeg", width=800, height=600)

# Histogram
hist_fig = px.histogram(df_diabetes, x="Age", color="Outcome", barmode="overlay",
                        title="Age Distribution by Diabetes Outcome")
pio.write_json(hist_fig, "static/figures/diabetes_hist.json")
hist_fig.write_image("static/figures/diabetes_hist.jpeg", width=800, height=600)

# Box plot
box_fig = px.box(df_diabetes, x="Outcome", y="BloodPressure",
                 title="Blood Pressure by Diabetes Outcome")
pio.write_json(box_fig, "static/figures/diabetes_box.json")
box_fig.write_image("static/figures/diabetes_box.jpeg", width=800, height=600)

# Heart Disease Dashboard

# heart_url = "https://raw.githubusercontent.com/plotly/datasets/master/heart.csv"
# df_heart = pd.read_csv(heart_url)

# # Correlation heatmap
# corr_fig = px.imshow(df_heart.corr(), text_auto=True, title="Heart Disease Feature Correlation Heatmap")
# pio.write_json(corr_fig, "static/figures/heart_corr.json")

# # Scatter matrix

# scatter_matrix_fig = px.scatter_matrix(df_heart, dimensions=["age", "chol", "trestbps"],
#                                        color="target", title="Heart Disease Scatter Matrix")
# pio.write_json(scatter_matrix_fig, "static/figures/heart_scatter_matrix.json")


# # COVID-19 Dashboard

# covid_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
# df_covid = pd.read_csv(covid_url)
# df_covid = df_covid[df_covid['location'].isin(['United States','India','Brazil','Germany'])]

# # Time series line plot
# line_fig = px.line(df_covid, x="date", y="new_cases", color="location",
#                    title="Daily New COVID-19 Cases")
# pio.write_json(line_fig, "static/figures/covid_line.json")

# # Choropleth map (
# latest = df_covid[df_covid['date'] == df_covid['date'].max()]
# map_fig = px.choropleth(latest, locations="iso_code", color="total_cases",
#                         hover_name="location", title="Total COVID-19 Cases by Country")
# pio.write_json(map_fig, "static/figures/covid_map.json")

print("All figures saved to static/figures/")