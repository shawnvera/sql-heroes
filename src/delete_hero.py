from database.connection import execute_query, create_connection

# Create a new hero in the DB

delete_a_hero = input("What is the name of the hero you want to delete: ")

def delete_hero(delete_a_hero):
    
    query = """
        DELETE FROM heroes WHERE name = (%s);
        """
    execute_query(query, delete_a_hero)

delete_hero(delete_a_hero)