import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import os

dash.register_page(__name__, path="/")

# Page layout
layout = dbc.Container([

    dbc.Row(
        dbc.Col(
            dbc.Card(
                dbc.CardHeader(
                    "Plataforma de Hechos Viales (OCISEVI)",
                    style={'background-color': '#FFFFFF', 'font-weight': 'bold'}
                )
            ),
            lg=12, className='pt-4'
        )
    )

])