#!/usr/bin/python3
""" main program for query logger """
import json
import psycopg2
from tabulate import tabulate

def run_queries(query):
    """connects with database runs the query and returns result
    query= sql query"""

    #connection string
    conn_string = "dbname=news"
    print("Connecting to database ->{}\n".format(conn_string))

    #connect to database
    conn = psycopg2.connect(conn_string)

    #return a cursor
    cursor = conn.cursor()

    # execute the queries and fetch reults
    print("Running query -> {}\n".format(query))
    cursor.execute(query)
    results = cursor.fetchall()

    #close connection
    conn.close()
    return results

def write_file(header, title, results):
    """writes to file called log.txt
    header = result header
    title = Question
    results = query results"""

    table = []
    for result in results:
        item = []
        item.append(str(result[0]))
        item.append(str(result[1]))
        table.append(item)

    with open('log.txt', 'a') as log_file:
        log_file.write("%s\n\n" %title)
        log_file.write(tabulate(table, header, tablefmt='presto'))
        log_file.write('\n\n')

def main():
    """ reads json file for data"""
    #read the file contents
    with open('data.json') as json_file:
        file_data = json.load(json_file)

    data = file_data['data']

    #views = file_data['views']

    # results = runQueries(data[0]['query'])
    # writeToFile(data[0]['header'],data[0]['question'],results)

    for query in data:
        results = run_queries(query['query'])
        write_file(query['header'], query['question'], results)


if __name__ == "__main__":
    main()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      