import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import numpy as np

app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

srate = 1000
time = np.arange(-1., 1., 1. / srate)

morlet_freq = 5
morlet_exp = np.exp((-time ** 2) / .1)

real_wave = np.cos(2 * np.pi * morlet_freq * time)
complex_wave = np.exp(1j * 2 * np.pi * morlet_freq * time)

morlet_wave = None


def calculate_morlet_wavelet(morlet_phas):
    morlet_sine = np.sin(2 * np.pi * morlet_freq * time + morlet_phas)
    morlet_signal = morlet_sine * morlet_exp

    return morlet_signal


app.layout = html.Div([

    html.H2("Real vs. Complex Dot Products", style={'textAlign': 'center'}),

    html.Hr(),

    dcc.Interval(
        id='interval-component',
        interval=0.05 * 1000,  # in milliseconds
        n_intervals=0
    ),

    html.Div([

        html.Div([
            dcc.Graph(
                id='graph-morlet-wave'
            )
        ]),

        html.Hr(),

        html.Div([
            html.Label(id='label-interval'),
            html.Label(id='label-morlet-phas'),
            dcc.Slider(
                id='slider-morlet-phas',
                min=0,
                max=np.pi * 4,
                value=0,
                step=0.05,
                marks={
                    0: '0',
                    np.pi / 2: '1/2 pi',
                    np.pi: 'pi',
                    np.pi * 3 / 2: '3/2 pi',
                    np.pi * 2: '2 pi',
                    np.pi * 5 / 2: '5/2 pi',
                    np.pi * 3: '3 pi',
                    np.pi * 7 / 2: '7/2 pi',
                    np.pi * 4: '4 pi'
                },
                updatemode='drag'
            )
        ], style={'marginBottom': 30}),

        html.Div([
            html.Div([
                dcc.Graph(id='graph-real-dot-product')
            ], style={'display': 'inline-block', 'width': 500}),
            html.Div([
                dcc.Graph(id='graph-complex-dot-product')
            ], style={'display': 'inline-block', 'width': 500})
        ])

    ]),

    html.Div(id='signal', style={'display': 'none'}),

], style={'width': 1000, 'margin': '30px auto'})


@app.callback(
    Output('label-interval', 'children'),
    [Input('interval-component', 'n_intervals')])
def update_slider_morlet_phas(n_intervals):
    return "n_intervals = {}".format(n_intervals)


@app.callback(
    Output('slider-morlet-phas', 'value'),
    [Input('interval-component', 'n_intervals')])
def update_slider_morlet_phas(n_intervals):
    proxy_value = n_intervals % len(np.arange(0., np.pi * 4, 0.05))
    value = 0 + proxy_value * 0.05
    return value

    # min = 0,
    # max = np.pi * 4,
    # value = 0,
    # step = 0.05,


@app.callback(
    Output('label-morlet-phas', 'children'),
    [Input('slider-morlet-phas', 'value')])
def update_label_morlet_phas(morlet_phas):
    return "Morlet Wave Phase = {} pi".format(round(morlet_phas / np.pi, 1))


@app.callback(
    Output('signal', 'children'),
    [Input('slider-morlet-phas', 'value')])
def send_signal(morlet_phas):
    # change global variable for use across different callbacks
    # use a non-displayed div as signal
    global morlet_wavelet
    morlet_wavelet = calculate_morlet_wavelet(morlet_phas)
    return "signal sent"


@app.callback(
    Output('graph-morlet-wave', 'figure'),
    [Input('signal', 'children')]
)
def update_graph_morlet_wave(value):
    return {
        'data': [
            go.Scatter(
                x=time,
                y=morlet_wavelet,
                mode='lines',
                name='morlet wavelet'
            ),

            go.Scatter(
                x=time,
                y=complex_wave.real,
                mode='lines',
                name='real part'
            ),

            go.Scatter(
                x=time,
                y=complex_wave.imag,
                mode='lines',
                name='imaginary part'
            )
        ],

        'layout': go.Layout(
            title='Morlet Wavelet',
            titlefont={"size": 24},
            xaxis={'title': 'time [s]',
                   'range': [np.min(time) - 0.1, np.max(time) + 0.1]},
            yaxis={'title': '[a.u.]',
                   'range': [-1.1, 1.1]},
            height=400
        )
    }


@app.callback(
    Output('graph-real-dot-product', 'figure'),
    [Input('signal', 'children')]
)
def update_graph_real_dot_product(value):
    dp_real = np.dot(morlet_wavelet, real_wave) / len(time)

    return {
        'data': [
            go.Scatter(
                x=[dp_real],
                y=[0],
                mode='markers',
                marker={
                    'size': 20,
                    'color': 'red'
                },
                name='real dot products'
            ),
            go.Scatter(
                x=[0, dp_real],
                y=[0, 0],
                mode='lines',
                line={
                    'color': 'red'
                }
            )
        ],

        'layout': go.Layout(
            title='Real Dot Products',
            titlefont={"size": 18},
            xaxis={'title': 'Real',
                   'range': [-0.2, 0.2]},
            yaxis={'title': '[a.u.]',
                   'range': [-0.2, 0.2]},
            showlegend=False,
            width=500,
            height=500
        )
    }


@app.callback(
    Output('graph-complex-dot-product', 'figure'),
    [Input('signal', 'children')]
)
def update_graph_complex_dot_product(value):
    dp_complex = np.dot(morlet_wavelet, complex_wave) / len(time)

    return {
        'data': [
            go.Scatter(
                x=[dp_complex.real],
                y=[dp_complex.imag],
                mode='markers',
                marker={
                    'size': 20,
                    'color': 'red'
                },
                name='complex dot products'
            ),
            go.Scatter(
                x=[0, dp_complex.real],
                y=[0, dp_complex.imag],
                mode='lines',
                line={
                    'color': 'red'
                }
            )
        ],

        'layout': go.Layout(
            title='Complex Dot Products',
            titlefont={"size": 18},
            xaxis={'title': 'Real',
                   'range': [-0.2, 0.2]},
            yaxis={'title': '[a.u.]',
                   'range': [-0.2, 0.2]},
            showlegend=False,
            width=500,
            height=500
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
