import dash
import dash_bootstrap_components as dbc

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