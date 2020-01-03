from tkinter import *
# from PIL import ImageTk, image
from tkinter import messagebox
from myedit_db import Database
from tkinter import filedialog

myedit_db = Database("items.db")
###########################

#######################
#### Menu Defined #####
#######################
def doNothing():
    print("OK OK I Won't...")

def populate_list():
    item_list.delete(0, END)
    for row in myedit_db.fetch():
        item_list.insert(END, row)


def add_item():
    if item_text.get() == '' or amount_text.get() == '' or supplier_text.get() == '' or cost_text.get() == '' or dpt_text.get() == '' or admin_text.get() == '':
        messagebox.showerror('Required Fields', 'Please Fill Out All Fields')
        return
    myedit_db.insert(item_text.get(), amount_text.get(), supplier_text.get(), cost_text.get(), dpt_text.get(),
                      admin_text.get())
    item_list.delete(0, END)
    item_list.insert(END, (item_text.get(), amount_text.get(), supplier_text.get(), cost_text.get(), dpt_text.get(),
                           admin_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = item_list.curselection()[0]
        selected_item = item_list.get(index)

        item_entry.delete(0, END)
        item_entry.insert(END, selected_item[1])
        amount_entry.delete(0, END)
        amount_entry.insert(END, selected_item[2])
        supplier_entry.delete(0, END)
        supplier_entry.insert(END, selected_item[3])
        cost_entry.delete(0, END)
        cost_entry.insert(END, selected_item[4])
        dpt_entry.delete(0, END)
        dpt_entry.insert(END, selected_item[5])
        admin_entry.delete(0, END)
        admin_entry.insert(END, selected_item[6])
    except IndexError:
        pass


def remove_item():
    myedit_db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    myedit_db.update(selected_item[0], item_text.get(), amount_text.get(),
                     supplier_text.get(), cost_text.get(), dpt_text.get(), admin_text.get())
    populate_list()


def clear_text():
    item_entry.delete(0, END)
    amount_entry.delete(0, END)
    supplier_entry.delete(0, END)
    cost_entry.delete(0, END)
    dpt_entry.delete(0, END)
    admin_entry.delete(0, END)


# Create window object
app = Tk()
####################################
###### Item Label And Text Box #####
####################################
item_text = StringVar()
item_label = Label(app, text='Item Name : ', fg='brown', font=('Gill Sans Ultra Bold', 12), pady=10)
item_label.place(x=15, y=5)
item_entry = Entry(app, textvariable=item_text)
item_entry.place(x=150, y=15)
#####################################
##### Amount Label And Text Box #####
#####################################
amount_text = StringVar()
amount_label = Label(app, text='Quantity : ', fg='brown', font=('Gill Sans Ultra Bold', 12))
amount_label.place(x=350, y=10)
amount_entry = Entry(app, textvariable=amount_text)
amount_entry.place(x=470, y=15)
######################################
#### Supplier Label And Text Box #####
######################################
supplier_text = StringVar()
supplier_label = Label(app, text='Supplier : ', fg='brown', font=('Gill Sans Ultra Bold', 12))
supplier_label.place(x=45, y=50)
supplier_entry = Entry(app, textvariable=supplier_text)
supplier_entry.place(x=150, y=50)
# Cost
cost_text = StringVar()
cost_label = Label(app, text='Item Cost : ', fg='brown', font=('Gill Sans Ultra Bold', 12))
cost_label.place(x=350, y=50)
cost_entry = Entry(app, textvariable=cost_text)
cost_entry.place(x=470, y=50)
# Department
dpt_text = StringVar()
dpt_label = Label(app, text='Department : ', fg='brown', font=('Gill Sans Ultra Bold', 12))
dpt_label.place(x=680, y=10)
dpt_entry = Entry(app, textvariable=dpt_text)
dpt_entry.place(x=840, y=10)
# Admin
admin_text = StringVar()
admin_label = Label(app, text='Administror : ', fg='brown', font=('Gill Sans Ultra Bold', 12))
admin_label.place(x=680, y=50)
admin_entry = Entry(app, textvariable=admin_text)
admin_entry.place(x=840, y=50)
# Item List (ListBox)
item_list = Listbox(app, height=12, width=70, border=5)
item_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=100, padx=20)
# Create Scrollbar
scrollbar = Scrollbar(app)
scrollbar.place(x=550, y=170)
# Set Scrollbar To List Box
item_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=item_list.yview)
# Bind Selection From List Box
item_list.bind('<<ListboxSelect>>', select_item)

# Button
add_btn = Button(app, text='Add Item', bg='brown', font='bold', fg='yellow', width=12, command=add_item)
add_btn.place(x=650, y=100)

remove_btn = Button(app, text='Remove Item', bg='brown', font='bold', fg='yellow', width=12, command=remove_item)
remove_btn.place(x=650, y=150)

update_btn = Button(app, text='Update Item', bg='brown', font='bold', fg='yellow', width=12, command=update_item)
update_btn.place(x=800, y=150)

clear_btn = Button(app, text='Clear Text', bg='brown', font='bold', fg='yellow', width=12, command=clear_text)
clear_btn.place(x=800, y=100)

button_exit = Button(app, text="EXIT Program", bg='brown', font='bold', fg='yellow',command=app.quit)
button_exit.place(x=650, y=200)

app.title('DSVHub Inventory Manager')
app.iconbitmap("C:/Users/nemes/Documents/My_Files/MyCodes/Media/dsvarietyhublogo1.ico")
app.geometry('1000x350')

#####################
##### Menu Bar #####
####################
menu = Menu(app)
app.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="Item", menu=subMenu)
subMenu.add_command(label="Add Item...", command=add_item)
subMenu.add_command(label="Remove Item...", command=remove_item)
subMenu.add_command(label="Clear Text...", command=clear_text)
subMenu.add_command(label="Update...", command=update_item)
subMenu.add_separator()
subMenu.add_command(label="QUIT Program", command=app.quit)

editMenu = Menu(menu)
menu.add_cascade(label="File", menu=editMenu)
editMenu.add_command(label="Open File...", command=doNothing)
editMenu.add_command(label="Save File...", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="About", menu=editMenu)
editMenu.add_command(label="Info...", command=doNothing)
editMenu.add_command(label="HELP...", command=doNothing)

# Populate Data
populate_list()

# Start program
app.mainloop()

# To create an executable, install pyinstaller and run
# '''
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py
# '''
