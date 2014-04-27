from db_access import db, sa

def test():
    # Get connection object and create a cursor object
    conn = db.get_conn_obj()
    curs = conn.cursor()
    
    # These are the cursor arguments
    sentiment = "sentiment"
    length = 10
    weight = 23.45
    type = "type"
    
    # Create a new cluster
    curs.execute(sa.sql_insert_cluster, (sentiment, length, weight, type))
    # Get the cluster id of the cluster we just created
    last_cluster_id = curs.lastrowid
    print last_cluster_id
    
    # a test sentence id to insert into the cluster
    sentence_id = 965
    
    curs.execute(sa.sql_update_sentence_cluster, (last_cluster_id, sentence_id))
    
    # At this point, you could change the value of sentence_id and then call the above statement again
    # and continue adding sentences in the cluster. Additionally you could change the variables for the cluster
    # and simply call the insert cluster statement again and retrieve the new cluster id, same way as before.
    
    
    # Commit changes. Only after calling this will any changes take effect in the database
    conn.commit()
    
    curs.close()
    conn.close()