from database.connection import execute_query, create_connection

# Read the heroes table

def select_all_heroes():
    query = """
        SELECT * from heroes;
    """
    returned_items = execute_query(query).fetchall
    for item in returned_items:
        print(item[1])
    return returned_items
 
select_all_heroes()

