import dash
import dash_core_components as dcc
import dash_html_components as html

layout = html.Div(
    children=[
        html.H1("Bolt EV - Efficacité et Autonomie")
    ]
)

app = dash.Dash(__name__)

app.layout = layout

if __name__ == '__main__':

    app.server.run(debug=True)