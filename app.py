# choropleth map of revenues
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd
#app = dash.Dash(__name__)
#server = app.server
df = pd.read_csv("df_map_group_sum.csv")

#app.layout = html.Div([
fig = go.Figure(data=go.Choropleth(
    locations = df['Territory'],
    z = df['2020B_amount'],
    text = df['Territory_name'],
    colorscale = 'Greens',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.8,
    colorbar_tickprefix = '$',
    colorbar_title = 'Revenue<br>EUR',
))

fig.update_layout(
    title_text='SBKE Group - Map of 2020 Proposed Budgeted Revenues',
    geo=dict(
        showframe=True,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
),

fig.show()
#if __name__ == '__main__':
    #app.run_server(debug=True)
