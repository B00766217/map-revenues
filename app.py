# choropleth map of revenues
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


df = pd.read_csv("df_map.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([html.Div([html.H2("SBKE Group - Revenues by Territory")],
                                style={'textAlign': "center", "padding-bottom": "30"}),
                       html.Div([html.Span("Select year : ", className="six columns",
                                           style={"text-align": "right", "width": "40%", "padding-top": 10}),
                                 dcc.Dropdown(id="value-selected", value='2020B',
                                              options=[{'label': "2017A ", 'value': '2017A'},
                                                       {'label': "2018A ", 'value': '2018A'},
                                                       {'label': "2019F ", 'value': '2019F'},
													   {'label': "2020B ", 'value': '2020B'}],
                                              style={"display": "block", "margin-left": "auto", "margin-right": "auto",
                                                     "width": "70%"},
                                              className="six columns")], className="row"),
                       dcc.Graph(id="my-graph")
                       ], className="container")


@app.callback(
    dash.dependencies.Output("my-graph", "figure"),
    [dash.dependencies.Input("value-selected", "value")]
)
def update_figure(selected):
    dff = df.groupby(['Territory', 'Territory_name']).mean().reset_index()
    def title(text):
        if text == "2017A":
            return "Revenue 2017 Actual"
        elif text == "2018A":
            return "Revenue 2018 Actual"
        elif text == "2019F":
            return "Revenue 2019 Forecast"
        else:
            return "Revenue 2020 Budget"
    trace = go.Choropleth(locations=dff['Territory'],z=dff[selected],text=dff['Territory_name'],autocolorscale=False,
                          colorscale="YlGnBu",marker={'line': {'color': 'rgb(180,180,180)','width': 0.5}},
                          colorbar={"thickness": 10,"len": 0.3,"x": 0.9,"y": 0.7,
                                    'title': {"text": title(selected), "side": "bottom"}})
    return {"data": [trace],
            "layout": go.Layout(title=title(selected),height=800,geo={'showframe': False,'showcoastlines': False,
                                                                      'projection': {'type': "miller"}})}

if __name__ == '__main__':
    app.run_server(debug=True)
