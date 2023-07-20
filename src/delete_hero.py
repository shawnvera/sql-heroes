from database.connection import execute_query, create_connection

# Create a new hero in the DB

def delete_hero(name):
    
    query = """
        DELETE FROM heroes WHERE name = (%s);
        """
    execute_query(query, name[1])

delete_hero("Cletus")