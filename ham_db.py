import sqlite3

class Database:
    def __init__(self, ham_db):
        self.conn = sqlite3.connect(ham_db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS ham (id INTEGER PRIMARY KEY, Rval text, Rlist text, Xi0val text, Xi0list text, Spin_para text, Lambda_para text, Parite_para text, Isym_para text, Iprt_para text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM ham")
        rows = self.cur.fetchall()
        return rows

    def insert(self, Rval, Rlist, Xi0val, Xi0list, Spin_para, Lambda_para, Parite_para, Isym_para, Iprt_para):
        self.cur.execute("INSERT INTO ham VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (Rval, Rlist, Xi0val, Xi0list, Spin_para, Lambda_para, Parite_para, Isym_para, Iprt_para))
        self.conn.commit()
        
    def remove(self, id):
        self.cur.execute("DELETE FROM ham WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, Rval, Rlist, Xi0val, Xi0list, Spin_para, Lambda_para, Parite_para, Isym_para, Iprt_para):
        self.cur.execute("UPDATE ham SET Rval=?, Rlist=?, Xi0val=?, Xi0list=?, Spin_para=?, Lambda_para=?, Parite_para=?, Isym_para=?, Iprt_para=? WHERE id = ?", (R, R_list, Xi0, Xi0_list, Spin_val, Lambda_para, Parite_para, Isym_para, Iprt_para, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#db = Database('store.db')        





        
