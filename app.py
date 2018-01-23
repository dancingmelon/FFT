import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import numpy as np

from lectures_code.section_02 import z

app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.layout = html.Div([
    html.H1("The complexe number z = 4 + 3i"),
    dcc.Graph(
        id='single complex number',
        figure={
            'data': [
                go.Scatter(
                    x=np.array([z.real]),
                    y=np.array([z.imag]),
                    # x=random_x,
                    # y=random_y,
                    text='complexe number (4 + 3i)',
                    mode='markers',
                    marker={
                        'size': 15,
                        'color': 'red',
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name='complexe number'
                )
            ],

            'layout': go.Layout(
                title='Complex numbers',
                xaxis={'title': 'Real axis',
                       'range': [-5, 5]},
                yaxis={'title': 'Imaginary axis',
                       'range': [-5, 5]},
                width=700,
                height=700
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
