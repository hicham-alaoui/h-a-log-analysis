#!/usr/bin/env python

import psycopg2


def connect(dbname="news"):
    """Connect to PostgreSQL database."""
    try:
        db = psycopg2.connect("dbname={}".format(dbname))
        c = db.cursor()
        return db, c
    except:
        print("Oops! error in connecting to databse.")


def most_popular_articles():
    """Query for most popular three articles"""
    db, c = connect()
    articles_query = "select * from top_three_articles limit 3"
    c.execute(articles_query)
    counts = c.fetchall()
    for x in range(len(counts)):
            title = counts[x][0]
            hits = counts[x][1]
            print("%s| Total hits: %d" % (title, hits))

def most_popular_authors():
    """Query for most popular authors"""
    db, c = connect()
    authors_query = "select * from top_three_authors"
    c.execute(authors_query)
    counts = c.fetchall()
    for y in range(len(counts)):
        name = counts[y][0]
        hits = counts[y][1]
        print("%s| Total hits:  %d" % (name, hits))

def error_percent():
    """Query for day with error rate higher than 1%"""
    db, c = connect()
    errors_query = "select * from error_rate"
    c.execute(errors_query)
    counts = c.fetchall()
    for i in range(len(counts)):
        date = counts[i][0]
        percentage = counts[i][1]
        print("%s|%.1f %%" % (date, percentage))




if __name__ == "__main__":
    print("The three articles with most hits are listed below:")
    most_popular_articles()
    print("\n")

    print("The three authors with most hits are listed below:")
    most_popular_authors()
    print("\n")  

    print("The day when the error rate was more than 1 percent:")
    error_percent()

 print "\nAll done!\n"
