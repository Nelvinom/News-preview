class Config:
    '''
    General configuration parent class
    '''
     NEWS_API_WEB_URL='https://newsapi.org/v2/{}?&api_Key={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
    DEBUG = True