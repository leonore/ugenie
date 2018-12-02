## Using the Bot-Runner database

### Installing dependencies on your own machine:

```bash
# they are already installed on the VM
pip install sqlalchemy
pip install sqlalchemy-utils
```
---

### Using MySQL on the command line
```bash
mysql -u root -p
password: ****
mysql> use database_name; # e.g. courses_test
mysql> show tables;
mysql> describe table_name; # e.g. short
mysql> exit # see link below for more SQL commands
```

---

### ⚠ Updating the database ⚠     
right now, if the database schema is updated, you need to drop(:delete) the database, initialise the tables, and populate them again, that is:
```bash
mysql -u root -p
password: ****
mysql> drop database database_name; exit;
python3 tabledef.py
python3 readtodb.py
```

This is obviously something that should be changed. 

---

### Some useful links:
[Refresh on SQL commands](http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm)     
[ORM with SqlAlchemy](https://pythonspot.com/orm-with-sqlalchemy/)    
[SQLAlchemy Tutorial](https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91)    
[SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
