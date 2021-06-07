
from config import r
from config import db
from config import date_key
from datetime import datetime


def db_initialize(x):
    wsb_sub = r.subreddit("wallstreetbets").hot(limit=x)
    cursor = db.cursor()

    print(submission.title)


def p_test():
    wsb_sub = r.subreddit("wallstreetbets").hot(limit=1)

    print(dir(wsb_sub))
    for item in wsb_sub:
        print(item.comments)

if __name__ == '__main__':
    # db_initialize()

    # db.close()
    p_test()