### LAB 2, Part 1...  I already can push python code to my GitHub account



### LAB 2, Part 2
import sqlite3


sqlite_file = 'my_first_db.sqlite'

table_name1 = 'juggling_table'

new_field = 'Juggler'
one_field = 'Country'
two_field = 'Number of catches'

field_type = 'TEXT'
field_type_one = 'INTEGER'


def create_database():
    global conn, c, rows
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS {tn} ({nf} {ft}, {cn} {ct}, {cc}{tt})' \
              .format(tn=table_name1, nf=new_field,
                      ft=field_type, cn=one_field, ct=field_type, cc=two_field, tt=field_type_one))
    c.execute('INSERT OR IGNORE INTO juggling_table VALUES ("Ian Stewart","Canada", 94)')
    c.execute('INSERT OR IGNORE INTO juggling_table VALUES ("Aaron Gregg","Canada", 88)')
    c.execute('INSERT OR IGNORE INTO juggling_table VALUES ("Chad Taylor","USA", 78)')
    conn.commit()
    c.execute('SELECT * FROM juggling_table')
    rows = c.fetchall()
    print(rows)
    conn.close()


def main():
    create_database()
    menu()


def menu():
    global choice
    choice = int(input("\nWhat would you like to do to the database? Please type the number of your choice!\n"
                       " 1.)Add new data\n 2.)Search and update a record\n 3.)Delete a record\n"))

    if choice == 1:
        name = input("What is the name of the Chainsaw Juggling Record Holder?")
        country = input("Which country is a Juggling Record Holder from?")
        catches = int(input("How many catches it has?"))
        add_data(name,country, catches)


    if choice == 3:
        nameA = input("Which Juggling Record Holder name data would you like to delete? ")
        delete_data(nameA)




def add_data(name, country, catches):
    conn = sqlite3.connect(sqlite_file)

    c = conn.cursor()

    c.execute('INSERT OR IGNORE INTO juggling_table VALUES (?,?,?)',(name,country,catches))
    conn.commit()
    c.execute('SELECT * FROM juggling_table')

    rows = c.fetchall()
    print(rows)
    conn.close()





def delete_data(nameA):

    conn = sqlite3.connect(sqlite_file)

    c = conn.cursor()
    c.execute('DELETE FROM juggling_table WHERE Juggler = (?)', (nameA,))
    conn.commit()
    c.execute('SELECT * FROM juggling_table')
    rows = c.fetchall()
    print(rows)
    conn.close()



main()