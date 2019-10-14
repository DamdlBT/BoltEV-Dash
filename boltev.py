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
        dcc.Graph(id="graph")
    ]
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