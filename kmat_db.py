import sqlite3

class Database:
    def __init__(self, mov_db):
        self.conn = sqlite3.connect(mov_db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS halfium (id INTEGER PRIMARY KEY, Rval text, Rlist text, Xi0_val text, Xi0_list text, Z1 text, Z2 text, n text, l text, m text, nco text, nop text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM halfium")
        rows = self.cur.fetchall()
        return rows

    def insert(self, Rval, Rlist, Xi0_val, Xi0_list, Z1, Z2, n, l, m, nco, nop):
        self.cur.execute("INSERT INTO halfium VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (Rval, Rlist, Xi0_val, Xi0_list, Z1, Z2, n, l, m, nco, nop))
        self.conn.commit()
        
    def remove(self, id):
        self.cur.execute("DELETE FROM halfium WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, Rval, Rlist, Xi0_val, Xi0_list, Z1, Z2, n, l, m, nco, nop):
        self.cur.execute("UPDATE halfium SET Rval = ?, Rlist = ?, Xi0_val = ?, Xi0_list = ?,Z1 = ?, Z2 = ?, n = ?, l = ?,m = ?, nco = ?,nop = ? WHERE id = ?", (Rval, Rlist, Xi0_val, Xi0_list, Z1, Z2, n, l, m, nco, nop, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#db = Database('store.db')        





        
