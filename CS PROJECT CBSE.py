import mysql.connector as sqltor
import tkinter as tk
mycon=sqltor.connect(host="localhost",user="root",passwd="s1234",database="library_management_system")
if mycon.is_connected()==False:
    print("Connection unsuccessful")
cursor=mycon.cursor()

var=True

def add_book():
    global mw
    mw.destroy()
    def add():
    
        title = en1.get()
        author = en2.get()
        available_copies = int(en3.get())
        mw.destroy()
        cmd="INSERT INTO Books (title, author, available_copies) VALUES ('{}','{}',{})".format(title, author, available_copies)
        cursor.execute(cmd)
        book_id = cursor.lastrowid
        mycon.commit()
        print("Book added successfully.")
        print("Book ID is",book_id)
        
    mw=tk.Tk()
    mw.title("Add Book")
    lb=tk.Label(text="ADD BOOK",height=2,font=("Consolas",23,"bold"),width=30,bg="#3E14CA")
    lb.grid(row=0,column=0)
    lb=tk.Label(text="Enter Book Title",height=2,font=("Consolas",23,"bold"),width=30,bg="#1296E8")
    lb.grid(row=1,column=0)
    en1=tk.Entry(font=("Consolas",23,"bold"),width=30,bg="#56E812")
    en1.grid(row=2,column=0)
    lb1=tk.Label(text="Enter Author",height=2,font=("Consolas",23,"bold"),width=30,bg="#1296E8")
    lb1.grid(row=3,column=0)
    en2=tk.Entry(font=("Consolas",23,"bold"),width=30,bg="#56E812")
    en2.grid(row=4,column=0)
    lb1=tk.Label(text="Enter Available Copies",height=2,font=("Consolas",23,"bold"),width=30,bg="#1296E8")
    lb1.grid(row=5,column=0)
    en3=tk.Entry(font=("Consolas",23,"bold"),width=30,bg="#56E812")
    en3.grid(row=6,column=0)
    btn=tk.Button(text="Add",command=add,height=1,font=("Consolas",23,"bold"),width=30,bg="#ECA81E")
    btn.grid(row=7,column=0)
    mw.mainloop()


def add_member():
    global mw
    mw.destroy()
    def add():
        name = en1.get()
        classs = int(en2.get())
        section = en3.get()
        mw.destroy()
        cmd="INSERT INTO Members (name, class, section) VALUES ('{}',{},'{}')".format(name,classs,section)
        cursor.execute(cmd)
        member_id = cursor.lastrowid
        mycon.commit()
        print("Member added successfully.")
        print("Member ID is",member_id)

    mw=tk.Tk()
    mw.title("Add Member")
    lb=tk.Label(text="ADD MEMBER",height=2,font=("Consolas",23,"bold"),width=30,bg="#3E14CA")
    lb.grid(row=0,column=0)
    lb=tk.Label(text="Enter Member Name",height=2,font=("Consolas",23,"bold"),width=30,bg="#1296E8")
    lb.grid(row=1,column=0)
    en1=tk.Entry(font=("Consolas",23,"bold"),width=30,bg="#56E812")
    en1.grid(row=2,column=0)
    lb1=tk.Label(text="Enter Class",height=2,font=("Consolas",23,"bold"),width=30,bg="#1296E8")
    lb1.grid(row=3,column=0)
    en2=tk.Entry(font=("Consolas",23,"bold"),width=30,bg="#56E812")
    en2.grid(row=4,column=0)
    lb1=tk.Label(text="Enter Section",height=2,font=("Consolas",23,"bold"),width=30,bg="#1296E8")
    lb1.grid(row=5,column=0)
    en3=tk.Entry(font=("Consolas",23,"bold"),width=30,bg="#56E812")
    en3.grid(row=6,column=0)
    btn=tk.Button(text="Add",command=add,height=1,font=("Consolas",23,"bold"),width=30,bg="#ECA81E")
    btn.grid(row=7,column=0)
    mw.mainloop()
    

