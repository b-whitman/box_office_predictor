# Imports from 3rd party libraries
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## See You At The Movies!
            
            Thinking of investing in a feature film? Plug its projected runtime and genres into this model to help you decide whether or not it's worth your money!
            """
        ),
        dcc.Link(dbc.Button('Get Started', color='primary'), href='/predictions')
    ],
    md=4,
)

box_office = pd.read_csv('notebooks/box_office.csv')
fig = px.scatter(box_office, x='Production_Budget', y='Worldwide_Gross', color='runtimeNumber', marginal_x='histogram')

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])