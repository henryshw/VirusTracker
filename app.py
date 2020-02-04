import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from figures1 import fig1, fig2, confirmed_string, isolated_string, checking_string, death_string
from mapfigures import fig

app = dash.Dash(__name__,  external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = '香港疫情數據分折'
server = app.server

colors = {
    'background': '#233b5e',
    'text': '#F2F5FA'
}

####Define each component
##Header
heading = \
    dbc.Container([
        dbc.Row([
            dbc.Col([html.H1(
            children='香港疫情數據分折',
            style={
            'textAlign': 'center',
            'color': colors['text'],
            'padding-top': '30px'}
            )]),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div(html.P(children=['根據香港衞生署及醫院管理局官方資訊，分析疫情數據.', html.Br(), '最後更新時間為: 04-02-2020 10:00'],
                         style={
                             'textAlign': 'center',
                             'color': colors['text']})),
            ]),
        ])
    ])


###Map + Statistics

latest_num = dbc.Container(
    html.Div([
            html.H3(confirmed_string, style={'color': "#fc2c03"}),
            html.H3(death_string, style={'color': "#fc2c03"}),
            html.H3(isolated_string, style={'color': "#fcad03"}),
            html.H3(checking_string, style={'color': "#03fc35"}),
        ])
)


figuress = dbc.Container(
    html.Div(
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='map', figure=fig)),
            ]
        )
    , style={'padding-top':'30px'}))

statisticss = dbc.Container(
    html.Div(
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='virus', figure=fig1)),
                dbc.Col(dcc.Graph(id= 'other_graph', figure=fig2)),
            ]
        )
    , style={'padding-top':'30px'}))


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[heading,latest_num, figuress, statisticss])


if __name__ == '__main__':
    app.run_server(debug=True)
