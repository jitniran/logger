# logger
This project is used for submission in Udacity FullStack ND program, it can also be used to query a postgres database and log the results to a text file.This project uses a json file that lets you list the queries and name the column headers for sql query results

You need a postgres database set up

    sudo apt-get update
    sudo apt-get install postgresql postgresql-contrib

The installation procedure created a user account called postgres, log into account using

    sudo -i -u postgres

You will asked for normal user password and then will be given a new shell prompt for postgres

Create a database called news

    createdb news

You can use psql to connect to database and create tables

    psql news

The queries present in json file are used to query tables populated from
    
    newsdata.sql which can be downloaded from Udacity Full Stack Nanodegree Log Analysis project

Populate database using psql command

    psql -f newsdata.sql

Use data.json to store queries under the format:
    data['header'] = Column headers you want
    data['question'] = Natural language (english) question represent the sql query
    data['query'] = sql queries that will be run

Usage python3 query.py

1. Create views ind database using following sql commands

        create view populararticles as 
        select substring(path,10) as slug,count(*) as views from log
        where status like '2%' and log.path != '/'
        group by slug
        order by views desc
  
        create view allrequests as 
        select date(log.time) as date,cast(count(*)as float) as req from log
        group by date
        order by req desc;

        create view failedrequests as
        select date(log.time) as date,count(*) as errors from log
        where status not like '2%'
        group by date
        order by errors desc;

2. query.py uses tabulate,psycopg2,json install using pip
    
    pip3 install tabulate
    pip3 install psycopg2
    pip3 install json

3. Run query.py using python3

4. The results are tabulated in logs.txt file


SQL Queries

[popular articles]

    select title,populararticles.views
    from articles join populararticles
    on articles.slug=populararticles.slug
    limit 3;

[popular authors]

    select authors.name,sum(views) from authors
    join articles on authors.id=articles.author
    join populararticles on articles.slug=populararticles.slug
    group by authors.name
    order by sum desc;

[percent]

    select to_char(failedrequests.date, 'FMmonth dd, YYYY'),
    100.0 *(failedrequests.errors/allrequests.req) as percent from failedrequests,allrequests
    where failedrequests.date=allrequests.date and 100.0*(failedrequests.errors/allrequests.req) > 1.0 order by percent;
