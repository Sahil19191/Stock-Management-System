# Problem in add and withdraw
# Search box

from tkinter        import * 
from tkinter        import messagebox
from tkinter.font   import BOLD
from PIL            import Image,ImageTk
from datetime       import datetime


import tkinter as ttk
import json

import Helper
import Login

#   Path for all related files

    # Image path for login page
login_image = #Add path here
icon_path = #Add path here




class Login:
    def __init__(self):

        self.name = ''
        self.pin=''
        self.id=''
        self.name=''
        self.fund=0
        self.user_dict={}
        self.root = Tk()
        self.root.title("Login")
        photo = Image.open(icon_path)
        self.icon=ImageTk.PhotoImage(photo)
        self.root.iconphoto(False, self.icon)
        self.root.geometry("1000x600+250+75")
        fr1 = Frame(self.root, bg="#E7F4FF").place(
            x=0, y=0, width=374, height=626)
        fr2 = Frame(self.root, bg="white").place(x=374, y=0, width=626, height=626)
        im = Image.open(login_image)
        self.bg = ImageTk.PhotoImage(im)

        #Label(fr2, image=self.bg).pack()
        self.bg_Image = Label(fr2, image=self.bg).place( x=374, y=0, width=626, height=626)

        desc = Label(fr1, text="Login here!", font=("calibri", 25, "bold"), bg="#E7F4FF").place(x=100, y=30)

        lab_user1 = Label(fr1, text="UserID", font=( "calibri", 14, "bold"), fg="black").place(x=65, y=120)
        self.txt_user = Entry(fr1, font=("comicsansms", 15))
        self.txt_user.place(x=65, y=150, width=250, height=35)
        self.txt_user.configure(highlightbackground="#6794F5", highlightcolor="#6794F5", highlightthickness=2)

        lab_pass1 = Label(fr1, text="Password", font=("calibri", 14, "bold"), fg="black").place(x=65, y=220)
        self.txt_pass = Entry(fr1, font=("comicsansms", 15))
        self.txt_pass.place(x=65, y=250, width=250, height=35)
        self.txt_pass.configure(highlightbackground="#6794F5", highlightcolor="#6794F5", highlightthickness=2)

        #forget_btn = Button(Frame_login, command=self.forget_password, text="Forget Password?", fg="white", bg='black')
       # forget_btn.place(x=100, y=295)
        login_btn = Button(fr1, command=self.login_function, text="Login", font=("calibri", 13, 'bold'), fg="black", bg='#4696F9', relief=GROOVE)
        login_btn.place(x=75, y=330, width=230)

        Button(fr1, text='Forgot Password?', command=self.Forget, font=('calibri', 12, 'bold'), fg='black', bg='#E7F4FF', relief=FLAT).place(x=55, y=390)

        #Label(text='New here?',font=('calibri',14,'bold'),fg='black',bg='#43C4D3',relief=FLAT).place(x=110,y=323)
        Button(fr1, text='Click to Register', command=self.Register, font=('calibri', 12,'bold'), fg='black', bg='#E7F4FF', relief=FLAT).place(x=205, y=390)
        ##34495E 
        self.root.mainloop()

        self.root.mainloop()
    #end of __init__

    def Forget(self):
        self.newroot=Toplevel()
        self.newroot.focus_force()
        self.newroot.grab_set()
        self.newroot.title('Forgot Password')
        self.newroot.geometry('350x300+700+300')
        self.newroot.config(bg='#76D7C4')
        photo = Image.open(icon_path)
        self.icon=ImageTk.PhotoImage(photo)
        self.newroot.iconphoto(False, self.icon)
        
        Label(self.newroot,text='ID',bg='red',fg='white',relief=RAISED,font=("calibri",13,"bold")).place(x=30,y=50, width=95, height=25)
        Label(self.newroot, text='New PIN', bg='red', fg='white', relief=RAISED, font=(
            "calibri", 13, "bold")).place(x=30, y=95, width=95, height=25)
        new_pass = StringVar()
        self.id_entry = Entry(self.newroot,textvariable=new_pass,borderwidth=3)
        self.id_entry.place(x=150, y=50, width=170, height=25)
        new_id = StringVar()
        self.pass_entry = Entry(self.newroot, textvariable=new_id,borderwidth=3)
        self.pass_entry.place(x=150, y=95, width=170, height=25)
        Button(self.newroot,text='Submit',command=self.onClick_forget,bg='black',fg='white').place(x=120,y=170,width=100,height=30)
        
        self.newroot.mainloop()
    
    def onClick_forget(self):
        self.id = self.id_entry.get()
        self.p = self.pass_entry.get()
    
        if self.id=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.id not in Helper.d.keys():
            messagebox.showerror("Error","Id not found", parent=self.root)
        else:
            if self.p=="":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            elif(len(self.p)!=6):
                messagebox.showerror("Error","Please enter 6 digit pin", parent=self.root)
            else:
                if(self.p.isdecimal() == False):
                    messagebox.showerror("Error","Only Digits are allowed", parent=self.root)
                    return
                Helper.d[self.id]=self.p
                self.save_login()
                messagebox.showinfo("info","successfully changed", parent=self.root)
                self.newroot.destroy()
   
    def Register(self):
        self.newroot = Toplevel()
        self.newroot.focus_force()
        self.newroot.grab_set()
        self.newroot.title('Register')
        self.newroot.geometry('350x300+700+300')
        self.newroot.config(bg='#76D7C4')
        photo = Image.open(icon_path)
        self.icon=ImageTk.PhotoImage(photo)
        self.newroot.iconphoto(False, self.icon)
        
        Label(self.newroot,text='ID',bg='red',fg='white',relief=RAISED,font=("calibri",13,"bold")).place(x=50,y=50,width=50,height=25)
        Label(self.newroot,text='PIN',bg='red',fg='white',relief=RAISED,font=("calibri",13,"bold")).place(x=50,y=100,width=50,height=25)
        Label(self.newroot, text='Name', bg='red',fg='white', relief=RAISED,font=("calibri",13,"bold")).place(x=50, y=150,width=50,height=25)
       
        new_id = StringVar()
        self.id_entry = Entry(self.newroot, textvariable=new_id, relief=SUNKEN,borderwidth=3,highlightbackground="black",highlightcolor='black')
        self.id_entry.place(x=120,y=50,width=150,height=25)
        new_pin = StringVar()
        self.pin_entry = Entry(self.newroot, textvariable=new_pin,relief=SUNKEN,borderwidth=3)
        self.pin_entry.place(x=120, y=100, width=150, height=25)
        new_name = StringVar()
        self.name_entry = Entry(
            self.newroot, textvariable=new_name, relief=SUNKEN, borderwidth=3)
        self.name_entry.place(x=120, y=150, width=150, height=25)
        Button(self.newroot,text='Submit',command=self.onClick_register,bg='black',fg='white').place(x=135,y=215,width=100,height=30)
        
        self.newroot.mainloop()
        
    def onClick_register(self):
        id = self.id_entry.get()
        pin = self.pin_entry.get()
        name = self.name_entry.get()
        if id=="" or pin=="" or name=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif(id in Helper.d.keys()):
            messagebox.showerror('Error','Id already exists', parent=self.root)
        elif(len(pin) != 6):
            messagebox.showerror("Error", "Please enter 6 digit pin", parent=self.root)
        else:
            if(pin.isdecimal() == False):
                    messagebox.showerror("Error","Only Digits are allowed", parent=self.root)
                    return

            Helper.d[id]=pin
            self.user_dict[name]=0
            self.save_login()
            self.new_user()
            messagebox.showinfo("info", "Account successfully created", parent=self.root)
            self.newroot.destroy()

    def login_function(self):
         self.pin = self.txt_pass.get()
         self.id = self.txt_user.get()
         if self.txt_pass.get() == "" or self.txt_user.get() == "":
             messagebox.showerror("Error", "All fields are required", parent=self.root)
         else:
              if self.id in Helper.d.keys():
                 if self.pin == str(Helper.d[self.id]):
                      n, f, u_dict = Helper.user_details(self.id)
                      self.name = n
                      self.fund = f
                      self.user_dict = u_dict
                      self.root.destroy()
                      Home.home(self)
                 else:
                    messagebox.showerror("Error", "Invalid PIN", parent=self.root)
              else:
                   messagebox.showerror("Error", "Invalid ID", parent=self.root)
    # login_function end

    def save_login(self):
        f = open(Helper.user_file, "w")
        f.write(str(json.dumps(Helper.d)))
        f.close()
    # save_login_function end
    
    # Registering new user
    def new_user(self):
        self.id = self.id_entry.get()
        id_file = Helper.sample_id_path+self.id+'.txt'
        f = open(id_file, "w")
        f.write(str(json.dumps(self.user_dict)))
        f.close()
    # new_user function end

    # Saving data when logout
    def save_home(self):
        id_file = Helper.sample_id_path+self.id+'.txt'
        f = open(id_file, "w")
        f.write(str(json.dumps(self.user_dict)))
        f.close()
    # save_home_function end


