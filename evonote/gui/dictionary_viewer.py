# Import necessary libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Your dictionary
data = {
    "Key1": "Value1",
    "Key2": "Value2",
    "Key3": "Value3",
    #... add as many keys and values as you like
}

# Initialize Dash app
app = dash.Dash(__name__)

# Layout for the app
app.layout = html.Div([
    html.Div([
        html.H3("Keys:"),
        dcc.RadioItems(
            id='key-selector',
            options=[{'label': key, 'value': key} for key in data.keys()],
            value=list(data.keys())[0]
        )
    ], style={'width': '30%', 'display': 'inline-block'}),

    html.Div([
        html.H3("Value:"),
        html.Div(id='value-display', children="")
    ], style={'width': '60%', 'display': 'inline-block', 'verticalAlign': 'top'})
])

# Callback to update the value when a key is clicked
@app.callback(
    Output('value-display', 'children'),
    [Input('key-selector', 'value')]
)
def update_value(selected_key):
    return data[selected_key]

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
