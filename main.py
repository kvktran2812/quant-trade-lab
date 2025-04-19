import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    # Header Navigation
    html.Nav([
        html.Div([
            # Logo/Brand
            html.Div(
                html.A("My Dash App", href="/", className="navbar-brand"),
                className="navbar-header"
            ),
            
            # Navigation Links
            html.Ul([
                html.Li(html.A("Home", href="/", className="nav-link")),
                html.Li(html.A("Dashboard", href="/dashboard", className="nav-link")),
                html.Li(html.A("Analysis", href="/analysis", className="nav-link")),
                html.Li(html.A("About", href="/about", className="nav-link")),
            ], className="navbar-nav")
        ], className="navbar-container")
    ], className="navbar"),
    
    # Page Content
    html.Div(id='page-content', style={'padding': '20px'}),
    
    # URL Router
    dcc.Location(id='url', refresh=False)
], style={'fontFamily': 'Arial, sans-serif'})

if __name__ == '__main__':
    app.run_server(debug=True)