## Login class ends#####################################################


class Home(Login):

    def home(self):
        self.root=Tk()
        self.root.geometry('1150x645+110+60')
        self.root.state('zoomed')
        self.root.title('Stock Market')
        self.root.config(bg='#D6DBDF', relief=SUNKEN, highlightbackground="#2E4053",
                         highlightcolor="#2E4053", highlightthickness=2)
        photo = Image.open(icon_path)
        self.icon=ImageTk.PhotoImage(photo)
        self.root.iconphoto(False, self.icon)

        #Frame1 - Name 
        fr1=Frame(self.root,bg="#4B4A7F", highlightbackground="#2E4053", highlightcolor="#2E4053", highlightthickness=2)
        fr1.pack(side=TOP,fill='x')
        self.ABC=StringVar()
        self.nse_index=StringVar()
        self.nse_index.set('NIFTY50 : '+str(Helper.index()))
        temp = round(self.user_dict[self.name],2)
        self.ABC.set('FUNDS: '+str(temp))
        
        Label(fr1,text=self.name.upper(),font=('calibri',30,BOLD),fg='black',bg='#EC9787',relief=SUNKEN).pack(padx=10,pady=10,side=LEFT)        
        Label(fr1,textvariable=self.ABC,font=('calibri',25,BOLD),fg='black',bg='#EC9787',relief=SUNKEN).pack(padx=10,pady=10,side=RIGHT)
        Label(fr1,textvariable=self.nse_index,font=('calibri',25,BOLD),fg='black',bg='#EC9787',relief=SUNKEN).pack(padx=10,pady=10,anchor='n')


        #Frame2 - Functional Buttons
        fr2=Frame(self.root,bg="#f7cec3", highlightbackground="#2E4053", highlightcolor="#2E4053", highlightthickness=2,pady=50,padx=10)
        fr2.pack(side=LEFT,fill='y')
        Button(fr2,text='FUNDS',command=self.fund_f,font=("times new roman",15,"bold"),bg="#4C4B80",fg="white",relief=RAISED).pack(padx=20,pady=20,side=TOP,fill='x')        
        Button(fr2,text='BUY',command=self.buy,font=("times new roman",15,"bold"),bg="#4C4B80",fg="white",relief=RAISED).pack(padx=20,pady=20,side=TOP,fill='x')
        Button(fr2,text='SELL',command=self.sell,font=("times new roman",15,"bold"),bg="#4C4B80",fg="white",relief=RAISED).pack(padx=20,pady=20,side=TOP,fill='x')
        Button(fr2,text='PORTFOLIO',command=self.portfolio,font=("times new roman",15,"bold"),bg="#4C4B80",fg="white",relief=RAISED).pack(padx=20,pady=20,side=TOP,fill='x')
        Button(fr2, text='LOGOUT', command=self.logout, font=("times new roman", 15, "bold"),
               bg="#E74F44", fg="white", relief=RAISED).pack(padx=20, pady=20, side=TOP, fill='x')
        Button(fr2, text='RELOAD', command=self.Refresh, font=("times new roman", 15, "bold"),
               bg="#34495E", fg="white", relief=RAISED).pack(padx=20, pady=0, side=BOTTOM, fill='x')


        #Frame3 - Static List
        fr3=Frame(self.root,bg='#D6DBDF',relief=SUNKEN,highlightbackground="#2E4053", highlightcolor="#2E4053", highlightthickness=2)
        fr3.pack(fill=BOTH)

        self.common_stock_list=['RELIANCE','MRF','ADANIGREEN','ADANIPOWER','NAZARA','SBICARD','INFY']
        self.B=[]
        self.S=[]

        for i in range(len(self.common_stock_list)):
            self.B.append(StringVar())
            self.S.append(StringVar())
        
        FR=Frame(fr3,bg='#CEE5F0', relief=SUNKEN)
        FR.pack(fill='x',padx=10,pady=10)
        Label(FR, text='NAME ( Code )', font=('times new roman', 19,BOLD),fg='black', bg='#CEE5F0',relief=SUNKEN).pack(padx=10, pady=10, side=LEFT)
        Label(FR, text='Price( INR ) / Percentage Change', font=('times new roman', 19, BOLD),
              fg='black', bg='#CEE5F0', relief=SUNKEN).pack(padx=10, pady=10, side=RIGHT)
        #Label(FR,text='PRICE',font=('times new roman',17,BOLD),bg='#FF5733').pack(padx=320,pady=10,side=RIGHT)
        FR4=Frame(self.root,bg='#D6DBDF',relief=SUNKEN )
        FR4.pack(fill='x',side=BOTTOM,anchor='s',padx=10,pady=10)
        for i in range(len(self.common_stock_list)):
            try:
                b,s,per=Helper.nse_get(self.common_stock_list[i])
            except:
                messagebox.showerror("Error","Invalid code", parent=self.root)
            self.B[i].set(s+' ( '+self.common_stock_list[i]+' )')
            self.S[i].set(str(b)+' / '+str(per))
            fr=Frame(fr3)
            fr.pack(fill='x',padx=10,pady=7)
            Label(fr,textvariable=self.B[i], font=('calibri', 15), bg='white').pack(padx=10, pady=10, side=LEFT)
            Label(fr,textvariable=self.S[i],font=('calibri',15),bg='white').pack(padx=10,pady=10,side=RIGHT)
        
        #Search Bar
        sfr=Frame(FR4,relief=SUNKEN)
        sfr.pack(padx=10,pady=10,side=BOTTOM,anchor='s')
        self.svalue=StringVar()
        self.s_entry=Entry(sfr,textvariable=self.svalue,width=65,font=('Times new roman',18))
        self.s_entry.pack(padx=10,pady=10,side=LEFT)
        self.s_entry.configure(highlightbackground="red", highlightcolor="red", highlightthickness=2)
        Button(sfr,text="Search",command=self.search,font=('Times new roman',16,"bold"),bg='#34495E',fg='white',width=40).pack(padx=10,pady=10,side=RIGHT)

        
    
        self.root.mainloop()
    # End of home 

    #Refresh Button
    def Refresh(self):
        self.nse_index.set('NIFTY50 : '+str(Helper.index()))
        for i in range(len(self.common_stock_list)):
            try:
                b,s,per=Helper.nse_get(self.common_stock_list[i])
            except:
                messagebox.showerror("Error","Invalid Code", parent=self.root)
            self.S[i].set(b+' / '+str(per))
        
    #search box
    def search(self):
        var=self.svalue.get()
        if var == "":
            messagebox.showerror("Error", "Empty searchbox", parent=self.root)
            return
        l1=[]
        l2=[]
        try: 
            l1,l2=Helper.search_m(var)
        except Exception as e:
            messagebox.showerror("Error",'Please be more specific', parent=self.root)
            return
        
        #New search-result window
        self.newroot = Toplevel()
        self.newroot.focus_force()
        self.newroot.grab_set()
        self.newroot.geometry('900x600')
        self.newroot.maxsize(900,600)
        self.newroot.minsize(900,600)
        self.newroot.title('Results')
        self.newroot.configure(bg="#C5EBF6")
        photo = Image.open(icon_path)
        self.icon=ImageTk.PhotoImage(photo)
        self.newroot.iconphoto(False, self.icon)
        #Title Frame
        Tframe = Frame(self.newroot, bg='#4B4A7F')
        Tframe.pack(side=TOP,anchor='w',fill=X,)
        Label(Tframe, text="Name( Code )\t\tPrice( INR )",font=("calibri", 20, "bold"), fg="black", bg="#C5EBF6",relief=SUNKEN).pack(anchor='n',padx=40,pady=10)
        
        # Result List
        first_frame=Frame(self.newroot,bg='red')
        first_frame.pack(side=TOP,fill=BOTH,expand=1)
        Cvas = Canvas(first_frame, bg='#C5EBF6', bd=0, width=400)
        Cvas.pack(side=LEFT,fill=BOTH,expand=1)
        scbar=ttk.Scrollbar(first_frame,orient=VERTICAL, command=Cvas.yview)
        scbar.pack(side=RIGHT, fill=Y)
        Cvas.configure(yscrollcommand=scbar.set)
        Cvas.bind('<Configure>',lambda e:Cvas.configure(scrollregion=Cvas.bbox('all')))
        second_frame=Frame(Cvas,bg='#C5EBF6')
        Cvas.create_window((50,0),window=second_frame,anchor='nw')

        
        i=0
        while i<len(l1):
            f = Frame(second_frame, bg='#f7cec3')  # EC9787
            f.pack(fill="both",padx=110,pady=10)
            Label(f, text=str(l1[i]),font=("calibri", 15, "bold"), fg="black", bg="lightblue",relief=SUNKEN).pack(side=LEFT,padx=10,pady=10)
            Label(f, text=str(l2[i]),font=("calibri", 15, "bold"), fg="black", bg="lightblue",relief=SUNKEN).pack(side=RIGHT,padx=10,pady=10)
            i+=1
            


    #Funds Button
    def fund_f(self):
        
        #New Funds window 
        self.newroot=Toplevel()
        self.newroot.focus_force()
        self.newroot.grab_set()
        self.newroot.geometry('600x400+475+240')
        self.newroot.title('FUNDS')
        self.newroot.configure(bg="#C5EBF6")
        photo = Image.open(icon_path)
        self.icon=ImageTk.PhotoImage(photo)
        self.newroot.iconphoto(False, self.icon)

        Label(self.newroot, text="Enter Amount",  font=("calibri", 15,
                                                        "bold"), fg="black", bg="#C5EBF6").place(x=100, y=60)
        self.e_fund = Entry(self.newroot, font=("calibri", 15), bg="white")
        self.e_fund.place(x=100, y=100, width=350, height=35)
        Button(self.newroot, command=self.onClick_fund,text='Add',font=("times new roman",13,"bold"),bg="#239B56",fg="white",relief=RIDGE).place(x=130, y=170)
        Button(self.newroot, command=self.withdraw, text='Withdraw', font=(
            "times new roman", 13, "bold"), bg="#239B56", fg="white", relief=RIDGE).place(x=240, y=170)


    # Add Funds
    def onClick_fund(self):
        if self.e_fund.get()== "":
            messagebox.showerror("Error", "All fields are required", parent=self.newroot)
        
        else:
            try:
                f = float(self.e_fund.get())
                if f <=0:
                    messagebox.showerror("Error","Please enter valid ammount",parent=self.newroot)
                    return
                
                self.fund += f
                self.user_dict[self.name] = self.fund
                self.ABC.set('FUNDS: '+str(round(self.user_dict[self.name],2)))
                messagebox.showinfo("Status","Successfully Added", parent=self.newroot)
                self.newroot.destroy()
            except:
                messagebox.showerror("Error","Only Digits are allowed", parent=self.newroot)
               
    # Withdraw Funds
    def withdraw(self):
        if self.e_fund.get()== "":
            messagebox.showerror("Error", "All fields are required", parent=self.newroot)
        else:
            try:
                f = float(self.e_fund.get())
                if f <=0:
                    messagebox.showerror("Error","Please enter valid ammount",parent=self.newroot)
                    return
                if(f<=self.fund):
                    self.fund -= f
                    self.user_dict[self.name] = self.fund
                    self.ABC.set('FUNDS: '+str(round(self.user_dict[self.name],2)))
                    messagebox.showinfo("Status","Successfully Withdrawn", parent=self.newroot)
                else:
                    messagebox.showerror("Error","Not Enough Money", parent=self.newroot)
            except:
                messagebox.showerror("Error","Only Digits are allowed", parent=self.newroot) 
    #end of withdraw

    # Buy Button
    def buy(self):
         if(Helper.checktime() != TRUE):
             messagebox.showinfo("Message","Market is closed")
             return 

         self.newroot = Toplevel()
         self.newroot.focus_force()
         self.newroot.grab_set()
         self.newroot.geometry('600x400+475+240')
         self.newroot.title('Buy Stocks')
         self.newroot.configure(bg="#C5EBF6")
         photo = Image.open(icon_path)
         self.icon=ImageTk.PhotoImage(photo)
         self.newroot.iconphoto(False, self.icon)
         #self.Frame_buy = Frame(bg="orange").place(x=0, y=0, width=1350, height=700)
         Label(self.newroot, text="Enter CODE of Stock(share) to buy", font=("calibri", 15, "bold"), fg="black", bg="#C5EBF6").place(x=100, y=70)
         self.e_code= Entry(self.newroot, font=("calibri", 15), bg="white")
         self.e_code.place(x=100, y=110, width=350, height=35)
         Label(self.newroot, text="Enter QUANTITY of Stock", font=("calibri", 15, "bold"), fg="black", bg="#C5EBF6").place(x=100, y=155)
         self.e_quantity = Entry(self.newroot, font=("calibri", 15), bg="white")
         self.e_quantity.place(x=100, y=195, width=350, height=35)
         #self.bt1 = Button(self.newroot, command=self.home, text='back').place(x=100, y=425)
         self.bt2 = Button(self.newroot, command=self.onClick_buy, text='BUY', font=("times new roman",15,"bold"),bg="#4987ee",fg="white",relief=GROOVE).place(x=100, y=250,width=350, height=35)

    #Buy Function
    def onClick_buy(self):
        if self.e_code.get() == "" or self.e_quantity.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.newroot)
        else:
            try:
                s= Helper.nse.get_quote(self.e_code.get())
                if(s==None):
                    messagebox.showerror("Error","Invalid Code", parent=self.newroot)
                    return
                price = s['sellPrice1']
                if(int(self.e_quantity.get())<=0 or float(self.e_quantity.get())-int(self.e_quantity.get())!=0):
                    messagebox.showerror("Error","Enter valid Quantity", parent=self.newroot)
                    return
                
                req= int(self.e_quantity.get())*price

                dec=messagebox.askquestion('Are you sure ?','Required Funds : '+str(req), parent=self.newroot)
                if(dec == 'yes'):
                    str1 = Helper.buy(self.e_code.get(), self.e_quantity.get(), self.name, self.fund, self.user_dict)
                    self.ABC.set('FUNDS: '+str(round(self.user_dict[self.name],2)))
                    messagebox.showinfo("Status", str1, parent=self.newroot)
                    self.newroot.destroy()
            except TypeError:
                messagebox.showerror("Error","Only digits are allowed in quantity", parent=self.newroot)
            except Exception as e:
                messagebox.showerror("Exception",e)



    #Sell Button
    def sell(self):
         if(Helper.checktime() != TRUE):
            messagebox.showinfo("Message","Market is closed")
            return 
         self.newroot = Toplevel()
         self.newroot.focus_force()
         self.newroot.grab_set()
         self.newroot.geometry('600x400+475+240')
         self.newroot.title('Sell Stocks')
         self.newroot.configure(bg="#C5EBF6")
         photo = Image.open(icon_path)
         self.icon=ImageTk.PhotoImage(photo)
         self.newroot.iconphoto(False, self.icon)
         #self.Frame_sell=Frame(bg="orange").place(x=0, y=0, width=1350, height=700)
         Label(self.newroot, text="Enter CODE of Stock(share) to sell", font=("calibri", 15, "bold"), fg="black", bg="#C5EBF6").place(x=100, y=70)
         self.e_s_code= Entry(self.newroot,font=("calibri", 15), bg="white")
         self.e_s_code.place(x=100, y=110, width=350, height=35)
         Label(self.newroot, text="Enter QUANTITY of Stock", font=("calibri", 15, "bold"), fg="black", bg="#C5EBF6").place(x=100, y=155)
         self.e_s_quantity = Entry(self.newroot, font=("calibri", 15), bg="white")
         self.e_s_quantity.place(x=100, y=195, width=350, height=35)
         self.s_bt2 = Button(self.newroot, command=self.onClick_sell, text='SELL', font=(
             "times new roman", 13, "bold"), bg="#d4603b", fg="white",relief=GROOVE).place(x=100, y=250, width=350, height=35)
    

    #Sell function
    def onClick_sell(self):
         if self.e_s_code.get() == "" or self.e_s_quantity.get() == "":
             messagebox.showerror( "Error", "All fields are required", parent=self.newroot)
         else:
             try:
                s= Helper.nse.get_quote(self.e_s_code.get())
                if(s==None):
                    messagebox.showerror("Error","Invalid Code", parent=self.newroot)
                    return
                price = s['sellPrice1']
                if(int(self.e_s_quantity.get())<=0 or float(self.e_s_quantity.get())-int(self.e_s_quantity.get())!=0):
                    messagebox.showerror("Error","Enter valid Quantity", parent=self.newroot)
                    return
                req= int(self.e_s_quantity.get())*price

                dec=messagebox.askquestion('Are you sure ?','Funds will be added :'+str(req), parent=self.newroot)
                if(dec == 'yes'):
                     str1 = Helper.sell(self.e_s_code.get(), self.e_s_quantity.get(), self.name, self.fund, self.user_dict)
                     self.ABC.set('FUNDS: '+str(round(self.user_dict[self.name],2)))
                     messagebox.showinfo("Status", str1, parent=self.newroot)
                     self.newroot.destroy()
             except:
                 messagebox.showerror("Error","Only digits are allowed in quantity", parent=self.newroot)

    #Portfolio Button
    def portfolio(self):
        #New Window
        self.newroot = Toplevel()
        self.newroot.focus_force()
        self.newroot.grab_set()
        self.newroot.geometry('600x400+475+240')
        self.newroot.title('Portfolio')
        self.newroot.configure(bg="#4b4a7f")
        photo = Image.open(icon_path)
        self.icon=ImageTk.PhotoImage(photo)
        self.newroot.iconphoto(False, self.icon)
        #Title Frame
        Tframe = Frame(self.newroot, bg='#4b4a7f')
        Tframe.pack(side=TOP,anchor='w',fill=X)
        Label(Tframe, text="STOCKS and Available QUANTITY", font=("calibri", 20, "bold"), fg="black", bg="#C5EBF6", relief=SUNKEN).pack(padx=10, pady=10)
        
        #List of Stock
        first_frame=Frame(self.newroot,bg='red')
        first_frame.pack(side=TOP,fill=BOTH,expand=1)

        Cvas = Canvas(first_frame, bg='#C5EBF6', bd=0)
        Cvas.pack(side=LEFT,fill=BOTH,expand=1)

        scbar=ttk.Scrollbar(first_frame,orient=VERTICAL, command=Cvas.yview)
        scbar.pack(side=RIGHT, fill=Y)

        Cvas.configure(yscrollcommand=scbar.set)
        Cvas.bind('<Configure>',lambda e:Cvas.configure(scrollregion=Cvas.bbox('all')))
        
        second_frame = Frame(Cvas, bg='#C5EBF6')

        Cvas.create_window((60,30),window=second_frame,anchor='nw')
        l1=[]
        l2=[]
        k=0
        for key, value in self.user_dict.items():
           l1.append(key)
           l2.append(str(value))

    
        j=3
        i=1
        while i<len(l1):
            f = Frame(second_frame, bg='#f7cec3')
            f.pack(fill="both",padx=110,pady=10)
            Label(f, text=str(l1[i]),font=("calibri", 18, "bold"), fg="black", bg="#C5EBF6",relief=SUNKEN).pack(side=LEFT,padx=10,pady=10)
            Label(f, text=str(l2[i]), font=("calibri", 18, "bold"), fg="black",bg="#C5EBF6", relief=SUNKEN).pack(side=RIGHT, padx=10, pady=10)
            i+=1
            j+=2

   
    #Logout Button
    def logout(self):
        self.save_home()
        self.root.destroy()

        
        
# Creating object
app = Home()

