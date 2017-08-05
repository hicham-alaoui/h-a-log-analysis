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
CREATE VIEW articles_by_author AS  
SELECT articles.title, count(\*) as views from articles inner join log on log.path like concat('%', articles.slug, '%') where log.status  
like '%200%' group by articles.title, log.path order by views desc limit 3";

**View for 2nd query: Who are the most popular article authors of all time?**  
CREATE VIEW articles_by_view AS  
SELECT authors.name, count(\*) as views from articles inner join authors on articles.author = authors.id inner join log on log.path like   
concat('%', articles.slug, '%') where log.status like '%200%' group by authors.name order by views desc;

**View for 3rd query: On which days did more than 1% of requests lead to errors?**  
CREATE VIEW errors AS  
SELECT day, perc from (select day, round((sum(requests)/(select count(\*) from log where substring(cast(log.time as text), 0, 11) = day)  
\* 100), 2) as perc from (select substring(cast(log.time as text), 0, 11) as day, count(\*) as requests from log where status like   
'%404%' group by day) as log\_percentage group by day order by perc desc) as final\_query where perc >= 1;


[The Github link to this repo] (https://github.com/hicham-alaoui/h-a-log-analysis) :shipit:
