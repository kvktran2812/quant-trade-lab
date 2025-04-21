import dash
from dash import html

dash.register_page(
    __name__,
    order=2,
)

layout = html.Div([
    html.H1('This is our Analytics page'),
    html.Div('This is our Analytics page content.'),
])