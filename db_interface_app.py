import logging
import db_gui

import sqlite3
from sqlite3 import Error

import mysql.connector
from mysql.connector import Error

def window_load_menu():
    # Creating Menubar 
    menubar = db_gui.tk.Menu(db_gui.window) 
      
    # Adding File Menu and commands 
    file = db_gui.tk.Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='File', menu = file) 
    file.add_command(label ='Open...', command = open_file_dialog)
    file.add_command(label ='Close', command = None)     
    file.add_command(label ='Save As...', command = None)
    file.add_command(label ='Rename...', command = None)     
    file.add_separator()
    file.add_command(label ='Print...', command = None)
    file.add_separator()    
    file.add_command(label ='Exit', command = db_gui.window.destroy) 

    # Adding Edit Menu and commands 
    edit = db_gui.tk.Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='Edit', menu = edit) 
    edit.add_command(label ='Cut', command = None) 
    edit.add_command(label ='Copy', command = None) 
    edit.add_command(label ='Paste', command = None) 
    edit.add_command(label ='Select All', command = None) 
    edit.add_separator() 
    edit.add_command(label ='Find...', command = None) 
    edit.add_command(label ='Find again', command = None) 

    # Adding Connection Menu and commands 
    connection = db_gui.tk.Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='Connection', menu = connection) 
    connection.add_command(label ='SQLite', command = None) 
    connection.add_command(label ='MySQL', command = None) 
    connection.add_command(label ='Postgres', command = None) 

    # Adding DDL Menu and commands 
    ddl = db_gui.tk.Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='DDL', menu = ddl) 
    ddl.add_command(label ='Create Table', command = None) 
    ddl.add_command(label ='Drop Table', command = None) 
    
    dml = db_gui.tk.Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='DML', menu = dml)
    dml.add_command(label ='Select', command = retrieve_frame)
    dml.add_command(label ='Insert', command = insert_frame) 
    dml.add_command(label ='Update', command = None) 
    dml.add_command(label ='Delete', command = None)
    
    # Adding Help Menu 
    help_ = db_gui.tk.Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='Help', menu = help_) 
    help_.add_command(label ='About', command = None)
    
    db_gui.window.config(menu = menubar)

def display_errmsg(errmsg):
    db_gui.lbl_errmsg.config(text=errmsg, font=("Arial Bold", 10), anchor="center")
    db_gui.lbl_errmsg.grid(column=3,row=12, sticky='nsew')
    logging.error(f'{errmsg}')
    raise Exception (f'{errmsg}')

def startup_splash_frame():
    """ Display initial (splash) screen at app startup """
    
    db_gui.frm_frame1.grid(column=0, row=0)
    db_gui.frm_buttons.grid(column=0, row=1)

    myimage = db_gui.tk.PhotoImage(file='X:\\EDWARD\\ITTrain\\Python\\Builds\\DBInterface\\datbase_icon.gif')
    appdisplay = db_gui.ttk.Label(db_gui.frm_frame1, image=myimage)
    appdisplay.image = myimage
    appdisplay.grid(column=1, row=1)

    db_gui.btn_exit.config(command=exitprg)
    db_gui.btn_exit.pack(side="right")
    #db_gui.btn_exit.grid(column=9, row=2, sticky=('e','w') )
 
    db_gui.frm_splash_visible = True

def reload_splash_frame():
    """ Redisplay the splash screen when [Home] button is pressed """
    
    if db_gui.frm_splash_visible:
        print('do nothing')
        return
    elif db_gui.frm_retrieve_visible or db_gui.frm_insert_visible:
        widget_forget(db_gui.frm_frame2)
        db_gui.frm_retrieve_visible = False
        db_gui.frm_insert_visible = False
    
        db_gui.frm_frame1.grid(column=0, row=0)
        db_gui.frm_buttons.grid(column=0, row=1)

        myimage = db_gui.tk.PhotoImage(file='X:\\EDWARD\\ITTrain\\Python\\Builds\\DBInterface\\datbase_icon.gif')
        appdisplay = db_gui.ttk.Label(db_gui.frm_frame1, image=myimage)
        appdisplay.image = myimage
        appdisplay.grid(column=1, row=1)

        db_gui.btn_exit.config(command=exitprg)
        db_gui.btn_exit.pack(side="right")
        #db_gui.btn_exit.grid(column=9, row=2, sticky=('e','w') )
     
        db_gui.frm_splash_visible = True
    
