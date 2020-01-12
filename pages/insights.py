# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Imports from this application
from app import app

box_office = pd.read_csv('assets/box_office.csv')
box_office_comedy = box_office[box_office['Comedy'] == True]
box_office_hyped = box_office[box_office['hyped'] == True]
box_office_adventure = box_office[box_office['Adventure'] == True]

fig = px.scatter(box_office, x='Production_Budget', y='gross_log', color='runtimeNumber', marginal_x='histogram')
fig2 = px.scatter(box_office_comedy, x='Production_Budget', y='gross_log', color='runtimeNumber', marginal_x='histogram', range_x=(-25000000,425000000))
fig3 = px.scatter(box_office_hyped, x='Production_Budget', y='gross_log', color='runtimeNumber', marginal_x='histogram')
fig4 = px.scatter(box_office_adventure, x='Production_Budget', y='gross_log', color='runtimeNumber', marginal_x='histogram')

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights

            Production budget is far and away the most important factor in predicting box office.
            More expensive films make more money. This makes sense. Studios have their own methods
            for determining how much budget to allocate different projects, but in general more expensive
            movies are targeted for broader audiences.
            """
        ),
        dcc.Markdown(
            '''
            The engineered "hype" feature is also very predictive, though it is leaky, as it is based on
            IMDb user ratings data. When planning a release schedule, a movie studio obviously will not
            have access to user ratings data. Even so, I've left the feature in. Studios do focus testing
            during post-production to help predict how a movie will perform, so this feature isn't entirely
            unrealistic. And anyway, I think it's interesting to see just what an impact audience reaction
            seems to have in this model.
            '''
        ),
        html.Img(src='assets/permutation_importances.PNG', className='img-fluid'),
        dcc.Markdown(
            '''
            The partial disparity plot for production budget shows the relationship between budget and box office.
            Going from a low-budget film to a medium-budget film makes a big difference, but the higher the budget,
            the flatter the curve becomes. This may be a limitation of the model, and something that could be
            investigated in further research: the biggest movies in the world right now are the ultra-high-budget films,
            films costing hundreds of millions of dollars and earning returns in the billions.
            '''
        ),
        html.Img(src='assets/pdp.PNG', className='img-fluid'),
        dcc.Markdown(
            '''
            The PDP interact for production budget and hype helps illustrate the relationship between these two features.
            It's good for your movie to resonate with audiences!
            '''
        ),
        html.Img(src='assets/interact.PNG', className='img-fluid'),
        dcc.Markdown(
            '''
            Finally, let's break the dataset down a little bit and examine how genre distinctions and hype impact the relationship
            between budget and box office. 
            '''
        ),
        dcc.Markdown('#### Whole Dataset'),
        dcc.Graph(figure=fig),
        dcc.Markdown('#### Comedy'),
        dcc.Markdown(
            '''
            Observe that proximity to the top left corner, where we find the movies with the lowest budgets and highest returns,
            is roughly equal between the whole dataset and the comedy subset.
            '''),
        dcc.Graph(figure=fig2),
        dcc.Markdown('#### Hyped'),
        dcc.Markdown(
            '''
            Hyped movies hew a little closer to that magic top-left corner.
            '''),
        dcc.Graph(figure=fig3),
        dcc.Markdown('#### Adventure'),
        dcc.Markdown(
            '''
            And adventure movies seem to wander a little further from the top-left corner. This might mean that adventure movies are
            slightly riskier -- pouring more money into them may not have the same effect it would on movies of other genres.
            '''
        ),
        dcc.Graph(figure=fig4)
    ],
)

layout = dbc.Row([column1])