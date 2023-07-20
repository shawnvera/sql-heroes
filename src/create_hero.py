from database.connection import execute_query, create_connection

# Create a new hero in the DB

x = input("Enter name of new hero: ")
print(x)

y = input("Enter about me: ")
print(y)

z = input("Enter biography: ")
print(z)

def create_new_hero(x, about_me, biography):
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        """
    execute_query(query, (x, about_me, biography))


create_new_hero(x, y, z)
