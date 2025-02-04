import sqlite3

def setup_database():
    conn = sqlite3.connect("loans.db")
    cursor = conn.cursor()
    
    cursor.execute(
    CREATE TABLE LoanRecords (
        amount INTEGER,
        interest INTEGER,  
        tenure INTEGER
    ))
    
    conn.commit()
    conn.close()

def insert_loan(amount, interest, tenure, emi):
    conn = sqlite3.connect("loans.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO LoanRecords (amount, interest, tenure, emi) VALUES (?, ?, ?, ?)", 
                   (amount, interest, tenure, emi))
    
    conn.commit()
    conn.close()
