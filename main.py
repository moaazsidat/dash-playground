import dash
import dash_core_components as dcc
import dash_html_components as html

import layouts.page_one as page_one
import layouts.page_two as page_two
from app import app


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


index_page = html.Div([
    dcc.Link('Go to Page 1', href='/page_one'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page_two'),
])

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
        return page_one.layout
    elif pathname == '/page_two':
        return page_two.layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run_server(host="localhost", port=8050, debug=True)
