import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import  pandas as pd

days = pd.read_csv("data/data.csv")

layout = html.Div(
    children=[
        html.H1("Bolt EV - Efficacité et Autonomie"),
        html.Label('Variable x'),
        dcc.Dropdown(
            id="x",
            options=[
                {"label": c, "value": c} for c in sorted(days.columns)
            ],
            placeholder="choisir la variable",
        ),
        html.Label('Variable y'),
        dcc.Dropdown(
            id="y",
            options=[
                {"label": c, "value": c} for c in sorted(days.columns)
            ],
            placeholder="choisir la variable",
        ),
    ]
)

app = dash.Dash(__name__)

app.layout = layout

if __name__ == '__main__':

    app.server.run(debug=True)