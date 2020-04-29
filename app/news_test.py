import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()
    
We import theUnittest module and the news module. We then get the Newsclass which we will create.

We then create a test class and inside we define a setUp() method. This will instantiate our News class to make the self.new_news object. We pass in six arguments.

We then define a test case test_instance that uses the isinstance() function that checks if the object self.new_news is an instance of the News class.

Make sure the test is failing. We then can add code to make the code work

models/news.py

class News:
    '''
    News class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count