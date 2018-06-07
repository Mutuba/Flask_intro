import sqlite3
with sqlite3.connect("sample.db") as connection:
	c = connection.cursor()
	c.execute(" DROP TABLE posts")
	c.execute("CREATE TABLE posts(title TEXT, description TEXT )")
	c.execute('INSERT INTO posts VALUES("GOOD", "I\'m GOOD")')
	c.execute('INSERT INTO posts VALUES("WELL", "I\'m WELL")') 
	c.execute('INSERT INTO posts VALUES("Saturday", "Went for Burrial at Jimmy")') 