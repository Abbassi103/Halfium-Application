import sqlite3

class Database:
    def __init__(self, bas_db):
        self.conn = sqlite3.connect(bas_db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Bas (id INTEGER PRIMARY KEY, Rval text, Rlist text, Xi0val text, Xi0list text, Spin_para text, Lambda_para text, Parite_para text, Isym_para text, Mol_sym text, Nbas_max text, Open_func text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM Bas")
        rows = self.cur.fetchall()
        return rows

    def insert(self, Rval, Rlist, Xi0val, Xi0list, Spin_para, Lambda_para, Parite_para, Isym_para, Mol_sym, Nbas_max, Open_func):
        self.cur.execute("INSERT INTO Bas VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (Rval, Rlist, Xi0val, Xi0list, Spin_para, Lambda_para, Parite_para, Isym_para, Mol_sym, Nbas_max, Open_func))
        self.conn.commit()
        
    def remove(self, id):
        self.cur.execute("DELETE FROM Bas WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, Rval, Rlist, Xi0val, Xi0list, Spin_para, Lambda_para, Parite_para, Isym_para, Mol_sym, Nbas_max, Open_func):
        self.cur.execute("UPDATE Bas SET Rval=?, Rlist=?, Xi0val=?, Xi0list=?, Spin_para=?, Lambda_para=?, Parite_para=?, Isym_para=?, Mol_sym=?, Nbas_max=?, Open_func=? WHERE id = ?", (R, R_list, Xi0, Xi0_list, Spin_val, Lambda_para, Parite_para, Isym_para, Mol_sym, Nbas_max, Open_func, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#db = Database('store.db')        





        
