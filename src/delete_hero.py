from database.connection import execute_query, create_connection

# Delete a hero in the DB

def delete_hero():
    delete_a_hero = input("What is the name of the hero you want to delete: ")
    query = """
        DELETE FROM heroes WHERE name = (%s);
        """
    execute_query(query, (delete_a_hero,))

delete_hero()