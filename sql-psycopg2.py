import psycopg2

# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# # Query 2 - select only the "Name" column form the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 form the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" form the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])

# Fetch the result (mutiple)
results = cursor.fetchall()

# Fetch the reult (single)
# results = cursor.fetchone()

# Close the connection
connection.close()

# Print results
for result in results:
    print(result)
