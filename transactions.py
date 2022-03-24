from datetime import date
import sqlite3


def to_trans_dict(trans_tuple):
    '''item, amount, category, date (yyyymmdd), description'''
    trans = {'item': trans_tuple[0], 'amount':trans_tuple[1], 'category': trans_tuple[2], 'date': trans_tuple[3], 'description':trans_tuple[4]}
    return trans

def to_trans_dict_list(trans_tuple):
    ''' convert a list of transactions tuples into a list of dictionaries'''
    return [to_trans_dict(trans) for trans in trans_tuple]

class Transaction():
    def __init__(self,dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (item text, amount INTEGER, category text, date INTEGER, description text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def select_all(self):
        ''' return all of the categories as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    def select_one(self,rowid):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * from transactions where rowid=(?)",(rowid,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict(tuples[0])
    
    def add(self,item):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions(item, amount, category, date, description) VALUES(?,?,?,?,?)",
        (item['item'],item['amount'],item['category'], item['date'], item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]
    
    def update(self,rowid,item):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''UPDATE categories
                        SET item=(?), amount=(?), category=(?),
                        date=(?), description=(?)
                        WHERE rowid=(?);
        ''',(item['item'],item['amount'],item['category'], item['date'], item['description'],rowid))
        con.commit()
        con.close()
    
    def delete(self,rowid):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE rowid=(?);
        ''',(rowid,))
        con.commit()
        con.close()
    
    def summarize_by_date(self, date):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT * from transactions WHERE date % 100=(?);''',(date,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)
    
    def summarize_by_month(self, month):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT * from transactions WHERE (date/100) % 100=(?);''',(month,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    def summarize_by_year(self, year):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT * from transactions WHERE (date/10000)=(?);''',(year,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)
    
    def summarize_by_category(self, category):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT * from transactions WHERE category=(?);''',(category,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    def summarize_by_recent_year(self, year):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT * from transactions WHERE (date/10000)>=(?);''',(year) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    def show_db(self):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT * from transactions;''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    
