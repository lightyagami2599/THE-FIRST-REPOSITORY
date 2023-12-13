# hospital management system 
from msilib.schema import SelfReg
from tkinter import*
from tkinter import ttk
import random 
import time
import datetime
from tkinter import messagebox
from turtle import update
from typing import Self
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital management System")
        self.root.geometry("1540x800+0+0")


        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.dose=StringVar()
        self.numberoftablets=StringVar()
        self.lot=StringVar()
        self.issuedate=StringVar()
        self.expdate=StringVar()
        self.dailydose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.BloodPressure=StringVar()
        self.StorageAdvice=StringVar()
        self.Medication=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        



        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)


        #================================================Dataframe==================================================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)

        #=======================================buttons frame========================================================


        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)


         #=======================================details frame========================================================


        detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        detailsframe.place(x=0,y=600,width=1530,height=190)

        #================================================DataframeLeft==================================================

        lblNameTablet=Label(DataframeLeft,text="Names of tablet",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="readonly",font=("arial",12,"bold"),width=33)
        comNametablet["values"]=("Doxorubicin","Nitroglycerin","Glimpiride","Acebrophylline","Fabflu","Amphot","Ericin","Aclidinium","L-Ornithine" "L-Aspartate","Loperamide")
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Refrence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1) 

        lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOfTablets=Label(DataframeLeft,font=("arial",12,"bold"),text="No of Tablets:",padx=2,pady=6)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.numberoftablets,width=35)
        txtNoOfTablets.grid(row=3,column=1) 

        lblLot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.lot,width=35)
        txtLot.grid(row=4,column=1)     

        lblIssueDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.issuedate,width=35)
        txtIssueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.expdate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.dailydose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.sideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInformation=Label(DataframeLeft,font=("arial",12,"bold"),text="Further Information:",padx=2,)
        lblFurtherInformation.grid(row=0,column=2,sticky=W)
        txtFurtherInformation=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherInformation.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.BloodPressure,width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorageAdvice=Label(DataframeLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorageAdvice.grid(row=2,column=2,sticky=W)
        txtStorageAdvice=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.StorageAdvice,width=35)
        txtStorageAdvice.grid(row=2,column=3)

        lblMedication=Label(DataframeLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedication.grid(row=3,column=2,sticky=W)
        txtMedication=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Medication,width=35)
        txtMedication.grid(row=3,column=3)

        lblPatientID=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient ID:",padx=2,pady=6)
        lblPatientID.grid(row=4,column=2,sticky=W)
        txtPatientID=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientId,width=35)
        txtPatientID.grid(row=4,column=3)

        lblNHSNumber=Label(DataframeLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNHSNumber.grid(row=5,column=2,sticky=W)
        txtNHSNumber=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.nhsNumber,width=35)
        txtNHSNumber.grid(row=5,column=3)

        lblPatientName=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=6,column=3)

        lblDateOfBirth=Label(DataframeLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DateOfBirth,width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)

        #=========================================================DataFrameRight=================================================
        self.txtprescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtprescription.grid(row=0,column=0)


        #==========================================Buttons========================================================================
        btnPrescription=Button(Buttonframe,command=self.iPrectioption,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=28
        ,padx=4,pady=5)
        btnPrescription.grid(row=0,column=1)

        btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=28,padx=4,pady=5)
        btnPrescriptionData.grid(row=0,column=2)

        

        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=28,padx=4,pady=5)
        btnDelete.grid(row=0,column=4)

        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=28,padx=4,pady=5)
        btnClear.grid(row=0,column=5)

        btnExit=Button(Buttonframe,command=self.iExit,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=28,padx=4,pady=5)
        btnExit.grid(row=0,column=6)
        



        #===================================================Tables=================================================================
        #=====================================================Scrolbar=============================================================
        scroll_x=ttk.Scrollbar(detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(detailsframe,columns=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name OF Table")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="Name OF Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHSNUMBER")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.pack(fill=BOTH,expand=1)
        
        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()

        #===========================================functionality declation================================================
    def iPrescriptionData(self) :
        if  self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="vibhu",database="Mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                         self.Nameoftablets.get(),
                                                                                                         self.ref.get(),
                                                                                                         self.dose.get(),
                                                                                                         self.numberoftablets.get(),       
                                                                                                         self.lot.get(),
                                                                                                         self.issuedate.get(),
                                                                                                         self.expdate.get(),
                                                                                                         self.dailydose.get(),
                                                                                                         self.StorageAdvice.get(),
                                                                                                         self.nhsNumber.get(),
                                                                                                         self.PatientName.get(),
                                                                                                         self.DateOfBirth.get(),
                                                                                                         self.PatientAddress.get(),
                                                                                                        
                                                                                                        ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("sucess","record has been inserted")
    
    
    
    
    
    
    
    
    def fatch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="vibhu",database="Mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from hospital")
                row=my_cursor.fetchall()
                if len(row)!=0:
                    self.hospital_table.delete(*self.hospital_table.get_children())
                    for i in row:
                        self.hospital_table.insert("",END,values=i)
                    conn.commit()
                conn.close()


    def get_cursor(self,event=""):
                cursor_row=self.hospital_table.focus()
                content=self.hospital_table.item(cursor_row)
                row=content["values"]
                self.Nameoftablets.set(row[0])
                self.ref.set(row[1])
                self.dose.set(row[2])
                self.numberoftablets.set(row[3])
                self.lot.set(row[4])
                self.issuedate.set(row[5])
                self.expdate.set(row[6])
                self.dailydose.set(row[7])
                self.StorageAdvice.set(row[8])
                self.nhsNumber.set(row[9])
                self.PatientName.set(row[10])
                self.DateOfBirth.set(row[11])
                self.PatientAddress.set(row[12])

    def iPrectioption(self):
        self.txtprescription.insert(END,"Name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtprescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtprescription.insert(END,"Dose:\t\t\t"+self.dose.get()+"\n")
        self.txtprescription.insert(END,"Number of Tablets:\t\t\t"+self.numberoftablets.get()+"\n")
        self.txtprescription.insert(END,"Lot:\t\t\t"+self.lot.get()+"\n")
        self.txtprescription.insert(END,"Issue Date:\t\t\t"+self.issuedate.get()+"\n")
        self.txtprescription.insert(END,"Exp date:\t\t\t"+self.expdate.get()+"\n")
        self.txtprescription.insert(END,"Daily Dose:\t\t\t"+self.dailydose.get()+"\n")
        self.txtprescription.insert(END,"Side Effect:\t\t\t"+self.sideEffect.get()+"\n")
        self.txtprescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtprescription.insert(END,"Driving Using Machine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtprescription.insert(END,"Patient Id:\t\t\t"+self.PatientId.get()+"\n")
        self.txtprescription.insert(END,"NHS Number:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtprescription.insert(END,"Date Of Birth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtprescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get()+"\n")

    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="vibhu",database="Mydata")
        my_cursor=conn.cursor()
        query="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")


    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.dose.set("")
        self.numberoftablets.set("")
        self.lot.set("")
        self.issuedate.set("")
        self.expdate.set("")
        self.dailydose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.BloodPressure.set("")
        self.StorageAdvice.set("")
        self.Medication.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtprescription.delete("1.0",END)
    
    
    def iExit(self):
        iExit=messagebox.askyesno("Hospital management system","confirm you want to exit")
        if iExit>0:
            root.destroy()
            return




        

        





        

root=Tk()
ob=Hospital(root)
root.mainloop()   
