# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process

            Movies are interesting. They're one of the most popular, profitable art forms yet devised.
            So analyzing them demands a blend of qualitative and quantitative approaches. Studio executives
            are responsible for allocating millions and millions of dollars to projects, and I'm interested
            in some of the processes they use to make those huge business decisions. So I chose to target box
            office returns. I log-transformed my target to fit it to a normal distribution, and I used a mean
            baseline because it seemed like a good enough heuristic to get me started. As an evaluation metric,
            I chose mean squared error at first and later tried mean absolute error as well. I like the
            interpretability of mean absolute error. I think if a studio were to try to use this model, MAE would
            deliver the most explainable results. "The model predicts this movie would make 150 million dollars,
            and the model's results tend to be within 60 million dollars of actual box office."

            I started with the user rating feature taken into account, but upon further reflection that feature
            seems leaky. You can't predict how a movie is going to be received by audiences. However, as noted
            in the 'insights' page, movies in post-production are often shown to test audiences and focus groups
            to gauge how they will be received. So I chose to abstract user rating into a boolean "hype factor."
            Movies with a 7.1 or higher on IMDb (i.e. movies in the upper quartile) are considered by this model
            to be "hyped."

            For an MAE mean baseline, I got around 120 million dollars. My XGBoost model reduces that to around 70 million
            dollars on the validation set. My linear regression model reduces it from 1.63 log-dollars to 1.26. Huzzah!
            (I ran into a bug while converting my linear regression MAE from log-dollars to USD, so I report it here
            as log-dollars)

            This model is useful for imagining how hype impacts a movie and for picking a release month. But its
            usefulness is limited. The MAE, though better than baseline, is admittedly still wicked high. If you're
            considering putting 30 million dollars into a film and someone tells you their model has an error of
            70 million dollars, you should laugh them out of the room. But if you're talking hundreds of millions 
            of dollars, which increasingly is where the biggest movies reside, that MAE sounds a little less
            ridiculous.

            I can think of numerous ways in which this project could be extended. The most interesting area for
            future research would be to turn it into a categorization problem, where you pick a ratio of budget
            to box office and try to predict what combinations of genre, release month, and runtime will most
            likely result in such a ratio.

            """
        ),

    ],
)

layout = dbc.Row([column1])