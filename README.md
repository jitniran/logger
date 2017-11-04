# logger
Project for udacity log analysis
1.Create views using following sql commands

  create view populararticles as 
  select substring(path,10) as slug,count(*) as views from log
  where status like '2%' and log.path != '/'
  group by slug
  order by views desc
  limit 3;
  
  create view allrequests as select to_char(log.time,'FMMonth dd,YYYY') as date,cast(count(*) as float) as req from log
  group by date
  order by req desc;

  create view failedrequests as select to_char(log.time,'FMMonth dd,YYYY') 
  as date,count(*) as errors from log
  where status not like '2%'
  group by date
  order by errors desc;

2.run query.py using python3
3. Project uses data.json to store queries under the format:
    data['header'] = Column headers you want
    data['question'] = Natural language (english) question represent the sql query
    data['query'] = sql queries that will be run
4. optional views = [] are present to run view queries within script not enabled
5. The results are tabulated in logs.txt file
 

SQL Queries

//[popular articles]
select title,populararticles.views
from articles join populararticles
on articles.slug=populararticles.slug;

//popular authors

select authors.name,sum(views) from authors
join articles on authors.id=articles.author
join populararticles on articles.slug=populararticles.slug
group by authors.name order by sum desc;

//percent
select failedrequests.date,100.0 *(failedrequests.errors/allrequests.req) as percent from failedrequests,allrequests
where failedrequests.date=allrequests.date and 100.0*(failedrequests.errors/allrequests.req) > 1.0 order by percent;
