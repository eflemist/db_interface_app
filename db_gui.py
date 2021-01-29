import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import filedialog

frm_splash_visible = False
frm_retrieve_visible = False
frm_insert_visible = False
frm_delete_visible = False
frm_update_visible = False


window = tk.Tk()
#window.title("DB Interactive Application")
#window.geometry("1200x600")

#fontStyle = tkFont.Font(family="Lucida Grande", size=20)

frm_frame1 = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3)
frm_frame2 = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3)
frm_buttons = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=3)

lbl_dbtype_select = ttk.Label(frm_frame2, text = "Select DB to use:") 
var_dbtype = tk.StringVar() 
dbtype_choosen = ttk.Combobox(frm_frame2, width = 15, textvariable = var_dbtype)
dbtype_choosen['values'] = (' Sqlite',  
                          ' MySql', 
                          ' Postgres', 
                          ' MongoDb') 

lbl_table_retrieve = ttk.Label(frm_frame2, text="Name of Table to retrive data:")
lbl_result_text = ttk.Label(frm_frame2, text="Result from Select is:")
lbl_errmsg = ttk.Label(frm_frame2,width=75, foreground="black", background="red")
lbl_filename = ttk.Label(frm_frame2,width=25)

tblname_entry = tk.Entry(frm_frame2, width=25)
ent_filename = tk.Entry(frm_frame2, width=15)

result_text = tk.Text(frm_frame2, height=20, width=100)

var_chkbtn = tk.StringVar(value='N')   
chkbtn_writefile = tk.Checkbutton(frm_frame2, text = "Write Result to File?",  
                      variable = var_chkbtn, 
                      onvalue = 'Y', 
                      offvalue = 'N', 
                      height = 2, 
                      width = 15)

btn_home = ttk.Button(frm_buttons, text="Home", command=None)
btn_readfile = ttk.Button(frm_buttons, text="Read File", command=None)
btn_writefile = ttk.Button(frm_buttons, text="Write File", command=None)
btn_retrieve = ttk.Button(frm_buttons, text="Retrieve", command=None)
btn_insert = ttk.Button(frm_buttons, text="Insert", command=None)
btn_update = ttk.Button(frm_buttons, text="Update", command=None)
btn_delete = ttk.Button(frm_buttons, text="Delete", command=None)
btn_exit = ttk.Button(frm_buttons, text="Exit", command=None)

 


    
 