def view_books():
    
    mw.destroy()
    
    cursor.execute("SELECT * FROM Books")
    rows = cursor.fetchall()
    print("_"*130)
    print()
    print(" "*15,"TITLE"," "*75,"AUTHOR")
    print("_"*130)
    print()
    for row in rows:
        l=90-len(row[1])
        print(" "*3,row[1]," "*l,row[2])

    print("_"*130)
    

def view_members():
    
    mw.destroy()
    
    cursor.execute("SELECT * FROM Members")
    rows = cursor.fetchall()
    print("_"*130)
    print()
    print(" "*7,"NAME"," "*30,"CLASS"," "*30,"SECTION")
    print("_"*130)
    print()
    for row in rows:
        l=40-len(row[1])
        print(" "*3,row[1]," "*l,row[2]," "*33,row[3])

    print("_"*130)
    
    
    

def borrow_book():
    global mw
    mw.destroy()
    def borrow():
        member_id = int(en1.get())
        book_id = int(en2.get())
        mw.destroy()
        cmd="SELECT available_copies FROM Books WHERE book_id ={}".format(book_id)
        cursor.execute(cmd)
        available_copies = cursor.fetchone()
        if available_copies:
            
            if available_copies[0] > 0:
                try:
                    cmd="INSERT INTO Transactions (book_id, member_id, borrow_date) VALUES ({},{},CURDATE())".format (book_id, member_id)
                    cursor.execute(cmd)
                    transaction_id = cursor.lastrowid
                    cmd="UPDATE Books SET available_copies = available_copies - 1 WHERE book_id ={}".format(book_id)
                    cursor.execute(cmd)
                    mycon.commit()
                    print("Book borrowed successfully.")
                    print("Transaction ID is",transaction_id)
                except:
                    print("Invalid Member ID")
                
                
            else:
                print("Book not available.")
        else:
            print("Invalid Book ID")


    mw=tk.Tk()
    mw.title("Borrow Book")
    lb=tk.Label(text="BORROW BOOK",height=2,font=("Consolas",23,"bold"),width=30,bg="#3E14CA")
    lb.grid(row=0,column=0)
    lb=tk.Label(text="Enter Member ID",height=2,font=("Consolas",23,"bold"),width=30,bg="#1296E8")
    lb.grid(row=1,column=0)
    en1=tk.Entry(font=("Consolas",23,"bold"),width=30,bg="#56E812")
    en1.grid(row=2,column=0)
    lb1=tk.Label(text="Enter Book ID",height=2,font=("Consolas",23,"bold"),width=30,bg="#1296E8")
    lb1.grid(row=3,column=0)
    en2=tk.Entry(font=("Consolas",23,"bold"),width=30,bg="#56E812")
    en2.grid(row=4,column=0)
    btn=tk.Button(text="Borrow",command=borrow,height=1,font=("Consolas",23,"bold"),width=30,bg="#ECA81E")
    btn.grid(row=5,column=0)
    mw.mainloop()    
    
    

def return_book():
    global mw
    mw.destroy()
    def return_():
        transaction=()
        transaction_id = int(en1.get())
        mw.destroy()
        cmd="SELECT * FROM Transactions WHERE transaction_id ={}".format(transaction_id)
        cursor.execute(cmd)
        transaction = cursor.fetchone()
       
        if transaction:
            if transaction[4]==None:
                book_id = transaction[1]
                cmd="UPDATE Transactions SET return_date = CURDATE() WHERE transaction_id ={}".format(transaction_id)
                cursor.execute(cmd)
                cmd="UPDATE Books SET available_copies = available_copies + 1 WHERE book_id ={}".format(book_id)
                cursor.execute(cmd)
                mycon.commit()
                print("Book returned successfully.")
            else:
                print("Book already returned.")
        else:
            print("Transaction not found.")

    mw=tk.Tk()
    mw.title("Return Book")
    lb=tk.Label(text="RETURN BOOK",height=2,font=("Consolas",23,"bold"),width=30,bg="#3E14CA")
    lb.grid(row=0,column=0)
    lb=tk.Label(text="Enter Transaction ID",height=2,font=("Consolas",23,"bold"),width=30,bg="#1296E8")
    lb.grid(row=1,column=0)
    en1=tk.Entry(font=("Consolas",23,"bold"),width=30,bg="#56E812")
    en1.grid(row=2,column=0)
    btn=tk.Button(text="Return",command=return_,height=1,font=("Consolas",23,"bold"),width=30,bg="#ECA81E")
    btn.grid(row=3,column=0)
    mw.mainloop()
    
    

