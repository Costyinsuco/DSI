import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Import layouts from each tab
from tabs.intro import layout as intro_layout
from tabs.overview import layout as overview_layout
from tabs.division import layout as division_layout
from tabs.countries import layout as country_layout
from tabs.comment import layout as comment_layout  # NEW: import the comment tab layout

external_stylesheets = ['https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "DSI Evaluation Dashboard"

# Define colors
main_color = "#00828e"
tab_color = "#005E66"
text_color = "#ffffff"

app.layout = html.Div(style={'fontFamily': 'Roboto, sans-serif'}, children=[
    html.H1(
        "Tableau de bord d’évaluation de la DSI",
        style={
            'textAlign': 'center',
            'color': main_color,
            'marginBottom': '20px',
            'fontWeight': '700',
            'fontSize': '32px'
        }
    ),

    dcc.Tabs(
        id="tabs",
        value='tab-1',
        children=[
            dcc.Tab(label='Introduction', value='tab-1'),
            dcc.Tab(label='Vue d’ensemble DSI', value='tab-2'),
            dcc.Tab(label='Par division', value='tab-3'),
            dcc.Tab(label='Par pays', value='tab-4'),
            dcc.Tab(label='Commentaires', value='tab-5'),  # NEW: Comments tab
        ],
        colors={
            "border": tab_color,
            "primary": main_color,
            "background": "white"
        },
        style={
            'fontWeight': 'bold',
            'fontSize': '18px',
        },
        className="custom-tabs"
    ),
    html.Div(id='tabs-content', style={'padding': '20px'})
])

@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return intro_layout
    elif tab == 'tab-2':
        return overview_layout
    elif tab == 'tab-3':
        return division_layout
    elif tab == 'tab-4':
        return country_layout
    elif tab == 'tab-5':  # NEW
        return comment_layout

if __name__ == '__main__':
    server = app.server  # Required for Render
    app.run(debug=False, host="0.0.0.0", port=8080)
