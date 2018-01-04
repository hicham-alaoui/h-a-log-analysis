This README file outlines the steps for how to go about the FSND Udacity Logs Analysis Project.

It is assumed you are a FSND Udacity student using the VM embedded in the FSND VM and that you have Python, Vagrant and Virtualbox installed on your device.  
* Create a new folder/dir and download the newsdata folder using the link available from the project resources.
* Add vagrant to this same folder using the command vagrant init
* Run the comand vagrant up to create a VM instance: vagrant up
* Log into the new VM using the command: vagrant ssh
* CD into the vagrant dir: vagrant@vagrant: cd /vagrant
* Load the news database using the command: psql -d news -f newsdata.sql
* CD into to the News database: vagrant@vagrant:/vagrant$ cd newsdata
* Start using the news data base: vagrant@vagrant:/vagrant/newsdata$ psql news
* Now you should be in the databse directroy: news =>

After you've completed the above mentioned steps, you should be able to run the three project queries as listed below:

**View for 1st query: What are the most popular three articles of all time**  
CREATE VIEW top_three_authors AS  
select authors.name, count(articles.author) as hits from articles, log, authors where log.path = concat('/article/', articles.slug) and articles.author=authors.id group by authors.name order by hits desc limit 3;

**View for 2nd query: Who are the most popular article authors of all time?**  
CREATE VIEW top_three_articles AS  
select title, author, count(title) as hits from articles, log where log.path = concat('/article/', articles.slug) group by articles.title, articles.author order by hits desc limit 3;

**View for 3rd query: Day where error rate was over 1%**  
CREATE VIEW error_rate AS  
select day, rate from (select day, round((sum(queries)/(select count(*) from log where substring(cast(log.time as text), 0, 11) = day) * 100), 2) as rate from (select substring (cast(log.time as text), 0, 11) as day, count(*) as queries from log where status like '%4%' group by day) as query_rate  group by day order by rate desc) as error_rate where rate >= 1;

**Runing the queries in python**
After creating all the queires within the news database, now you need to quite the psql environemnt using the keyboard shortcut ctrl+d (Windows) or your own preferred method.  
You will be taken back to the newsdata directory in your vagrnat machine (vagrant@vagrant:/vagrant/newsdata$). Type python followed by space then your python file name (python log_analysis.py) then hit enter. Python will triger the process of connecting to the database and generating the query results included in the script.

[The Github link to this repo] (https://github.com/hicham-alaoui/h-a-log-analysis) :shipit:
