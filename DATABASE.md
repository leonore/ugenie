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

### Updating database fields

Once you've changed the fields in the `tabledef.py` file and given appropriate data for population in `readtodb.py`:

```bash
python3 tabledef.py
python3 readtodb.py
```

That will populate the database accordingly if done right.
I will be working on how to make the database more modular and sustainable by providing an interface to it that should:
- allow people to read in a file
- allow people to delete the database & repopulate it
- allow people to create a new database
- etc.

The only issue is we need to follow a general structure for the fields of the database, otherwise it won't work. I.E. fields that we will always need in the database.
This should come with working on issue #30 Making an ER diagram of the database.

---

### Some useful links:
[Refresh on SQL commands](http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm)     
[ORM with SqlAlchemy](https://pythonspot.com/orm-with-sqlalchemy/)    
[SQLAlchemy Tutorial](https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91)    
[SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
