import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import  pandas as pd
import plotly_express as px

days = pd.read_csv("data/data.csv")

layout = html.Div(
    children=[
        html.H1("Bolt EV - Efficacité et Autonomie"),
        html.Hr(),
        html.Div(
            children=[
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
                html.Label('Variable couleur'),
                dcc.Dropdown(
                    id="couleur",
                    options=[
                        {"label": c, "value": c} for c in sorted(days.columns)
                    ],
                    placeholder="choisir la variable",
                ),
            ],
            style={"width": "25%", "display": "inline-block", "float": "left" }
        ),
        html.Div(
            children=[
                dcc.Graph(id="graph")
            ],
            style={"width": "75%", "display": "inline-block",}
        ),
        html.Hr(),
        html.Div(
            children=[
                html.Div(["Démo d'application utilisant ", html.A("Plotly Dash", href="https://plot.ly/dash/"), " par Damien de la Bruère-Terreault."]),
                html.A("Code source sur GitHub",  href="https://github.com/DamdlBT/BoltEV-Dash"),
            ],
            style={"text-align": "center"}
        )
    ],
    style={"max-width": "1200px", "margin": "auto"}
)

app = dash.Dash(__name__)

app.layout = layout

@app.callback(Output("graph", "figure"),
              [Input('x', 'value'),
               Input("y", "value"),
               Input("couleur", "value")])
def update_graph(x, y, couleur):
    fig = px.scatter(days, x=x, y=y, color=couleur)
    return fig               

if __name__ == '__main__':

    app.server.run(debug=True)