def retrieve_frame():
    """ Display retrieve/select frame when [Select] option is selected on menu """
    
    if db_gui.frm_splash_visible:
        widget_forget(db_gui.frm_frame1)
        db_gui.frm_splash_visible = False
        
        db_gui.frm_frame2.grid(column=0, row=0, padx=50, pady=50, sticky=("N", "W", "E", "S"))

        db_gui.lbl_dbtype_select.grid(column=3, row=1, padx=5, sticky="W")
        db_gui.dbtype_choosen.grid(column=3, row=2, padx=5, sticky="W")
        
        db_gui.lbl_table_retrieve.grid(column=3, row=3, padx=5, sticky="W")
        db_gui.tblname_entry.grid(column=3, row=4, padx=5, sticky=("W", "E"))

        db_gui.lbl_result_text.grid(column=3, row=6, padx=5, sticky="W")    
        db_gui.result_text.grid(column=3, row=7, padx=5, sticky=("W", "E"))
        
    elif db_gui.frm_insert_visible:
        db_gui.tblname_entry.config(state=db_gui.tk.NORMAL)
        db_gui.frm_insert_visible = False
        
        db_gui.lbl_result_text.config(text="Result from Select is:")
        db_gui.result_text.grid(column=3, row=7, padx=5, sticky=("W", "E"))  
    
    else:
        None
    
    db_gui.btn_home.config(command=reload_splash_frame)
    db_gui.btn_home.pack(side="left")
    
    db_gui.btn_retrieve.config(command=select_retrieve)
    db_gui.btn_retrieve.pack(side="right")
    
    db_gui.btn_insert.config(command=insert_data)
    db_gui.btn_insert.pack(side="right")
    
    db_gui.btn_update.pack(side="right")
    db_gui.btn_delete.pack(side="right")

    db_gui.btn_writefile.config(command=write_to_file)
    db_gui.btn_writefile.pack(side="right")
    db_gui.btn_readfile.pack(side="right")
    
    db_gui.frm_retrieve_visible = True

def insert_frame():
    """ Display frame for inserting when [Insert] is selected on menu """
    
    if db_gui.frm_splash_visible:
        widget_forget(db_gui.frm_frame1)
        db_gui.frm_splash_visible = False
        
        db_gui.frm_frame2.grid(column=0, row=0, padx=25, pady=25, sticky=("N", "W", "E", "S"))

        db_gui.lbl_dbtype_select.grid(column=3, row=1, padx=5, sticky="W")
        db_gui.dbtype_choosen.grid(column=3, row=2, padx=5, sticky="W")
        
        db_gui.lbl_table_retrieve.grid(column=3, row=3, padx=5, sticky="W")
        db_gui.tblname_entry.config(state=db_gui.tk.DISABLED)
        db_gui.tblname_entry.grid(column=3, row=4, padx=5, sticky=("W", "E"))

        db_gui.lbl_result_text.config(text="Please provide insert statement")
        db_gui.lbl_result_text.grid(column=3, row=6, padx=5, sticky="W")    
        db_gui.result_text.grid(column=3, row=7, padx=5, sticky=("W", "E"))
        
        
    elif db_gui.frm_retrieve_visible:
        db_gui.tblname_entry.config(state=db_gui.tk.DISABLED)
        db_gui.frm_retrieve_visible = False
        
        db_gui.lbl_dbtype_select.grid(column=3, row=1, padx=5, sticky="W")
        db_gui.dbtype_choosen.grid(column=3, row=2, padx=5, sticky="W")
        
        db_gui.lbl_result_text.config(text="Please provide insert statement")
        db_gui.result_text.grid(column=3, row=7, padx=5, sticky=("W", "E"))
       
    else:
        None
    
    db_gui.btn_home.pack(side="left")
    
    db_gui.btn_retrieve.config(command=select_retrieve)
    db_gui.btn_retrieve.pack(side="right")
    
    db_gui.btn_insert.config(command=insert_data)
    db_gui.btn_insert.pack(side="right")
    
    db_gui.btn_update.pack(side="right")
    db_gui.btn_delete.pack(side="right")

    db_gui.btn_writefile.config(command=write_to_file)
    db_gui.btn_writefile.pack(side="right")
    db_gui.btn_readfile.pack(side="right")
    
    db_gui.frm_insert_visible = True

def open_file_dialog():

    db_gui.window.filename = db_gui.filedialog.askopenfilename(initialdir="X:\EDWARD\ITTrain\Python\Python_DBConnect", title="Select A File", filetypes=(("sql files", "*.sql"), ("all files", "*.*")))

    with open(db_gui.window.filename, 'r') as file:
        filecontents = file.readlines()
        db_gui.result_text.insert(1.0, filecontents)

        
def write_file_selected():
    
    db_gui.lbl_filename.config(text='Please provide name of file')
    db_gui.lbl_filename.grid(column=5, row=6, sticky='w')
    
    db_gui.ent_filename.grid(column=5, row=7, sticky='nw')

def write_to_file():
    
    w_filename = db_gui.ent_filename.get()
    
    with open(w_filename, 'w') as file:
        result = db_gui.result_text.get("1.0", "end")
        file.write(result)
              
    print(result)
    
    print('number of lines:' + str(db_gui.result_text.index('end')))
    numoflines = db_gui.result_text.index('end')
    lines_list = numoflines.split(".")
    total_lines = lines_list[0]
    print(total_lines)
    count = 1
    
    for line in result.split('\n'):
        print('line is: ' + line)
    
def create_sqlite_connection():
    """ Make connection to sqlite database """
    
    connection = None
    try:
        connection = sqlite3.connect("X:\\EDWARD\\ITTrain\\sqlite\\testDB.db")
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e} occured")
        
    return connection

