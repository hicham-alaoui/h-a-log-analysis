# UDACITY Log Analysis Project

# import psycopg2 to implement DB-API
import psycopg2


# function to connect to the news database
def connect():
    return psycopg2.connect("dbname=news")

# top three articles query
articles = "select title, hits from top_three_articles limit 3"


def top_articles(articles):
    a = connect()
    c = a.cursor()
    c.execute(articles)
    counts = c.fetchall()
    for x in range(len(counts)):
        title = counts[x][0]
        hits = counts[x][1]
        print("%s| Total hits: %d" % (title, hits))
    a.close()

# top three authors query
authors = "select * from top_three_authors"


def top_authors(authors):
    b = connect()
    c = b.cursor()
    c.execute(authors)
    counts = c.fetchall()
    for y in range(len(counts)):
        name = counts[y][0]
        hits = counts[y][1]
        print("%s| Total hits:  %d" % (name, hits))
    b.close()

# more than 1% error rate query

errors = "select * from error_rate"


def error_percent(errors):
    d = connect()
    c = d.cursor()
    c.execute(errors)
    counts = c.fetchall()
    for i in range(len(counts)):
        date = counts[i][0]
        percentage = counts[i][1]
        print("%s|%.1f %%" % (date, percentage))
    d.close()

# python output statements

if __name__ == "__main__":
    print("The three articles with most hits are listed below:" + "\n")
    top_articles(articles)
    print("\n")

    print("The three authors with most hits are listed below:" + "\n")
    top_articles(authors)
    print("\n")

    print("The day when the error rate was more than 1 percent:" + "\n")
    error_percent(errors)

    
