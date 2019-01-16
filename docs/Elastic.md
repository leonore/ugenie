### Installing and starting Elastic on your computer
Follow the [official tutorial](https://www.elastic.co/guide/en/elasticsearch/reference/2.4/_installation.html)

### Running Elasticsearch in the background
on macOS:
```brew services start elasticsearch```
on other os:
[official tutorial](https://www.elastic.co/guide/en/elasticsearch/reference/current/starting-elasticsearch.html)

### Populating the database
```python load_questions.py
python populate_elastic.py```

Database queries are stored as functions in elastic-db/functions.py

------

REFERENCES          

##### Quick links
* [Elasticsearch official reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
* [Delete an index](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-delete-index.html)
* [elasticsearch github](https://github.com/elastic/elasticsearch)
   1. setting up
   2. upgrading
   3. general interaction guidelines
* [Updating documents](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-update-documents.html)
* [Importing JSON files with Bulk API](https://stackoverflow.com/questions/42623636/import-list-of-dicts-or-json-file-to-elastic-search-with-python)

##### Tutorial links

* [ES with Python](https://medium.com/the-andela-way/getting-started-with-elasticsearch-python-part-two-1c0c9d1117ea)
  1. Adding documents
  2. Retrieving documents
  3. Updating documents
  4. Deleting documents
 * [ES with Python 2](http://nitin-panwar.github.io/Elasticsearch-tutorial-for-beginners-using-Python/)
   1. Same as 1-4 above
   2. Searching
* [ES with Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-full-text-search)
    1. Setting up ES with Flask
    2. Search queries
* [Getting started with ES](https://tryolabs.com/blog/2015/02/17/python-elasticsearch-first-steps/)
     1. Includes search queries
* [Practical introduction to ES with Python](https://www.elastic.co/blog/a-practical-introduction-to-elasticsearch) !! TO READ
* [Better queries](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-multi-match-query.html) !! TO READ

##### Integration
* [Using ES with Flask](https://dev.to/aligoren/using-elasticsearch-with-python-and-flask-2i0e)