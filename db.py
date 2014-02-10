import MySQLdb
import hashlib
import simplejson as json


# Debugging function to pretty print json
def pretty_print(json_string):
    s = json.dumps(json_string, indent=4 * ' ')
    print '\n'.join([l.rstrip() for l in  s.splitlines()])



# Generic function to execute a stored procedure
def exec_proc(proc, *args):
    db = MySQLdb.connect("174.74.50.196", "remote", "mountaindew", "sentiment_analysis")
    curs = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        curs.callproc(proc, args)
        rs = curs.fetchall()
        rc = curs.rowcount
    except MySQLdb.DatabaseError as er:
        return False, er
    finally:
        curs.close()
        db.close()
    return rc, rs
