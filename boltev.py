import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

layout = html.Div(
    children=[
        html.H1("Bolt EV - Efficacité et Autonomie"),
        dcc.Input(id="in"),
        html.P(id="out"),
    ]
)

app = dash.Dash(__name__)

app.layout = layout

@app.callback(Output("out", "children"), [Input("in", "value")])
def update_output(in_value):
    return in_value

if __name__ == '__main__':

    app.server.run(debug=True)