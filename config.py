import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8753755010:AAHjR-nD3AUXKOPzsBxO82eRud7pfzK0jt8")
    API_ID = int(os.environ.get("API_ID", "28854523"))
    API_HASH = os.environ.get("API_HASH", "3ec8779aa2109cfa00fd6146146a065c")
    AUTH_USER = os.environ.get('AUTH_USERS', '1018181607').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = os.environ.get("CREDIT", "Sujeet™")