def check_book_status():
    global mw
    mw.destroy()

    def book():
        book_id = int(en1.get())
        mw.destroy()
        cmd="SELECT title, available_copies FROM Books WHERE book_id ={}".format(book_id)
        cursor.execute(cmd)
        book = cursor.fetchone()

        if book:
            title, available_copies = book
            if available_copies > 0:
                print("'{}' is available. Copies available:'{}'.".format(title,available_copies))
            else:
                print("'{}' is currently checked out.".format(title))
        else:
            print("Book not found.")


    mw=tk.Tk()
    mw.title("Book Status")
    lb=tk.Label(text="CHECK BOOK STATUS",height=2,font=("Consolas",23,"bold"),width=30,bg="#3E14CA")
    lb.grid(row=0,column=0)
    lb=tk.Label(text="Enter Book ID to check status",height=2,font=("Consolas",23,"bold"),width=30,bg="#1296E8")
    lb.grid(row=1,column=0)
    en1=tk.Entry(font=("Consolas",23,"bold"),width=30,bg="#56E812")
    en1.grid(row=2,column=0)
    btn=tk.Button(text="Check",command=book,height=1,font=("Consolas",23,"bold"),width=30,bg="#ECA81E")
    btn.grid(row=3,column=0)
    mw.mainloop()
    
def exit_():
    global var
    mw.destroy()
    var=False
    print("Thank You!")


while var:
    
    mw=tk.Tk()
    mw.configure(bg="#5483FA")
    mw.title("Library Management System")
    ttl=tk.Label(text="LIBRARY MANAGEMENT SYSTEM",font=("Consolas",30,"bold"),bg="#5483FA")
    ttl.grid(row=0,column=0)
    wel=tk.Label(text="Welcome!",font=("Consolas",25,"bold"),bg="#5483FA")
    wel.grid(row=1,column=0)
    play=tk.Button(text="Add Book",width=50,height=1,font=("Consolas",23,"bold"),command=add_book,bg="#C812EC")
    play.grid(row=2,column=0,padx=10,pady=10,sticky="nsew")

    play=tk.Button(text="Add Member",width=50,height=1,font=("Consolas",23,"bold"),command=add_member,bg="#E10BA7")
    play.grid(row=3,column=0,padx=10,pady=10,sticky="nsew")

    play=tk.Button(text="View Books",width=50,height=1,font=("Consolas",23,"bold"),command=view_books,bg="#FAB439")
    play.grid(row=4,column=0,padx=10,pady=10,sticky="nsew")

    play=tk.Button(text="View Members",width=50,height=1,font=("Consolas",23,"bold"),command=view_members,bg="#5DAB13")
    play.grid(row=5,column=0,padx=10,pady=10,sticky="nsew")

    play=tk.Button(text="Borrow Book",width=50,height=1,font=("Consolas",23,"bold"),command=borrow_book,bg="#DBC714")
    play.grid(row=6,column=0,padx=10,pady=10,sticky="nsew")

    play=tk.Button(text="Return Book",width=50,height=1,font=("Consolas",23,"bold"),command=return_book,bg="#1060C8")
    play.grid(row=7,column=0,padx=10,pady=10,sticky="nsew")

    play=tk.Button(text="Check Book Status",width=50,height=1,font=("Consolas",23,"bold"),command=check_book_status,bg="#E555AE")
    play.grid(row=8,column=0,padx=10,pady=10,sticky="nsew")

    play=tk.Button(text="Exit",width=50,height=1,font=("Consolas",23,"bold"),command=exit_,bg="#DB4949")
    play.grid(row=9,column=0,padx=10,pady=10,sticky="nsew")

    mw.mainloop()


                                  
