from weppy import App


app = App(__name__)


@app.route('/hw/')
def hello_world():
    return 'Hello, world!'
