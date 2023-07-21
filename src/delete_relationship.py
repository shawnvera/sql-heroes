from database.connection import execute_query, create_connection

# Delete a relationship between characters in the DB



def delete_hero():
    delete_a_hero = input("Enter the ID of the hero1 relationship you want to delete: ")
    query = """
        DELETE FROM relationships WHERE hero1_id = (%s);
        """
    try:
        execute_query(query, (delete_a_hero,))
        print("Relationship deleted")
    except:
        print("Relationship persists, try again")

delete_hero()