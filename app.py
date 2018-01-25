import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import numpy as np

app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

srate = 500
time = np.arange(0., 2., 1. / srate)
# freq = 3
# ampl = 2
# phas = np.pi / 3
#
# sinwave = ampl * np.sin(2 * np.pi * freq * time + phas)
# coswave = ampl * np.cos(2 * np.pi * freq * time + phas)

app.layout = html.Div([
    html.H1("Sine and Cosine Wave Visualization"),

    html.Div([
        dcc.Graph(
            id='graph-waves',
            style={'display': 'inline-block'}
        ),

        html.Div([

            html.Label(id='label-ampl', style={'marginTop': 120}),
            dcc.Slider(
                id='slider-ampl',
                min=0,
                max=10,
                value=5,
                step=0.1,
                marks={
                    i: '{}'.format(i) for i in range(11)
                },
                updatemode='drag'
            ),
            html.Hr(),

            html.Label('Frequency', id='label-freq', style={'marginTop': 20}),
            dcc.Slider(
                id='slider-freq',
                min=0,
                max=10,
                value=5,
                step=0.1,
                marks={
                    i: '{}'.format(i) for i in range(11)
                },
                updatemode='drag'
            ),
            html.Hr(),

            html.Label('Phase', id='label-phas', style={'marginTop': 20}),
            dcc.Slider(
                id='slider-phas',
                min=0,
                max=2 * np.pi,
                value=np.pi / 3,
                step=0.05,
                marks={
                    0: '0',
                    np.pi / 2: '1/2 pi',
                    np.pi: 'pi',
                    np.pi * 3 / 2: '3/2 pi',
                    np.pi * 2: '2 pi'
                },
                updatemode='drag'
            ),
            html.Hr()

        ],
            style={'display': 'inline-block', 'width': 400, 'verticalAlign': 'top', 'marginLeft': 50})
    ]),

    html.Hr(),

    html.Div([

        html.H1("Complex Sine Wave Visualization"),

        html.Div([

            dcc.Graph(id='3d-curve', style={'display': 'inline-block'}),

            html.Div([
                html.Div([
                    html.Label(id='label-ampl-3d', style={'marginTop': 120}),
                    dcc.Slider(
                        id='slider-ampl-3d',
                        min=0,
                        max=10,
                        value=5,
                        step=0.1,
                        marks={
                            i: '{}'.format(i) for i in range(11)
                        },
                        updatemode='drag'
                    ),
                    html.Hr(),

                    html.Label(id='label-freq-3d', style={'marginTop': 20}),
                    dcc.Slider(
                        id='slider-freq-3d',
                        min=0,
                        max=10,
                        value=5,
                        step=0.1,
                        marks={
                            i: '{}'.format(i) for i in range(11)
                        },
                        updatemode='drag'
                    ),
                    html.Hr(),

                    html.Label(id='label-phas-3d', style={'marginTop': 20}),
                    dcc.Slider(
                        id='slider-phas-3d',
                        min=0,
                        max=2 * np.pi,
                        value=np.pi / 3,
                        step=0.05,
                        marks={
                            0: '0',
                            np.pi / 2: '1/2 pi',
                            np.pi: 'pi',
                            np.pi * 3 / 2: '3/2 pi',
                            np.pi * 2: '2 pi'
                        },
                        updatemode='drag'
                    ),
                    html.Hr()
                ])
            ], style={'display': 'inline-block', 'width': 400, 'verticalAlign': 'top', 'marginLeft': 50})
        ])
    ])
])


@app.callback(
    Output('label-ampl', 'children'),
    [Input('slider-ampl', 'value')])
def update_label_ampl(value):
    return "Amplitude = {}".format(value)


@app.callback(
    Output('label-ampl-3d', 'children'),
    [Input('slider-ampl-3d', 'value')])
def update_label_ampl(value):
    return "3D Amplitude = {}".format(value)


@app.callback(
    Output('label-freq', 'children'),
    [Input('slider-freq', 'value')])
def update_label_freq(value):
    return "Frequency = {}".format(value)


@app.callback(
    Output('label-freq-3d', 'children'),
    [Input('slider-freq-3d', 'value')])
def update_label_freq_3d(value):
    return "3D Frequency = {}".format(value)


@app.callback(
    Output('label-phas', 'children'),
    [Input('slider-phas', 'value')])
def update_label_phas(value):
    return "Phase = {}".format(value)


@app.callback(
    Output('label-phas-3d', 'children'),
    [Input('slider-phas-3d', 'value')])
def update_label_phas(value):
    return "3D Phase = {}".format(value)


@app.callback(
    Output('graph-waves', 'figure'),
    [Input('slider-ampl', 'value'),
     Input('slider-freq', 'value'),
     Input('slider-phas', 'value')]
)
def update_graph_ampl(ampl, freq, phas):
    sinwave = ampl * np.sin(2 * np.pi * freq * time + phas)
    coswave = ampl * np.cos(2 * np.pi * freq * time + phas)

    return {
        'data': [
            go.Scatter(
                x=time,
                y=sinwave,
                mode='lines',
                name='sine wave'
            ),
            go.Scatter(
                x=time,
                y=coswave,
                mode='lines',
                name='cos wave'
            )
        ],

        'layout': go.Layout(
            title='Sine and Cosine Waves',
            titlefont={"size": 16},
            xaxis={'title': 'time [s]',
                   'range': [np.min(time), np.max(time)]},
            yaxis={'title': 'amplitude [a.u.]',
                   'range': [-11, 11]},
            width=700,
            height=700
        )
    }


@app.callback(
    Output('3d-curve', 'figure'),
    [Input('slider-ampl-3d', 'value'),
     Input('slider-freq-3d', 'value'),
     Input('slider-phas-3d', 'value')]
)
def update_graph_ampl(ampl, freq, phas):
    complex_wave = ampl * np.exp(1j * (2 * np.pi * freq * time + phas))

    return {
        'data': [
            go.Scatter3d(
                x=time,
                y=np.real(complex_wave),
                z=np.imag(complex_wave),
                mode='lines',
                name='Complex Wave'
            )],

        'layout': go.Layout(
            title='Complex Wave',
            titlefont={"size": 16},
            scene=dict(
                bgcolor='rgb(240, 240, 240)',
                aspectmode='cube',
                xaxis={'title': 'time [s]',
                       'range': [np.min(time), np.max(time)]},
                yaxis={'title': 'Real Axis',
                       'range': [-11, 11]},
                zaxis={'title': 'Imaginary Axis',
                       'range': [-11, 11]},

            ),
            width=700,
            height=700
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
