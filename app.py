import dash
import flask

server = flask.Flask(__name__)

# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
app = dash.Dash(
    __name__,
    server=server,
    suppress_callback_exceptions=True,
)
