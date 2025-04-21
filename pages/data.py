import dash
from dash import html

dash.register_page(
    __name__,
    order=1,
)

layout = html.Div([
    html.H1('This is our Data page'),
    html.Div('This is our Data page content.'),
])