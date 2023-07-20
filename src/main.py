from database.connection import execute_query, create_connection

def select_all_heroes():
    query = """
        SELECT * from heroes;
    """
    returned_items = execute_query(query).fetchall
    for item in returned_items:
        print(item[1])
    return returned_items
 
select_all_heroes()

# def create_new_hero(name, about_me, biography):
#     query = """
#         INSERT INTO heroes (name, about_me, biography)
#         VALUES (%s, %s, %s)
#         """
#     execute_query(query, (name, about_me, biography))