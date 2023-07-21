from database.connection import execute_query, create_connection

# Create a new hero in the DB

def create_new_hero():
    x = input("Enter name of new hero: ")
    y = input("Enter about me: ")
    z = input("Enter biography: ")

    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        """
    try:
        execute_query(query, (x, y, z))
        print("New hero created!")
    except:
        print("Something went wrong, probably due to an archnemesis. Try again.")


create_new_hero()
