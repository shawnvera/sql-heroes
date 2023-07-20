from database.connection import execute_query, create_connection

# Create a new hero in the DB


def create_new_hero(name, about_me, biography):
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        """
    execute_query(query, (name, about_me, biography))


create_new_hero("Cletus", "Very good and DND", "Words that describe Cletus")
