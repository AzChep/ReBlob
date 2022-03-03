import psycopg2
from src.data.config import config

def connect():
    con= None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        
        #lisaa('matti2', 34, 'false', cursor, con)       
        #select_all(cursor)
        #get_table(cursor, con)
        #haeSarakkeet(cursor, con)
        #haeSarakkeet2(cursor, con)
        #haeCertti(cursor, con) 
        #lisaa_certti(cursor)      
        #paivita(450, 24, cursor, con)
        #poista(cursor, con)
        #cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def select_all(cursor):
    SQL = 'SELECT * FROM Person;'
    cursor.execute(SQL)
    row = cursor.fetchall()
        
    for rivi in row:
        print(rivi)

    cursor.close()

def get_table(haettava, cursor, con):

    con = psycopg2.connect(**config())
    cursor = con.cursor()
    SQL = 'SELECT %s FROM Person;'
    data = (haettava)
    cursor.execute(SQL, data)
    row = cursor.fetchall()
 
    for rivi in row:
        print(rivi)

def haeSarakkeet(cursor, con):

    cursor.execute('Select * FROM Person LIMIT 0')
    colnames = [desc[0] for desc in cursor.description]

    print(colnames)

def haeSarakkeet2(cursor, con):

    cursor.execute('Select * FROM Certificates LIMIT 0')
    colnames = [desc[0] for desc in cursor.description]

    print(colnames)

def lisaa(name, age, student, cursor, con):

    SQL = "INSERT INTO Person (name, age, student) VALUES (%s, %s, %s);"
    data = (name, age, student)
    cursor.execute(SQL, data)
    con.commit()

def lisaa_certti(sertifikaatti, id):

    con = psycopg2.connect(**config())
    cursor = con.cursor()

    SQL = "INSERT INTO certificates (name, person_id) values (%s, %s)"
    data = (sertifikaatti, id)
    cursor.execute(SQL, data)
    con.commit()

def haeCertti(cursor, con):

    SQL = "SELECT person.name, person.id, certificates.name FROM certificates, person WHERE certificates.name = 'kebab' AND certificates.person_id = person.id;"
    cursor.execute(SQL)
    row = cursor.fetchall()

    for rivi in row:
        print(rivi)

def paivita(muutos, muutettava, cursor, con):

    SQL = "UPDATE Person SET age = %s WHERE id = %s;"
    data = (muutos, muutettava)
    cursor.execute(SQL, data)
    con.commit()

def poista(cursor, con):

    SQL = 'DELETE FROM certificates WHERE id = 2;'
    cursor.execute(SQL)
    con.commit()

if __name__ == '__main__':
    connect()