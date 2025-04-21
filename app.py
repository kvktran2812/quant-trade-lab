import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages=True)


# This is the Logo and App name
header = html.Div(
    className="header",
    children=[
        html.Img(src="assets/icon.png", alt="icon"),
        html.H1('Quant Trade Lab')
    ]
)


# This is the Navigation bar
navbar = html.Div(
    className="navbar",
    children=[
        html.Span(
            dcc.Link(f"{page['name']}", href=page["relative_path"]),
        ) for page in dash.page_registry.values()
    ]
)


# All pages layers together with the header and navbar
app.layout = html.Div(
    children=[
        header,
        navbar,
        html.Hr(className="app-hr"),
        dash.page_container
    ],
)

if __name__ == '__main__':
    app.run(debug=True)