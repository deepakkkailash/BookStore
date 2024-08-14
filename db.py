import sqlite3




def getname(username):
    conn = sqlite3.connect('bookstore.db')
    cursor = conn.cursor()
    cursor.execute('select name from users where username = ?',(username,))
    name = cursor.fetchone()[0]
    return name
def loguserup(username,password):
    conn = sqlite3.connect('bookstore.db')
    cursor = conn.cursor()

    query = 'SELECT password from users where username=?'
    cursor.execute(query,(username,))


    value = cursor.fetchone()
    value = value[0]
    cursor.close()
    conn.commit()
    conn.close()
    if(password==value):
        return True
    else:
        print(value,password)
        return False


def signusersup(username,password,name):
    conn = sqlite3.connect('bookstore.db')
    cursor = conn.cursor()
    query = 'INSERT INTO USERS (username,password,name) values(?,?,?)'
    cursor.execute(query,(username,password,name,))
    cursor.close()
    conn.commit()
    conn.close()
    return 1


def addratingsfromuser(username,bookname,rating):
    conn = sqlite3.connect('bookstore.db')
    cursor = conn.cursor()
    try:
        cursor.execute('select * from ratings_NEW where username=? and bookname=?',(username,bookname))
        res = cursor.fetchall()
        if(len(res)==0):
            cursor.execute('INSERT INTO RATINGS_NEW (username,bookname,rating) VALUES(?,?,?)',(username,bookname,rating))
        else:
            cursor.execute('UPDATE RATINGS_NEW SET rating =? where username=? and bookname=? ',(rating,username,bookname))
        return 1
    except sqlite3.Error as e:
        print(e)
        return 0


conn = sqlite3.connect('bookstore.db')
cursor = conn.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')



