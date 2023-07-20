from database.connection import execute_query, create_connection

# UPDATE the heroes table instance

i = input("What do you want to update?")
# print(i)

def update_a_hero(name, about_me, biography, sqlname):
    query = """
        UPDATE heroes
        SET name = (%s), about_me = (%s), biography = (%s)
        WHERE name = (%s);
    """
    execute_query(query, (name, about_me, biography, sqlname))

update_a_hero("Cletus", 'Very good at DND', "good", "Cletus")