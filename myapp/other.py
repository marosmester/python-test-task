from django.db import connection

# --------------------------- HELPER FUNCTIONS ------------------------------

def choose_id():
    '''
    Finds all the IDs that are already in the database and returns valid (unique) one.
    :retunrs: A valid post ID [int]
    '''
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM myapp_blogpost", [])
        rows = cursor.fetchall()

    ids = []
    for entry in rows:
        ids.append(entry[3])

    cnt = 1 
    while cnt in ids:
        cnt+= 1

    return cnt

# --------------------------- HELPER FUNCTIONS ------------------------------
