import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import random
import plotly
import plotly.graph_objs as go
from collections import deque
from dash.dependencies import Output, Input

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

matched_stats = {
    'Total Ride Request': [43, 32, 19, 32, 20, 15, 20, 19, 19, 21, 19, 8, 14],
    'Matched Riders': [67, 55, 63, 39, 36, 34, 23, 21, 20, 16, 15, 26, 17],
    'Unmatched Riders': [110, 86, 82, 71, 56, 49, 43, 40, 39, 37, 34, 34, 31],
    'Unmatched Drivers': [223, 202, 167, 172, 147, 115, 135, 103, 119, 112, 120, 101, 102]
}


# df = pd.read_csv(
#     'https://gist.githubusercontent.com/chriddyp/'
#     'c78bf172206ce24f77d6363a2d754b59/raw/'
#     'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
#     'usa-agricultural-exports-2011.csv')

df = pd.DataFrame(matched_stats)


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


app.layout = html.Div(children=[
    html.H1(children='UMatch', style={'textAlign': 'center'}),

    html.Div(style={'textAlign': 'center'}, children='''
        Greedy Matching Live updates
    '''),

    dcc.Graph(
        id='general-matching',
        animate=True,
        # style={'height': '100%', 'width': '100%', 'display': 'inline-block'},
        # figure={
        #     'data': [
        #         {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
        #         {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
        #     ],
        #     'layout': {
        #         'title': 'Riders Matched'
        #     },

        # }
    ),
    dcc.Interval(
        id="general-matching-update",
        interval=1
    ),

    # dcc.Graph(
    #     id='example-graph2',
    #     style={'height': '30%', 'width': '50%', 'display': 'inline-block'},
    #     figure={
    #         'data': [
    #             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
    #             {'x': [1, 2, 3], 'y': [2, 4, 5],
    #                 'type': 'bar', 'name': u'Montréal'},
    #         ],
    #         'layout': {
    #             'title': 'Unmatched Riders'
    #         }
    #     }
    # ),
    # dcc.Graph(
    #     id='example-graph3',
    #     style={'height': '30%', 'width': '50%', 'display': 'inline-block'},
    #     figure={
    #         'data': [
    #             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
    #             {'x': [1, 2, 3], 'y': [2, 4, 5],
    #                 'type': 'bar', 'name': u'Montréal'},
    #         ],
    #         'layout': {
    #             'title': 'Unmatched Drivers'
    #         }
    #     }
    # ),

    # html.Div(children=[
    #     html.H4("Matched/Unmatched Statestics per window"),
    #     generate_table(df)
    # ],
    #     className="six columns"),
])


@app.callback(
    Output('general-matching', 'figure'),
    [Input('general-matching-update', 'interval')])
def update_graph_scatter():
    # X.append(X[-1]+1)
    # Y.append(Y[-1]+Y[-1]*random.uniform(-0.1, 0.1))

    # data = plotly.graph_objs.Scatter(
    #     x=list(X),
    #     y=list(Y),
    #     name='Scatter',
    #     mode='lines+markers'
    # )

    figure = {
        'data': [
            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5],
             'type': 'bar', 'name': u'Montréal'},
        ],
        'layout': {
            'title': 'Unmatched Drivers'
        }
    }
    # return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                                # yaxis=dict(range=[min(Y), max(Y)]),)}

    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
