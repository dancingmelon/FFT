import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import numpy as np

from lectures_code.section_01 import z

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
                ),

                go.Scatter(
                    x=np.array([7]),
                    y=np.array([z.imag]),
                    text='complexe number (7 + 3i)',
                    mode='markers',
                    marker={
                        'size': 15,
                        'color': 'blue',
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name='another complexe number'
                )
            ],

            'layout': go.Layout(
                xaxis={'title': 'Real axis'},
                yaxis={'title': 'Imaginary axis'}
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
