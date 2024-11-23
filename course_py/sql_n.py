import sqlite3

db = sqlite3.Connection('n.db')
db.execute("create table nums as select 2 union select 3;")

db.execute('insert into nums values (?),(?), (?);',range(4,7))
print(db.execute("select * from nums;").fetchall())
