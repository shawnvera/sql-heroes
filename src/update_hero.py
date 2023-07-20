from database.connection import execute_query, create_connection

# UPDATE the heroes table instance

update_name = input("Enter name: ")
update_about_me = input("Enter about me information: ")
update_biography = input("Enter biography information: ")
where_name = input("Enter the name of the hero you want to update: ")

def update_a_hero(name, about_me, biography, where_name):
    query = """
        UPDATE heroes
        SET name = (%s), about_me = (%s), biography = (%s)
        WHERE name = (%s);
    """
    execute_query(query, (name, about_me, biography, where_name))

update_a_hero(update_name, update_about_me, update_biography, where_name)