import dash
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = html.Div([
    html.Div(id='style-output'),
    html.H1('Page 1'),
    dcc.Dropdown(
        id='page_one-dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='page_one-content'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page_two'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),
])

@app.callback(dash.dependencies.Output('page_one-content', 'children'),
              [dash.dependencies.Input('page_one-dropdown', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)