def create_mysql_connection():
    """ Make connection to mysql database """
    
    connection = None
    try:
        connection = mysql.connector.connect(
            host="DESKTOP-NHLF4F4",
            user="trainuser",
            passwd="trainuser"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_db_table_select(connection, query):
    """ Executes a select statement against a database.
        {connetion} is the connection to the specific database being queried
        {query} contains the select statement  """
            
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_db_table_statement(connection, statement):
    """ Executes a non-select DML statement against a database.
        {connetion} is the connection to the specific database where DML to be executed
        {statement} contains the insert/update/delete statement  """
            
    cursor = connection.cursor()
    try:
        cursor.execute(statement)
        connection.commit()
        print(f"Statement executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
def select_result(dbname, tblname):
    
    if dbname == 'Sqlite':
        connection = create_sqlite_connection()
        
        if tblname == 'users':
            select_text = "SELECT * from users"
            select_result = execute_db_table_select(connection, select_text)
        elif tblname == 'posts':
            select_text = "SELECT * from posts"
            select_result = execute_db_table_select(connection, select_text)
        elif tblname == 'likes':
            select_text = "SELECT * from likes"
            select_result = execute_db_table_select(connection, select_text)
        elif tblname == 'comments':
            select_text = "SELECT * from comments"
            select_result = execute_db_table_select(connection, select_text)
        else:
            errmsg = 'You must enter a valid table name!!'
            display_errmsg(errmsg)
                        
    elif dbname == 'MySql':
        connection = create_mysql_connection()
        
        if tblname == 'sales_01':
            select_text = "SELECT * from sales_01"
            usedb_statement = 'use traindb1'
            execute_db_table_statement(connection, usedb_statement)
            select_result = execute_db_table_select(connection, select_text)
        elif tblname == 'sales_02':
            None
        else:
            errmsg = 'You must enter a valid table name!!'
            display_errmsg(errmsg)
            
    return select_result

def mysql_insert(insert_statement):
    
    connection = create_mysql_connection()
    usedb_statement = 'use traindb1'
    execute_db_table_statement(connection, usedb_statement)
    execute_db_table_statement(connection, insert_statement)
   
def select_retrieve():
    
    db_name = db_gui.dbtype_choosen.get()
    if db_name == "":
        errmsg = 'You must select a DB Type!!'
        display_errmsg(errmsg)
    print(db_name)
    db_name_stripped = db_name.strip()
    
    tblname = db_gui.tblname_entry.get()
    if tblname == "":
        errmsg = 'You must a Table name!!'
        display_errmsg(errmsg)
    print(tblname)
    
    if db_name_stripped == 'Sqlite':
        select_result_txt = select_result(db_name_stripped, tblname)
    elif db_name_stripped == 'MySql':
        select_result_txt = select_result(db_name_stripped,tblname)     
    else:
        print('do nothing')
    
    db_gui.result_text.delete("1.0","end")
    for result in select_result_txt:
        #print(result)
        db_gui.result_text.insert('end', result)
        db_gui.result_text.insert('end', '\n')

    db_gui.chkbtn_writefile.config(command=write_file_selected)
    db_gui.chkbtn_writefile.grid(column=3,row=10, sticky=('w'))

def insert_data():
    
    db_name = db_gui.dbtype_choosen.get()
    print(db_name)
    db_name_stripped = db_name.strip()
  
    insertstatements = db_gui.result_text.get("1.0", "end")
    
    for ins_statement in insertstatements.split('\n'):
        print('line is: ' + ins_statement)
        
    #insert_statement = db_gui.result_text.get('1.0', 'end-1c')
    #print(insert_statement)
    
        if db_name_stripped == 'Sqlite':
            None
        #   select_result = sqlite_insert_statement()
        elif db_name_stripped == 'MySql':
            mysql_insert(ins_statement)     
        else:
            print('do nothing')
    
def widget_forget(widget):
    widget.grid_forget()
    
def exitprg():
    db_gui.window.destroy()
    

logging.basicConfig(filename='C:\\Users\\Public\\db_interface_app.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

db_gui.window.title("DB Interactive Application")
db_gui.window.geometry("1200x600")

for i in range(2):
    db_gui.window.columnconfigure(0, weight=1, minsize=75)
    db_gui.window.rowconfigure(0, weight=1, minsize=50)

    for j in range(0, 1):
        if i == 0 and j == 0:
            db_gui.frm_frame1.grid(row=i, column=j, padx=10, pady=10)
            db_gui.frm_frame1.grid_forget()
            
            db_gui.frm_frame2.grid(row=i, column=j, padx=25, pady=25)
            db_gui.frm_frame2.grid_forget()
            
        elif i == 1 and j == 0:
            db_gui.frm_buttons.grid(row=i, column=j, sticky='nsew')
            #db_gui.frm_buttons.grid_propagate(0)
            db_gui.frm_buttons.grid_forget
        else:
            None

window_load_menu()
startup_splash_frame()

db_gui.window.mainloop()