import dash
import dash_core_components as dcc
import dash_html_components as html
import flask

server = flask.Flask(__name__)

# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
app = dash.Dash(__name__, server=server, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


index_page = html.Div([
    dcc.Link('Go to Page 1', href='/page_one'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page_two'),
])

page_1_layout = html.Div([
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


page_2_layout = html.Div([
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

app.clientside_callback(
    """
    function(pathname) {
        if (pathname !== '/') {
            var head = document.head
            var link = document.createElement("link")

            link.type = "text/css";
            link.rel = "stylesheet";
            link.href = `/static/${pathname.substring(1)}.css`

            head.appendChild(link)
        }
    }
    """,
    dash.dependencies.Output('style-output', 'children'),
    dash.dependencies.Input('url', 'pathname')
)

# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page_one':
        return page_1_layout
    elif pathname == '/page_two':
        return page_2_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run_server(host="localhost", port=8000, debug=True)
