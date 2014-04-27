import MySQLdb
import hashlib
import simplejson as json
from sa_settings import DatabaseConnection as db_settings

# Debugging function to pretty print JSON
def _pretty_print(json_string):
    s = json.dumps(json_string, indent=4 * ' ')
    print '\n'.join([l.rstrip() for l in  s.splitlines()])


# Generic function to execute a stored procedure
def exec_proc(proc, *args):
    db = MySQLdb.connect(db_settings.host, db_settings.user, db_settings.password, db_settings.db_name)
    curs = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        curs.callproc(proc, args)
        rs = curs.fetchall()
        rc = curs.rowcount
    except MySQLdb.DatabaseError as er:
        print er # change to email
        return False, False
    finally:
        curs.close()
        db.close()
    return rc, rs
    
def get_conn_obj():
    return MySQLdb.connect(db_settings.host, db_settings.user, db_settings.password, db_settings.db_name)

# Generic function to execute a query
def exec_query(query):
    db = MySQLdb.connect(d.host, d.user, d.password, d.db_name)
    curs = db.cursor(MySQLdb.cursors.DictCursor)
    db.query(query)
    return db.store_result()

