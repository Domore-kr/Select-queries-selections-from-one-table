import sqlalchemy

db = 'postgresql://sqlpy51:domore9132@localhost:5432/homework_select'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

sel_album = connection.execute(
    """
    SELECT name, year_of_issue FROM album
    WHERE year_of_issue = 2018;
    """).fetchall()
print(*sel_album)

long_track = connection.execute(
    """
    SELECT name, duration FROM track
    WHERE duration = (
        SELECT MAX(duration)
        FROM track);
    """).fetchall()
print(*long_track)

three_minute_track = connection.execute(
    """
    SELECT name FROM track
    WHERE duration >= 210;
    """).fetchall()
print(*three_minute_track)

collect = connection.execute(
    """
    SELECT name FROM collection
    WHERE year_of_issue BETWEEN 2018 AND 2020;
    """).fetchall()
print(*collect)

musician = connection.execute(
    """
    SELECT name FROM musician
    WHERE name NOT LIKE '%% %%';
    """).fetchall()
print(*musician)

my_track = connection.execute(
    """
    SELECT name FROM track
    WHERE name LIKE '%%my%%';
    """).fetchall()
print(my_track)
