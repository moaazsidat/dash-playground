import dash
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = html.Div([
    html.Div(id='style-output'),
    html.H1('Page 2'),
    dcc.RadioItems(
        id='page_two-radios',
        options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
        value='Orange'
    ),
    html.Div(id='page_two-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page_one'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])

@app.callback(dash.dependencies.Output('page_two-content', 'children'),
              [dash.dependencies.Input('page_two-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)
