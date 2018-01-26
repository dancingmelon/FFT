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

sine_phas = np.pi / 4
sine_freq = np.arange(2., 10., .5)

# Attn: this is a global variable used across different callbacks, suitable only for single user app!!!!
morlet_wavelet = np.zeros(len(time))


def calculate_morlet_wavelet(morlet_phas):
    morlet_sine = np.sin(2 * np.pi * morlet_freq * time + morlet_phas)
    morlet_signal = morlet_sine * morlet_exp

    return morlet_signal


def calculate_dot_product(morlet_signal):
    dps = np.zeros(len(sine_freq))

    for i in range(0, len(dps)):
        sine_wave = np.sin(2 * np.pi * sine_freq[i] * time + sine_phas)
        dps[i] = np.dot(morlet_signal, sine_wave) / len(time)

    return dps


app.layout = html.Div([

    html.H2("Dot Products Between Morlet Wavelet and Sine Function", style={'textAlign': 'center'}),

    html.Hr(),

    html.Div([

        html.Div([
            dcc.Graph(
                id='graph-morlet-wave'
            )
        ], style={'margin': '0px auto'}),

        html.Hr(),

        html.Div([
            html.Label(id='label-morlet-phas'),
            dcc.Slider(
                id='slider-morlet-phas',
                min=0,
                max=np.pi * 2,
                value=0,
                step=0.1,
                marks={
                    0: '0',
                    np.pi / 2: '1/2 pi',
                    np.pi: 'pi',
                    np.pi * 3 / 2: '3/2 pi',
                    np.pi * 2: '2 pi'
                },
                updatemode='drag'
            )
        ]),

        html.Hr(),

        html.Div([
            dcc.Graph(
                id='graph-dot-products'
            )
        ]),

        html.Hr(),

        html.Div(id='signal', style={'display': 'none'})

    ])
], style={'width': 1000, 'margin': '30px auto'})


@app.callback(
    Output('label-morlet-phas', 'children'),
    [Input('slider-morlet-phas', 'value')])
def update_label_sine_phas(morlet_phas):
    return "Morlet Wave Phase = {}".format(morlet_phas)


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
            )
        ],

        'layout': go.Layout(
            title='Morlet Wavelet',
            titlefont={"size": 24},
            xaxis={'title': 'time [s]',
                   'range': [np.min(time) - 0.1, np.max(time) + 0.1]},
            yaxis={'title': '[a.u.]',
                   'range': [-1.1, 1.1]},
            height=300
        )
    }


@app.callback(
    Output('graph-dot-products', 'figure'),
    [Input('signal', 'children')]
)
def update_graph_dot_products(value):
    dps = calculate_dot_product(morlet_wavelet)

    return {
        'data': [
            go.Scatter(
                x=sine_freq,
                y=dps,
                mode='markers',
                marker={
                    'size': 20
                },
                name='dot products'
            )
        ],

        'layout': go.Layout(
            title='Dot Products',
            titlefont={"size": 24},
            xaxis={'title': 'Sine Wave Frequency [Hz]',
                   'range': [np.min(sine_freq) - 0.1, np.max(sine_freq) + 0.1]},
            yaxis={'title': '[a.u.]',
                   'range': [-0.2, 0.2]},
            height=300
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
