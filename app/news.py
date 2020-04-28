from app import app

# News
@app.route('/')
def index():

    '''
    New root page function that returns the index page and its data
    '''
    return render_template('index.html')