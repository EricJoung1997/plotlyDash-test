import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.title = 'ZYJtest'
application = app.server

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        This is Dash running on Codespace.
    '''),

    dcc.Graph(
        id='example-graph',
        config={
                    'displayModeBar': True,
                    'displaylogo': False,                                       
                    'modeBarButtonsToRemove': ['zoom2d', 'hoverCompareCartesian', 'hoverClosestCartesian', 'toggleSpikelines']
                },
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
            ],
            'layout': {
                'title': 'This is a test'
            }
        }
    )
])



if __name__ == '__main__':
    application.run(debug=True)
