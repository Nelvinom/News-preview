from flask import render_template
from app import app

# Views
@app.route()
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular news
    popular_news = get_news('popular')
    upcoming_news = get_news('upcoming')
    now_showing_news = get_news('now_showing')
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title, popular = popular_news, upcoming = upcoming_news, now_showing = now_showing_news)