import tkinter as tk
import tkinter.font as tkFont
from classes import *
import classes 
from tkinter import messagebox

class Login:
    def __init__(self, root):
        
        self.window = root
        self.root = root
        
        bg_main = "#d8c3a5"
        btn_bg = "#eae7dc"
        ft = tkFont.Font(family='Roboto',size=25)
        
        root.title("Restraunt Management System")
        width=750
        height=320
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background = bg_main)
        
        self.name_restraunt=tk.Label(root)
        self.name_restraunt["font"] = ft
        self.name_restraunt["fg"] = "black"
        self.name_restraunt["bg"] = bg_main
        self.name_restraunt["justify"] = "center"
        self.name_restraunt["text"] = "NAME OF RESTAURANT"
        self.name_restraunt.place(x=10,y=40,width=729,height=30)
        
        ft = tkFont.Font(family='Roboto',size=15)
        self.name_restraunt=tk.Label(root)
        self.name_restraunt["font"] = ft
        self.name_restraunt["fg"] = "black"
        self.name_restraunt["bg"] = bg_main
        self.name_restraunt["justify"] = "center"
        self.name_restraunt["text"] = "LOG IN"
        self.name_restraunt.place(x=10,y=100,width=729,height=30)
        
        ft = tkFont.Font(family='Roboto',size=12, weight = "bold")
        self.username=tk.Entry(root)
        self.username["borderwidth"] = "1px"
        self.username["font"] = ft
        self.username["fg"] = "#333333"
        self.username["text"] = "User Name"
        self.username.place(x=160,y=140,width=494,height=30)

        self.password=tk.Entry(root)
        self.password["borderwidth"] = "1px"
        self.password["font"] = ft
        self.password["fg"] = "#333333"
        self.password["text"] = "Password"
        self.password.place(x=160,y=220,width=493,height=30)
        self.password['show'] = '*'

        self.label_username=tk.Label(root)
        self.label_username["font"] = ft
        self.label_username["fg"] = "#333333"
        self.label_username["bg"] = bg_main
        self.label_username["justify"] = "center"
        self.label_username["text"] = "User ID:"
        self.label_username.place(x=80,y=140,width=70,height=25)

        self.label_password=tk.Label(root)
        self.label_password["font"] = ft
        self.label_password["fg"] = "#333333"
        self.label_password["bg"] = bg_main
        self.label_password["justify"] = "center"
        self.label_password["text"] = "Password:"
        self.label_password.place(x=70,y=220,width=80,height=25)        
        
        self.login_btn=tk.Button(root)
        self.login_btn["bg"] = btn_bg
        self.login_btn["font"] = ft
        self.login_btn["fg"] = "black"
        self.login_btn["justify"] = "center"
        self.login_btn["text"] = "Admin Login"
        self.login_btn.place(x=200,y=280,width=150,height=30)
        self.login_btn["command"] = self.logAdmin
        
        self.login_btn=tk.Button(root)
        self.login_btn["bg"] = btn_bg
        self.login_btn["font"] = ft
        self.login_btn["fg"] = "black"
        self.login_btn["justify"] = "center"
        self.login_btn["text"] = "Employee Login"
        self.login_btn.place(x=400,y=280,width=150,height=30)
        self.login_btn["command"] = self.logEMP
    
    def logAdmin(self):
        self.window.destroy()
        root = tk.Tk()
        app = AdminPanel(root)
        root.mainloop()
        
            
    def logEMP(self):
        pass


class AdminPanel:
    def __init__(self, root):
        root.title("Admin Panel")
        width=1160
        height=615
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.admin=tk.Label(root)
        ft = tkFont.Font(family='Roboto',size=80)
        self.admin["font"] = ft
        self.admin["fg"] = "#333333"
        self.admin["justify"] = "center"
        self.admin["text"] = "ADMIN MODE"
        self.admin.place(x=0,y=0,width=1160,height=181)

        self.name=tk.Label(root)
        ft = tkFont.Font(family='Roboto',size=38)
        self.name["font"] = ft
        self.name["fg"] = "#333333"
        self.name["justify"] = "center"
        self.name["text"] = "Name:"
        self.name.place(x=90,y=200,width=156,height=71)

        self.name_admin_panel=tk.Label(root)
        ft = tkFont.Font(family='Roboto',size=38)
        self.name_admin_panel["font"] = ft
        self.name_admin_panel["fg"] = "#333333"
        self.name_admin_panel["justify"] = "left"
        self.name_admin_panel["text"] = "Achyut Shukla"
        self.name_admin_panel.place(x=270,y=200,width=866,height=71)

        self.btn_emp_mng=tk.Button(root)
        self.btn_emp_mng["bg"] = "#efefef"
        ft = tkFont.Font(family='Roboto',size=28)
        self.btn_emp_mng["font"] = ft
        self.btn_emp_mng["fg"] = "#000000"
        self.btn_emp_mng["justify"] = "center"
        self.btn_emp_mng["text"] = "Manage Employee"
        self.btn_emp_mng.place(x=420,y=290,width=345,height=62)
        self.btn_emp_mng["command"] = self.btn_emp_mng_command

        self.btn_reset=tk.Button(root)
        self.btn_reset["bg"] = "#efefef"
        ft = tkFont.Font(family='Roboto',size=28)
        self.btn_reset["font"] = ft
        self.btn_reset["fg"] = "#000000"
        self.btn_reset["justify"] = "center"
        self.btn_reset["text"] = "Reset Data Base"
        self.btn_reset.place(x=420,y=470,width=345,height=62)
        self.btn_reset["command"] = self.btn_reset_command

        self.btn_logout=tk.Button(root)
        self.btn_logout["bg"] = "#efefef"
        ft = tkFont.Font(family='Roboto',size=28)
        self.btn_logout["font"] = ft
        self.btn_logout["fg"] = "#000000"
        self.btn_logout["justify"] = "center"
        self.btn_logout["text"] = "Log Out"
        self.btn_logout.place(x=970,y=550,width=157,height=45)
        self.btn_logout["command"] = self.btn_logout_command

        self.btn_manage_item=tk.Button(root)
        self.btn_manage_item["bg"] = "#efefef"
        ft = tkFont.Font(family='Roboto',size=28)
        self.btn_manage_item["font"] = ft
        self.btn_manage_item["fg"] = "#000000"
        self.btn_manage_item["justify"] = "center"
        self.btn_manage_item["text"] = "Manage Items"
        self.btn_manage_item.place(x=420,y=380,width=345,height=62)
        self.btn_manage_item["command"] = self.btn_manage_item_command

    def btn_emp_mng_command(self):
        print("command")


    def btn_reset_command(self):
        print("command")


    def btn_logout_command(self):
        print("command")


    def btn_manage_item_command(self):
        print("command")
        

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
