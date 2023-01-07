from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import re

class Employee:


    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.wm_iconbitmap("img07.ico")
        self.root.title('Employee Management System')
        self.root.minsize( width=1500, height=790)


        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()
        self.var_married_status=StringVar()
        self.var_phone_number=StringVar()
        self.var_email=StringVar()
        self.var_country=StringVar()
        self.var_address=StringVar()
        self.var_joining_date=StringVar()
        self.var_department=StringVar()
        self.var_comboid_proof=StringVar()
        self.var_id_proof=StringVar()
        self.var_salary=StringVar()


        lbl_title=Label(self.root,text="Employee Management System", font=('times new roman', 30, 'bold'),fg='red')
        lbl_title.place(x=0,y=160,width=1500,height=50)


        # About botton
        About_botton=Button(self.root,text="About",font=('times new roma', 8, 'bold',),width=5,bg='blue',fg="white")
        About_botton.place(x=1360,y=176,width=50,height=25)

        '''                   photo frame                  '''

        frame1 = Frame(self.root,bd=5,relief=GROOVE)
        frame1.place(x=0,y=0,width=1445,height=160)

        #img01
        img01=Image.open('img08.png')
        img01=img01.resize((480,160,),Image.ANTIALIAS)
        self.photo01=ImageTk.PhotoImage(img01)

        self.img001=Label(frame1,image=self.photo01)
        self.img001.place(x=0,y=0,width=480,height=149)


        #img02
        img06=Image.open('img06.jpg')
        img06=img06.resize((535,150,),Image.ANTIALIAS)
        self.photo02=ImageTk.PhotoImage(img06)

        self.img06=Label(frame1,image=self.photo02)
        self.img06.place(x=480,y=0,width=481,height=149)


        #img03
        img033=Image.open('img033.jpg')
        img033=img033.resize((540,160,),Image.ANTIALIAS)
        self.photo033=ImageTk.PhotoImage(img033)

        self.img033=Label(frame1,image=self.photo033)
        self.img033.place(x=950,y=0,width=481,height=149)


        #                Developer Contact
        def Win_Contact():
            self.new_window = Toplevel(self.root)
            self.new_window.geometry("250x100+550+300")
            self.new_window.title("Dev. Contact")
            self.new_window.wm_iconbitmap("img07.ico")
            self.new_window.resizable(False, False)

            lbl_About = Label(self.new_window, text="Developer Name- Satyajay dibya \n Email- Satyajaydibya9@gmail.com ", font=('times new roman', 12, 'bold'),fg='red')
            lbl_About.pack()

        # Dev_Contact botton
        Dev_Contact_botton=Button(self.root,text="Contact",command=Win_Contact, font=('times new roma', 8, 'bold',),width=5,bg='blue',fg="white")
        Dev_Contact_botton.place(x=1360,y=176,width=50,height=25)


        '''                   Left main frame                  '''
        
        main_frame = Frame(self.root,bd=5,relief=GROOVE)
        main_frame.place(x=1,y=230,width=1440,height=605)


        Uppar_frame = LabelFrame(main_frame,bd=5,relief=GROOVE,text='Employee Input Information',font=('times new roman', 20, 'bold'),fg='blue')
        Uppar_frame.place(x=0,y=0,width=750,height=595)


        '''                  line(1)              '''

        #Name (1),
        lbl_name=Label(Uppar_frame,text='Name :',font=('times new roman', 12, 'bold'))
        lbl_name.grid(row=0,column=0,padx=10,pady=7,sticky=W)

        txt_name=ttk.Entry(Uppar_frame,textvariable=self.var_name, width=20, font=('times new roman', 12, 'bold'))
        txt_name.grid(row=0,column=1,padx=2,pady=7)  # padx=2 ka use space dene ke liye, 

        # bind in Call backe function
        #############################################################################
        validate_name=self.root.register(self.checkname)
        txt_name.config(validate='key',validatecommand=(validate_name,'%P'))


        #DOB (2),line(1)
        lbl_DOB=Label(Uppar_frame,text='DOB :',font=('times new roman', 12, 'bold'))
        lbl_DOB.grid(row=0,column=2,padx=10,pady=7,sticky=W) # sticky=W ka use chipka ke rakhne ke liye 
        
        txt_DOB=ttk.Entry(Uppar_frame,textvariable=self.var_dob, width=20, font=('times new roman', 12, 'bold'))
        txt_DOB.grid(row=0,column=3,padx=2,pady=10) 

        '''                    line(2)                   '''

        #Gender (1), line(2)
        lbl_Gender=Label(Uppar_frame,text='Gender :',font=('times new roman', 12, 'bold'))
        lbl_Gender.grid(row=2,column=0,padx=10,pady=7,sticky=W) 
        
        combo_Gender=ttk.Combobox(Uppar_frame,textvariable=self.var_gender,font=('times new roman', 12, 'bold'),width=18,state='readonly')
        combo_Gender['value']=('Female','Male','Other')
        combo_Gender.current(1)
        combo_Gender.grid(row=2,column=1,padx=15,pady=10,sticky=W)


        #Married Status (2)
        lbl_Married_Status=Label(Uppar_frame,text='Married Status :',font=('times new roman', 12, 'bold'))
        lbl_Married_Status.grid(row=2,column=2,padx=10,pady=7,sticky=W)

        combo_Married_Status=ttk.Combobox(Uppar_frame,textvariable=self.var_married_status,font=('times new roman', 12, 'bold'),width=18,state='readonly')
        combo_Married_Status['value']=('Married','UnMarried')
        combo_Married_Status.current(1)
        combo_Married_Status.grid(row=2,column=3,padx=15,pady=10,sticky=W)


        '''                    line(3)                   '''
        # Phone Number (1)
        lbl_Phone_Number=Label(Uppar_frame,text='Phone Number :',font=('times new roman', 12, 'bold'))
        lbl_Phone_Number.grid(row=4,column=0,padx=10,pady=7,sticky=W)

        txt_Phone_Number=ttk.Entry(Uppar_frame,textvariable=self.var_phone_number, width=20, font=('times new roman', 12, 'bold'))
        txt_Phone_Number.grid(row=4,column=1,padx=2,pady=7)

        # bind in Call backe function
        
        validate_Number=self.root.register(self.checknumber)
        txt_Phone_Number.config(validate='key',validatecommand=(validate_Number,'%P'))


        #Email (2)
        lbl_Email=Label(Uppar_frame,text='Email :',font=('times new roman', 12, 'bold'))
        lbl_Email.grid(row=4,column=2,padx=10,pady=7,sticky=W)

        txt_Email=ttk.Entry(Uppar_frame,textvariable=self.var_email, width=20, font=('times new roman', 12, 'bold'))
        txt_Email.grid(row=4,column=3,padx=2,pady=7) 


        '''                   line(4)                  '''


        #Country (1)
        lbl_Country=Label(Uppar_frame,text='Country :',font=('times new roman', 12, 'bold'))
        lbl_Country.grid(row=5,column=0,padx=10,pady=7,sticky=W)

        txt_Country=ttk.Entry(Uppar_frame,textvariable=self.var_country, width=20, font=('times new roman', 12, 'bold'))
        txt_Country.grid(row=5,column=1,padx=2,pady=7)

        #Address (2)
        lbl_Address=Label(Uppar_frame,text='Address :',font=('times new roman', 12, 'bold'))
        lbl_Address.grid(row=5,column=2,padx=10,sticky=W)

        txt_Address=ttk.Entry(Uppar_frame,textvariable=self.var_address, width=20, font=('times new roman', 12, 'bold'))
        txt_Address.grid(row=5,column=3,padx=2,pady=10)

        '''                  line(5)                  '''

        #Joining Date (1)
        lbl_Joining_Date=Label(Uppar_frame,text='Joining Date :',font=('times new roman', 12, 'bold'))
        lbl_Joining_Date.grid(row=6,column=0,padx=10,sticky=W)

        txt_Joining_Date=ttk.Entry(Uppar_frame,textvariable=self.var_joining_date, width=20, font=('times new roman', 12, 'bold'))
        txt_Joining_Date.grid(row=6,column=1,padx=2,pady=10)


        #Department(2)
        lbl_dep=Label(Uppar_frame,text='Department :',font=('times new roman', 12, 'bold'))
        lbl_dep.grid(row=6,column=2,padx=10,pady=7,sticky=W) 
        
        combo_dep=ttk.Combobox(Uppar_frame,textvariable=self.var_department,font=('times new roman', 12, 'bold'),width=18,state='readonly')
        combo_dep['value']=('Select Department','CO','HR', 'Manager', 'Senior Manager','CR Project Manager','Asoosiate WS Engineer','Principle WS Engineer','Security Engineer','Graphics Developer', 'Front-end Developer','Back-end Developer','Full-stack Developer','Data Scientist','Tester',)
        combo_dep.current(0)
        combo_dep.grid(row=6,column=3,padx=15,pady=10,sticky=W)

        '''                  line(6)                  '''

        #ID Proof (1)
        Combo_ID_Proof=ttk.Combobox(Uppar_frame,textvariable=self.var_comboid_proof,font=('times new roman', 11, 'bold'),width=18,state='readonly')
        Combo_ID_Proof['value']=('Select ID Proof','Aadhar','PAN Card','Passport')
        Combo_ID_Proof.current(0)
        Combo_ID_Proof.grid(row=7,column=0,padx=10,sticky=W)
    
        txt_ID_Proof=ttk.Entry(Uppar_frame,textvariable=self.var_id_proof, width=20, font=('times new roman', 12, 'bold'))
        txt_ID_Proof.grid(row=7,column=1,padx=2,pady=10)


        #Salary(CTC) (2)
        lbl_Salary=Label(Uppar_frame,text='Salary (CTC) :',font=('times new roman', 12, 'bold'))
        lbl_Salary.grid(row=7,column=2,padx=10,pady=7,sticky=W)

        txt_Salary=ttk.Entry(Uppar_frame,textvariable=self.var_salary, width=20, font=('times new roman', 12, 'bold'))
        txt_Salary.grid(row=7,column=3,padx=2,pady=7) 

        # bind Call backe function in Salary
        ##################################################################

        validate_Number=self.root.register(self.checknumber)
        txt_Salary.config(validate='key',validatecommand=(validate_Number,'%P'))



        # left img frame
        leftimg_frame = LabelFrame(Uppar_frame,bd=5,relief=GROOVE)
        leftimg_frame.place(x=30,y=310,width=450,height=200)

        #img04
        img04=Image.open('img10.jpg')
        img04=img04.resize((440,190,),Image.ANTIALIAS)
        self.photo04=ImageTk.PhotoImage(img04)

        self.img04=Label(leftimg_frame,image=self.photo04)
        self.img04.place(x=0,y=0,width=438,height=188)


        '''                 Button frame                    '''

        # Button frame
        Button_frame = LabelFrame(Uppar_frame,bd=5,relief=GROOVE)
        Button_frame.place(x=538,y=310,width=170,height=200)

        ############################################################################## 

        # Save button
        btn_Save_add=Button(Button_frame,text="Save",command=self.add_data,font=("arial",13, "bold"), bg='green', fg='white', width=14)
        btn_Save_add.grid(row=0,column=0,padx=4,pady=4)

        # Update button
        btn_Update_add=Button(Button_frame,text="Update",command=self.update_data,font=("arial",13, "bold"), bg='blue', fg='white', width=14)
        btn_Update_add.grid(row=1,column=0,padx=4,pady=10)

        # Delete button
        btn_Delete_add=Button(Button_frame,text="Delete",command=self.Delete_data,font=("arial",13, "bold"), bg='red', fg='white', width=14)
        btn_Delete_add.grid(row=2,column=0,padx=4,pady=10)

        # Reset button
        btn_Delete_add=Button(Button_frame,command=self.reset_data,text="Reset",font=("arial",13, "bold"), bg='azure', fg='black', width=14)
        btn_Delete_add.grid(row=3,column=0,padx=4,pady=4)


        '''                  Right frame                   '''

        Down_frame = LabelFrame(main_frame,bd=5,relief=GROOVE,text="Employee info :", font=('times new roman', 20, 'bold', ),fg='blue')
        Down_frame.place(x=750,y=0,width=680,height=595)


        #Search frame
        Search_frame = LabelFrame(Down_frame,bd=5,relief=GROOVE,text="  Search Employee  ",font=('times new roman', 15, 'bold'),fg='green')
        Search_frame.place(x=0,y=0,width=670,height=60)

        #Search_to
        Search_to=Label(Search_frame, text=' Search To ', font=('times new roma', 10, 'bold',),bg="red",fg="white")
        Search_to.grid(row=0,column=0,padx=2,pady=0)


        #Search Combobox
        self.var_com_search=StringVar()
        combo_Search=ttk.Combobox(Search_frame,textvariable=self.var_com_search,state="readonly",font=('times new roma', 10, 'bold',),width=10)
        combo_Search['value']=("Name","ID_Proof")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2,pady=0)

        #Search to text
        self.var_search=StringVar()
        txt_Searchbox=ttk.Entry(Search_frame,textvariable=self.var_search,font=('times new roma', 10, 'bold',))
        txt_Searchbox.grid(row=0,column=2,padx=2,pady=0)

        #############################################################################
        # Search botton
        Search_botton=Button(Search_frame,command=self.Search_data,text="Search",font=('times new roma', 8, 'bold',),width=10,bg='blue',fg="white")
        Search_botton.grid(row=0,column=3,padx=5,pady=0)

        #Show all botton
        Show_all_botton=Button(Search_frame,command=self.fetch_data,text="Show All",font=('times new roma', 8, 'bold',),width=10,bg='blue',fg="white")
        Show_all_botton.grid(row=0,column=4,padx=5,pady=0)


        '''                  Employee Table                  '''

        Employee_Table = Frame(Down_frame,bd=5,relief=GROOVE)
        Employee_Table.place(x=1,y=60,width=670,height=495)


        '''                  Scroll Bar                 '''
        scroll_x=ttk.Scrollbar(Employee_Table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Employee_Table,orient=VERTICAL)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.Employee_Table=ttk.Treeview(Employee_Table,column=("Name","DOB","Gender", "Married_Status","Phone_Number","Email", "Country", "Address", "Joining_Date","Department", "Combo_ID_Proof","ID_Proof", "Salary"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        


        scroll_x.config(command=self.Employee_Table.xview)
        scroll_y.config(command=self.Employee_Table.yview)


        '''                  Employee info : litle bar                '''

        self.Employee_Table.heading('Name',text='Name')
        self.Employee_Table.heading('DOB',text='DOB')
        self.Employee_Table.heading('Gender',text='Gender')
        self.Employee_Table.heading('Married_Status',text='Married Status')
        self.Employee_Table.heading('Phone_Number',text='Phone Number')
        self.Employee_Table.heading('Email',text='Email')
        self.Employee_Table.heading('Country',text='Country')
        self.Employee_Table.heading('Address',text='Address')
        self.Employee_Table.heading('Joining_Date',text='Joining Date')
        self.Employee_Table.heading('Department',text='Department')
        self.Employee_Table.heading('Combo_ID_Proof',text='Type of Proof')
        self.Employee_Table.heading('ID_Proof',text='ID Proof')
        self.Employee_Table.heading('Salary',text='Salary')

        # Employee info : litle bar heading dene ke liye 
        self.Employee_Table['show']='headings' 

        self.Employee_Table.pack(fill=BOTH,expand=1,)

        # Employee info : litle bar heading ko whdth dene ke liye  
        self.Employee_Table.column("Name",width=100,)
        self.Employee_Table.column("DOB",width=100,)
        self.Employee_Table.column("Gender",width=100,)
        self.Employee_Table.column("Married_Status",width=100,)
        self.Employee_Table.column("Phone_Number",width=100,)
        self.Employee_Table.column("Email",width=100,)
        self.Employee_Table.column("Country",width=100,)
        self.Employee_Table.column("Address",width=100,)
        self.Employee_Table.column("Joining_Date",width=100,)
        self.Employee_Table.column("Department",width=100,)
        self.Employee_Table.column("Combo_ID_Proof",width=100,)
        self.Employee_Table.column("ID_Proof",width=100,)
        self.Employee_Table.column("Salary",width=100,)

        self.fetch_data()
        '''                  Data ko input box ke sath bind karne ke liye           '''
        self.Employee_Table.bind("<ButtonRelease>",self.get_cursor)


        '''         Call back function in Input time validetion       '''




        #validate in name

    def checkname(self,name):
        if name.isalpha() and len(name) <=20:
            return True
        if name=="":
            return True
        else:
            messagebox.showerror('Invalid', 'Not Allowed : '+name[-1])
            return False



    #validate in Number 
    
    def checknumber(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            messagebox.showerror("Invalid",'Invalid Entry')
            return False



        ''' Regex module Email ID validetion '''

    def checkemail(self,var_email):
        if len(var_email)>7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",var_email):
                return True
            else:
                messagebox.showwarning('Alert','Invalid Email ID Please Input Valid Email ID ')
                return False
        messagebox.showinfo('Invalid','Email length is too Small')


        '''                   Oprations of Bottons                  '''


        # Data add karne ke liye or validetion 
    def add_data(self):
        x=0

        if self.var_name.get()=='':
            messagebox.showerror('Error', 'Please Input Name', parent=self.root)

        elif self.var_dob.get()=='':
            messagebox.showerror('Error', 'Please Input Date Of Birth', parent=self.root)

        elif self.var_gender.get()=='':
            messagebox.showerror('Error', 'Please Input Gender', parent=self.root)

        elif self.var_married_status.get()=='':
            messagebox.showerror('Error', 'Please Input Married Status', parent=self.root)

        elif self.var_phone_number.get()=='':
            messagebox.showerror('Error', 'Please Input Phone Number', parent=self.root)

        elif self.var_email.get()=='':
            messagebox.showerror('Error', 'Please Input Email ID', parent=self.root)

        elif self.var_country.get()=='':
            messagebox.showerror('Error', 'Please Input Country Name', parent=self.root)

        elif self.var_address.get()=='':
            messagebox.showerror('Error', 'Please Input Address', parent=self.root)

        elif self.var_joining_date.get()=='':
            messagebox.showerror('Error', 'Please Input Joining Date', parent=self.root)

        elif self.var_department.get()=='Select Department':
            messagebox.showerror('Error', ' Please Select Department', parent=self.root)

        elif self.var_comboid_proof.get()=='Select ID Proof':
            messagebox.showerror('Error', 'Please Select ID Proof', parent=self.root)

        elif self.var_id_proof.get()=='':
            messagebox.showerror('Error', 'Please Input ID Number', parent=self.root)

        elif self.var_salary.get()=='':
            messagebox.showerror('Error', 'Please Input Salary', parent=self.root)

        elif self.var_email.get()!=None:
            x = self.checkemail(self.var_email.get())
        if (x == True):
                try:
                   conn = mysql.connector.connect(host='localhost',username='root',password='Saty@777',database='mydata')
                   my_cursor=conn.cursor()
                   my_cursor.execute('insert into Employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                                           self.var_name.get(),
                                                                                                           self.var_dob.get(),
                                                                                                           self.var_gender.get(),
                                                                                                           self.var_married_status.get(),
                                                                                                           self.var_phone_number.get(),
                                                                                                           self.var_email.get(),
                                                                                                           self.var_country.get(),
                                                                                                           self.var_address.get(),
                                                                                                           self.var_joining_date.get(),
                                                                                                           self.var_department.get(),
                                                                                                           self.var_comboid_proof.get(),
                                                                                                           self.var_id_proof.get(),
                                                                                                           self.var_salary.get(),

                                                                                                          ))
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo('Success','Employee Data Add Success',parent=self.root)
                except Exception as es:
                   messagebox.showerror('Error',f'Dut To:{str(es)}',parent=self.root)


    '''                  fetch Dat                    '''
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='Saty@777',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.Employee_Table.delete(*self.Employee_Table.get_children())
            for i in data:
                self.Employee_Table.insert("",END,values=i)
        
        conn.commit()
        conn.close()
    

    '''                 Data ko input box me fatch karne ke liye               '''

    def get_cursor(self,event=""):
        cursor_row=self.Employee_Table.focus()
        content=self.Employee_Table.item(cursor_row)
        data=content['values']

        self.var_name.set(data[0])
        self.var_dob.set(data[1])
        self.var_gender.set(data[2])
        self.var_married_status.set(data[3])
        self.var_phone_number.set(data[4])
        self.var_email.set(data[5])
        self.var_country.set(data[6])
        self.var_address.set(data[7])
        self.var_joining_date.set(data[8])
        self.var_department.set(data[9])
        self.var_comboid_proof.set(data[10])
        self.var_id_proof.set(data[11])
        self.var_salary.set(data[12])

    '''        Update Button        '''
    def update_data(self):
        if self.var_department.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error', 'All Fields Are Required')
        else:
            try:
                update=messagebox.askyesno('Updata','Are you sure')
                if update>0:
                    conn = mysql.connector.connect(host='localhost',username='root',password='Saty@777',database='mydata')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update employee set Name=%s,DOB=%s,Gender=%s,Married_Status=%s,Phone_Number=%s,Email=%s,Country=%s,Address=%s,Joining_Date=%s,Department=%s,Combo_ID_Proof=%s,Salary=%s where ID_Proof=%s',(

                                                                                                                                                                                                                                 self.var_name.get(),
                                                                                                                                                                                                                                 self.var_dob.get(),
                                                                                                                                                                                                                                 self.var_gender.get(),
                                                                                                                                                                                                                                 self.var_married_status.get(),
                                                                                                                                                                                                                                 self.var_phone_number.get(),
                                                                                                                                                                                                                                 self.var_email.get(),
                                                                                                                                                                                                                                 self.var_country.get(),
                                                                                                                                                                                                                                 self.var_address.get(),
                                                                                                                                                                                                                                 self.var_joining_date.get(),
                                                                                                                                                                                                                                 self.var_department.get(),
                                                                                                                                                                                                                                 self.var_comboid_proof.get(),
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                 self.var_salary.get(),
                                                                                                                                                                                                                                 self.var_id_proof.get(),

                                                                                                                                                                                                                                ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Employee Data Update Success', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Dut To:{str(es)}',parent=self.root)


         # '''         Delete Button        '''
    def Delete_data(self):
        if self.var_id_proof.get()=="":
            messagebox.showerror('Error', "All fields are required")
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure',parent=self.root)
                if Delete>0:
                    conn = mysql.connector.connect(host='localhost',username='root',password='Saty@777',database='mydata')
                    my_cursor=conn.cursor()
                    sql= 'DELETE FROM mydata.employee WHERE ID_Proof = %s'
                    value=(self.var_id_proof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                      return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete', 'Employee Data Deleted Success', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Dut To:{str(es)}',parent=self.root)


        '''                   Reset Button                  '''

    def reset_data(self):
        self.var_name.set("")
        self.var_dob.set("")
        self.var_gender.set("Male")
        self.var_married_status.set("UnMarried")
        self.var_phone_number.set("")
        self.var_email.set("")
        self.var_country.set("")
        self.var_address.set("")
        self.var_joining_date.set("")
        self.var_department.set("Select Department")
        self.var_comboid_proof.set("Select ID Proof")
        self.var_id_proof.set("")
        self.var_salary.set("")


        '''                   Search Button                  '''
    def Search_data(self):
        if self.var_search.get()=='':
            messagebox.showerror('Error','Please Enter Name or Id proof ')
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='Saty@777',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from employee where ' +str(self.var_com_search.get())+ " LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.Employee_Table.delete(*self.Employee_Table.get_children())
                    for i in rows:
                        self.Employee_Table.insert("",END,values=i)
                conn.commit
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Dut To:{str(es)}',parent=self.root)
                


if __name__=="__main__":
 root=Tk()
 obj=Employee(root)
 root.mainloop()