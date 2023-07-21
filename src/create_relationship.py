from database.connection import execute_query, create_connection

# Create a new relationship between heroes/enemies in the DB

def create_new_hero():
    x = input("Enter the ID of the first hero: ")

    y = input("Enter the ID of the second hero: ")
    z = input("Enter 1 for \"Friends\" or 2 for \"Enemies\": ")

    query = """
        INSERT INTO relationships (hero1_id, hero2_id, relationship_type_id)
        VALUES (%s, %s, %s)
        """
    try:
        execute_query(query, (x, y, z))
        print("New relationship created!")
    except:
        print("Something went wrong, try again.")


create_new_hero()