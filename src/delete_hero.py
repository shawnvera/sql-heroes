from database.connection import execute_query, create_connection

# Create a new hero in the DB



def delete_hero():
    delete_a_hero = input("What is the name of the hero you want to delete: ")
    query = """
        DELETE FROM heroes WHERE name = (%s);
        """
    try:
        execute_query(query, (delete_a_hero,))
        print("Hero has been deleted")
    except:
        print("Hero wasn't deleted, try again. Make sure spelling and capitalization is correct.")

delete_hero()