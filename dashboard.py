import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

def create_dashboard(df):
    app = dash.Dash(__name__)
    
    fig = px.histogram(df, x='criando_at', title='Tweets Postados')
    
    app.layout = html.Div(children=[
        html.H1(children='Twitter Data Dashboard'),
        dcc.Graph(
            id='tweets-histogram',
            figure=fig
        )
    ])
    
    return app
