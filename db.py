import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS employeees(
            id Integer Primary key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, age, doj, email, gender, contact, address):
        self.cur.execute("insert into employeees values (NULL,?,?,?,?,?,?,?)",(name, age, doj, email, gender, contact, address))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from employeees")
        rows=self.cur.fetchall()
        #print(rows)
        return rows

    # Delete a Record in DB
    def remove(self,id):
        self.cur.execute("delete from employeees where id=?",(id,))
        self.con.commit()


    # Update a Record in DB
    def update(self,id,name, age, doj, email, gender, contact, address):
        self.cur.execute("update employeees set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=?",
                         (name, age, doj, email, gender, contact, address,id))
        self.con.commit()


