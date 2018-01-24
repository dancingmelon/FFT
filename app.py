import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import numpy as np

from lectures_code.section_02 import x, k1, euler1

app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})


# due to issues of plotly polar charts, this work is suspended for now
# see https://github.com/plotly/plotly.js/issues/275

app.layout = html.Div([
    dcc.Graph(
        id='exponential',
        figure={
            'data': [
                go.Scatter(
                    x=x,
                    y=np.exp(x),
                    mode='lines',
                    marker={
                        'color': 'blue'
                    },
                    name='exponetial curve'
                )
            ],

            'layout': go.Layout(
                title='Exponetial Curve',
                titlefont={"size": 16,
                           "color": "red"},
                xaxis={'title': 'x',
                       'range': [np.min(x), np.max(x)]},
                yaxis={'title': 'exp(x)',
                       'range': [0, np.exp(x[-1])]},
                width=700,
                height=700
            )
        },
        style={'display': 'inline-block'}
    ),

    dcc.Graph(
        id='complex number plot',
        figure={
            'data': [
                go.Scatter(
                    r=np.array([np.abs(euler1)]),
                    t=np.array([np.angle(euler1)*180/np.pi]),
                    mode='markers',
                    name='Trial 4',
                    marker=dict(
                        color='rgb(231,41,138)',
                        size=200,
                        line=dict(
                            color='red'
                        ),
                        opacity=0.7
                    )
                )
            ],

            'layout': go.Layout(
                title='Complex Number Plot',
                titlefont={"size": 16,
                           "color": "red"},
                font={'size': 15},
                plot_bgcolor='rgb(223,223,223)',
                angularaxis={'tickcolor': 'rgb(253,253,253)'},
                direction='counterclockwise',
                width=700,
                height=700
            )
        },
        style={'display': 'inline-block'}
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
