# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
from joblib import load

# Imports from this application
from app import app

xgb = load('assets/xgb.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Set the anticipated production budget, release month, runtime, and genres.
            If you want to see a range of box office returns depending on how the audience reacts,
            you can use the "Hyped" feature as an approximation.

            """
        ),
        dcc.Markdown('#### Budget in US Dollars'),
        dcc.Slider(
            id='Production_Budget',
            min=1000000,
            max=500000000,
            step=1000000,
            value=30000000,
            #marks={n: str(n) for n in range(1000000,500000000,500000)},
            className='mb-5',
            tooltip={'always_visible': True, 'placement': 'bottom'}
        ),
        dcc.Markdown('#### Release Month'),
        dcc.Dropdown(
            id='release_month',
            options = [
                {'label': 'January', 'value': 1},
                {'label': 'February', 'value': 2},
                {'label': 'March', 'value': 3},
                {'label': 'April', 'value': 4},
                {'label': 'May', 'value': 5},
                {'label': 'June', 'value': 6},
                {'label': 'July', 'value': 7},
                {'label': 'August', 'value': 8},
                {'label': 'September', 'value': 9},
                {'label': 'October', 'value': 10},
                {'label': 'November', 'value': 11},
                {'label': 'December', 'value': 12},
            ],
            value = 1,
            className='mb-5'
        ),
        dcc.Markdown('#### Runtime in Minutes'),
        dcc.Slider(
            id='runtimeNumber',
            min=40,
            max=400,
            step=10,
            value=90,
            className='mb-5',
            tooltip={'always_visible': True, 'placement': 'bottom'}
        ),
        dcc.Markdown('#### Hyped'),
        dcc.Markdown('Is this movie likely to be well-regarded by its viewers? (i.e. IMDb user rating >= 7.1)'),
        dcc.Dropdown(
            id='hyped',
            options = [
                {'label': 'Hyped', 'value': 1},
                {'label': 'Not Hyped', 'value': 0},
            ],
            value = 0,
            className='mb-5'
        ),
        dcc.Markdown('#### Genres'),
        dcc.Markdown('Select 3 or more'),
        dcc.Checklist(
            id='genres',
            options=[
                {'label': 'Action', 'value': 1},
                {'label': 'Adventure', 'value': 2},
                {'label': 'Animation', 'value': 3},
                {'label': 'Biography', 'value': 4},
                {'label': 'Comedy', 'value': 5},
                {'label': 'Crime', 'value': 6},
                {'label': 'Documentary', 'value': 7},
                {'label': 'Drama', 'value': 8},
                {'label': 'Family', 'value': 9},
                {'label': 'Fantasy', 'value': 10},
                {'label': 'History', 'value': 11},
                {'label': 'Horror', 'value': 12},
                {'label': 'Music', 'value': 13},
                {'label': 'Musical', 'value': 14},
                {'label': 'Mystery', 'value': 15},
                {'label': 'News', 'value': 16},
                {'label': 'Romance', 'value': 17},
                {'label': 'SciFi', 'value': 18},
                {'label': 'Sport', 'value': 19},
                {'label': 'Thriller', 'value': 20},
                {'label': 'War', 'value': 21},
                {'label': 'Western', 'value': 22},
            ],
            value=[17,18,22]
        )
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Expected Box Office Take', className='mb-5'),
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2])

genres = []

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Production_Budget', 'value'), 
    Input('release_month', 'value'), 
    Input('runtimeNumber', 'value'),
    Input('hyped', 'value'),
    Input('genres', 'value')
    ],
)
def predict(Production_Budget, release_month, runtimeNumber, hyped, genres):
    df = pd.DataFrame(
        columns=['runtimeNumber', 'Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 
        'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Romance', 'Sci-Fi', 
        'Sport', 'Thriller', 'War', 'Western', 'Production_Budget', 'hyped', 'release_year', 'release_month'],
        data=[[runtimeNumber, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, Production_Budget, hyped, 2020, release_month]]
    )
    for genre_num in genres:
        df.iloc[0,genre_num] = 1
    y_pred_log = xgb.predict(df)[0]
    y_pred = np.expm1(y_pred_log)
    return f'${y_pred:,}'