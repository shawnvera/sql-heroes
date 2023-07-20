from database.connection import execute_query, create_connection

# UPDATE the heroes table instance

def update_a_hero(name, about_me, biography):
    query = """
        UPDATE heroes
        SET name = (%s), about_me = (%s), biography = (%s)
        WHERE name = (%s);
    """
    execute_query(query, (name, about_me, biography))

update_a_hero('Cletus','Very good at DND', 'Words that describe Cletus')