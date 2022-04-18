
from dash import Dash, html, dcc
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output
from decode import decode
from encode import encode

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background'], 'height':'100vh'},children=[
    html.H1(children='Break Caesar Code', style={
        'textAlign': 'center',
        'color': colors['text'],
    }),
    
    html.Div(children='''A software to decode caesar cipher''', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Br(),
    html.Div(children='''Encode a word''', style={
        'color': colors['text']
    }),
    dcc.Input(id="input1", type="text", placeholder="", style={'marginRight':'10px'}),
    dcc.Input(id="input2", type="number", placeholder="choose the encryption key"),
    html.Div(id="output", style={
        'color': colors['text']
    }),
    
    html.Br(),
    html.Div(children='''Decode a word''', style={
        'color': colors['text']
    }),
    dcc.Input(id="input3", type="text", placeholder="", style={'marginRight':'10px'}),
    html.Div(id="output1", style={
        'color': colors['text']
    }),
    
    ])

@app.callback(
    Output(component_id="output",  component_property="children"),
    Input(component_id="input1",  component_property="value"),
    Input(component_id="input2",  component_property="value"),
)
def encode_output(input1, input2):
    return u'encoded Word : {}'.format(encode(input1, input2))

@app.callback(
    Output(component_id="output1",  component_property="children"),
    Input(component_id="input3",  component_property="value"),
)

def decode_output(input1):
    result=""
    if decode(input1):
        for k in decode(input1):
            result = result + str(k) + ", "      
        return result
    else:
        return ""

if __name__ == '__main__':
    app.run_server(debug=True)