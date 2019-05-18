
from tkinter import *
from PIL import ImageTk, Image
import os
import pandas as pd
import math

# In[146]:

import dt_ac_aztro as dt1
import dt_ac_cefta as dt2
import dt_ent_tetra as dt3
import dt_ent_cipro as dt4
import dt_kpn_gent as dt5
import dt_kpn_mero as dt6
import dt_eco_cot as dt7
import dt_eco_imp as dt8
import dt_pae_amika as dt9
import dt_pae_cefe as dt10
import dt_sau_eryth as dt11
import dt_sau_peni as dt12


# In[147]:

creds = 'doc.csv'
pat_db= 'pat_db.csv'
global df
df = pd.read_csv('pat_history.csv')
f1=0
f2=0

global count
count = 0

rootAf=0
dashf=0

global R_Drugs, S_Drugs
global R_res_lst,S_res_lst
R_res_lst=[]
S_res_lst=[]
R_Drugs=[]
S_Drugs=[]

def strtolist(stri):
    lis=[]
    var=''
    for i in stri:
        if i!=',':
            var=var+i
        else:
            lis.append(var)
            var=''
    lis.append(var)
    return lis

# In[148]:

def doc_dash_dum():
    rootA.destroy()
    doc_dash()


# In[149]:

def Signup(): 
    
    rootA.destroy()
    
    global pwordE 
    global usernameE
    global docNameE
    global hospitalE
    global roots
    #global signupButton
 
    roots = Tk()
    roots.title('Signup')
    roots.geometry('1300x740')
    flag=0
    
    img_1 = ImageTk.PhotoImage(Image.open("alpha.jpg"))
    imglabel_1 = Label(roots, image=img_1)
    imglabel_1.place(x=0, y=0) 
    
    intruction = Label(roots, text='''Please Enter new Doctor's Credentials\n''', font=('Courier',15), bg='white')
    intruction.place(x=670, y=100)
    docNameL = Label(roots, text='Doctor Name: ', bg='white' , font = 30)
    docNameL.place(x=750, y=170)
    hospitalL = Label(roots, text='Hospital Name: ', bg='white' , font = 30)
    hospitalL.place(x=750, y=220)
    usernameL = Label(roots, text='Username: ', bg='white' , font = 30)
    usernameL.place(x=750, y=270)
    pwordL = Label(roots, text='Password: ', bg='white' , font = 30)
    pwordL.place(x=750, y=320)
    
    docNameE = Entry(roots)
    docNameE.place(x=900, y=170) 
    hospitalE = Entry(roots)
    hospitalE.place(x=900, y=220) 
    usernameE = Entry(roots)
    usernameE.place(x=900, y=270) 
    pwordE = Entry(roots, show='*')
    pwordE.place(x=900, y=320)
    
    signupButton = Button(roots, text='Signup', bg='white' , font = 40)
    signupButton.place(x=1000, y=370)
    signupButton.bind('<Button-1>',onclicksignup)
    
    backButton = Button(roots, text='Back', bg='white' , font = 40, command=backSignUp)
    backButton.place(x=850, y=370)
    
    roots.mainloop()


# In[150]:

def onclicksignup(event):
    if not docNameE.get() or not hospitalE.get() or not usernameE.get() or not pwordE.get():
        label = Label(roots, text = 'Please fill all details', fg ='red' , font =30)
        label.place(x=900, y=420)
    else:
        FSSignup()


# In[151]:

def backSignUp():
    if roots:
        roots.destroy()
        Login()


# In[152]:

def FSSignup():
    with open(creds, 'a') as f:
        data = [[docNameE.get(),hospitalE.get(),usernameE.get(),pwordE.get()]]
        df = pd.DataFrame(data)
        df.to_csv(f, header=False)
 
    roots.destroy()
    Login()


# In[153]:

def Login():
    global nameEL
    global pwordEL
    global rootA
    
    rootA = Tk()
    rootA.title('Login')
    rootA.geometry('1300x740')    
    img_1 = ImageTk.PhotoImage(Image.open("alpha.jpg"))
    imglabel_1 = Label(rootA, image=img_1)
    imglabel_1.place(x=0, y=0)
    intruction = Label(rootA, text='Please Login\n',  font=('Courier',25), bg='white')
    intruction.place(x=850, y=100)
    nameL = Label(rootA, text='Username: ', bg='white' , font = 30)
    pwordL = Label(rootA, text='Password: ', bg='white' , font = 30)
    nameL.place(x=750, y=170)
    pwordL.place(x=750, y=220)
 
    nameEL = Entry(rootA) 
    pwordEL = Entry(rootA, show='*')
    nameEL.place(x=900, y=170)
    pwordEL.place(x=900, y=220)
 
    loginB = Button(rootA, text='Login', bg='white' , font = 40, command=CheckLogin)
    loginB.place(x=800, y=270)
 
    signuser = Button(rootA, text='Sign Up', bg='white' , font = 40, command=Signup)
    signuser.place(x=950, y=270)
    rootA.mainloop()


# In[154]:

def CheckLogin():
    
    global docName
    
    df=pd.read_csv(creds)
    usernm=nameEL.get()
    passwrd=pwordEL.get()
    
    f1=0
    f2=0
    for i in range(len(df)):
        if df.loc[i,'Username']==usernm:
            f1=1
        if df.loc[i,'Password']==passwrd:
            f2=1
        if f1==1 and f2==1:
            doc_dash_dum()
            docName=df.loc[i,'DoctorName']
            #print(docName)
            break  
    if f1==0 or f2==0:
        rlbl = Label(rootA, text= 'Invalid User Name or Password', font=50, fg='red')
        rlbl.place(x=750, y=370)


# In[155]:

def doc_dash():
    
    
    global dash,patIdEntry1,patIdEntry2,patSexEntry2,patAgeEntry2,patNameEntry1,patNameEntry2
    global label
    
    dash = Tk()
    dash.title('Doctor\'s Dashboard')
    dash.geometry('1300x740')
    img_2 = ImageTk.PhotoImage(Image.open("alpha.jpg"))
    imglabel_2 = Label(dash, image=img_2)
    imglabel_2.place(x=0, y=0)
    rlbl1 = Label(dash, text='Old Patient ', font=('Courier',25), bg='white')
    rlbl1.place(x=150, y=70)
    patID1 = Label(dash, text='Patient ID: ', bg='white' , font = 30)
    patID1.place(x=100, y=170)
    patNAME1 = Label(dash, text='Patient name: ', bg='white' , font = 30)
    patNAME1.place(x=100, y=220)
    
    patIdEntry1 = Entry(dash)
    patIdEntry1.place(x=300, y=170)
    patNameEntry1 = Entry(dash)
    patNameEntry1.place(x=300, y=220)
    
    myvarId = StringVar()
    myvarName = StringVar() 
    myvarAge = StringVar()
    myvarSex = StringVar() 
    myvarOrg = StringVar()
    
    myvarId.set('''eg. 00000''')
    myvarName.set('''eg. Dinesh''')
    myvarAge.set('''eg. 00''')
    myvarSex.set('M/F/O')
    
    rlbl2 = Label(dash, text='New Patient ', font=('Courier',25), bg='white')
    rlbl2.place(x=850, y=70)
    patID2 = Label(dash, text='Patient ID: ', bg='white' , font = 30)
    patID2.place(x=800, y=170)
    patNAME2 = Label(dash, text='Patient Name: ', bg='white' , font = 30)
    patNAME2.place(x=800, y=220)
    patAge2 = Label(dash, text='Patient Age: ', bg='white' , font = 30)
    patAge2.place(x=800, y=270)
    patSex2 = Label(dash, text='Patient Sex: ', bg='white' , font = 30)
    patSex2.place(x=800, y=320)
    
    
    patIdEntry2 = Entry(dash,textvariable=myvarId)
    patIdEntry2.place(x=950, y=170)
    patNameEntry2 = Entry(dash,textvariable=myvarName)
    patNameEntry2.place(x=950, y=220)
    patAgeEntry2 = Entry(dash,textvariable=myvarAge)
    patAgeEntry2.place(x=950, y=270)
    patSexEntry2 = Entry(dash,textvariable=myvarSex)
    patSexEntry2.place(x=950, y=320)
    
    patIdEntry2.bind('<Button-1>', on_click)
    patNameEntry2.bind('<Button-1>', on_click)
    patAgeEntry2.bind('<Button-1>', on_click)
    patSexEntry2.bind('<Button-1>', on_click)
    
    
    label = Label(dash, text='', font=30,fg='red')
    label.place(x=300, y=420)    
        
    
    patRegButton = Button(dash, text='Enter', bg='white' , font = 40)
    patRegButton.place(x=350, y=270)
    patRegButton.bind('<Button-1>', reg_click)
    
    patAddButton = Button(dash, text='Add', bg='white' , font = 40)
    patAddButton.place(x=950, y=370)
    patAddButton.bind('<Button-1>', add_click)
    
    logoutButton = Button(dash, text='Logout', bg='white' , fg='red', font = 40, command=logout_1)
    logoutButton.place(x=1050, y=500)
    
    dash.mainloop()   


# In[156]:

def reg_click(event):
    if not patIdEntry1.get() or not patNameEntry1.get():
        label.config(text='Please fill all details', font=30,fg='red')
    else:
        CheckPat()


# In[157]:

def add_click(event):
    global f1,f2,NewPatName, NewPatId, NewPatAge, NewPatSex
    
    f1=0
    f2=1
    flag=0
    NewPatName=patNameEntry2.get()
    NewPatId=patIdEntry2.get()
    NewPatAge=patAgeEntry2.get()
    NewPatSex=patSexEntry2.get()
    
    label = Label(dash, text='')
    with open(pat_db,'a') as f:
        df_fr_rd = pd.read_csv(pat_db)
        
    for i in range(len(df_fr_rd)):
        if int(df_fr_rd.loc[i,'ID'])==int(NewPatId):
                flag=1
    if flag==1:
        label.config(text='Patient ID exist', font=10,fg='red')
        label.place(x=800, y=450)
    
    if (NewPatName=='''eg. Dinesh''' or NewPatId=='''eg. 00000''' or NewPatAge=='''eg. 00''' or NewPatSex=='M/F/O') and flag!=1:
        flag=2
    
                
    if flag==2:    
        label.config(text='Please fill all details', font=30,fg='red')
        label.place(x=800, y=450)
    
    elif flag==0:
        add_pat()
        pat_dash()


# In[158]:

def logout_1():
    if dash:
        dash.destroy()
        Login()


# In[159]:

def add_pat():
    with open(pat_db,'a') as f:
        df_fr_rd = pd.read_csv(pat_db)
        data = [[NewPatId, NewPatName, NewPatAge, NewPatSex]]
        df = pd.DataFrame(data)
        df.to_csv(f, header=False)
    return


# In[160]:

def CheckPat():
    global OldPatName, OldPatId, OldPatAge, OldPatSex,patId,patName,f1,f2
    patId=int(patIdEntry1.get())
    patName=patNameEntry1.get()
    flag1 = 0
    flag2 = 1
    
    with open(pat_db,'a') as f:
        df_fr_rd = pd.read_csv(pat_db)
        
        for i in range(len(df_fr_rd)):
            if int(df_fr_rd.loc[i,'ID'])==patId and df_fr_rd.loc[i,'Name']==patName:
                f1 = 1
                OldPatName=patName
                OldPatId=patId
                OldPatAge=df_fr_rd.loc[i,'Age']
                OldPatSex=df_fr_rd.loc[i,'Sex']
                break
         
        if f1 != 1:
            label.config(text='Patient not found, check details', font=30,fg='red')
        else:
            pat_dash()
            
 


# In[161]:

def pat_dash():
    dash.destroy()
    global r,f1,f2,index
    global R_Drugs, S_Drugs
    global R_res_lst,S_res_lst
    global doc_submit
    r = Tk()
    r.title('Doctor\'s Dashboard')
    r.geometry('1300x740')
    img_2 = ImageTk.PhotoImage(Image.open("alpha.jpg"))
    imglabel_2 = Label(r, image=img_2)
    imglabel_2.place(x=0, y=0)
    rlbl = Label(r, text='Welcome Doctor', font=('Courier',25), bg='white')
    rlbl.place(x=150, y=70)
    
    patID = Label(r, text='Patient ID: ', bg='white' , font = 30)
    patID.place(x=100, y=170)
    
    patNAME = Label(r, text='Patient name: ', bg='white' , font = 30)
    patNAME.place(x=450, y=170)
    
    patAGE = Label(r, text='Patient Age: ', bg='white' , font = 30)
    patAGE.place(x=850, y=170)
    
    patSEX = Label(r, text='Patient Sex: ', bg='white' , font = 30)
    patSEX.place(x=100, y=250)
    
    patORG = Label(r, text='Organism: ', bg='white' , font = 30)
    patORG.place(x=450, y=250)
    
    global patORGEL,patAGEEL,patSEXEL
   
    myvarId = StringVar()
    myvarName = StringVar() 
    myvarAge = StringVar()
    myvarSex = StringVar() 
    myvarOrg = StringVar()
    myvarOrg.set("Refer key")
    
    if f1==1:
        
        myvarId.set(OldPatId)
        myvarName.set(OldPatName)
        myvarAge.set(OldPatAge)
        myvarSex.set(OldPatSex)
        
        for i in range(len(df)):
        	if int(df.loc[i,'ID'])==OldPatId:
		        R_Drugs=strtolist(df.loc[i,'R_Drugs'])
		        if not (df.loc[i,'S_Drugs']):
		            S_Drugs=[]
		        else:
		            S_Drugs=strtolist(df.loc[i,'S_Drugs'])
		        index=i
		        break
        		
        RDrugs = ','.join(map(str, R_Drugs))
        SDrugs = ','.join(map(str, S_Drugs))
		
        rLabel = Label(r, text='Previously Resistant Drugs : '+RDrugs, bg='white',font = 40)
        rLabel.place(x= 400,y = 450)
        sLabel = Label(r, text='Previously Sensitive Drugs : '+SDrugs, bg='white',font = 40)
        sLabel.place(x= 400,y = 550)
        
    elif f2==1:
        
        myvarId.set(NewPatId)
        myvarName.set(NewPatName)
        myvarAge.set(NewPatAge)
        myvarSex.set(NewPatSex)
           
        
    patIDEL = Entry(r, textvariable = myvarId)
    
    patIDEL.place(x=210, y=170) 
    patNAMEEL = Entry(r, textvariable = myvarName)
    patNAMEEL.place(x=600, y=170)
    patAGEEL = Entry(r, textvariable = myvarAge)
    patAGEEL.place(x=1000, y=170)
    patSEXEL = Entry(r, textvariable = myvarSex)
    patSEXEL.place(x=210, y=250)
    patIDEL.config(state='disabled')
    patNAMEEL.config(state='disabled')
    patAGEEL.config(state='disabled')
    patSEXEL.config(state='disabled')
    
    patORGEL = Entry(r, textvariable = myvarOrg)
    patORGEL.place(x=600, y=250)
    patORGEL.bind('<Button-1>', on_click)
    
    key=Label(r,text='Key:',bg='white' )
    key.place(x=50,y=550)
    img_1 = ImageTk.PhotoImage(Image.open("key.png"))
    imglabel_1 = Label(r, image=img_1)
    imglabel_1.place(x=10, y=570) 

    doc_submit = Button(r, text='  Next ', bg='white' , font = 20, command= sel_tar_drug)
    doc_submit.place(x=950, y=250)
    backbttn = Button(r, text='Back', bg='white' , font = 20,command=backpatdash)
    backbttn.place(x=1100, y=250)

    logoutButton = Button(r, text='Logout', bg='white' , fg='red', font = 40, command=logout_2)
    logoutButton.place(x=1050, y=500)
    r.mainloop()


# In[162]:

def logout_2():
    global count
    global RDrugs, SDrugs, R_Drugs, S_Drugs, R_res_lst,S_res_lst
    R_res_lst=[]
    S_res_lst=[]
    RDrugs=''
    SDrugs=''
    R_Drugs=[]
    S_Drugs=[]
    count=0
    if r:
        r.destroy()
        Login()


# In[163]:

def backpatdash():
    global count
    global RDrugs, SDrugs, R_Drugs, S_Drugs, R_res_lst,S_res_lst
    R_res_lst=[]
    S_res_lst=[]
    RDrugs=''
    SDrugs=''
    R_Drugs=[]
    S_Drugs=[]
    #print ('r',R_res_lst,S_res_lst)
    if r:
        count=0
        r.destroy()
        doc_dash()


# In[164]:

def on_click(event):
    event.widget.delete(0, END)
    return   


# In[165]:

def sel_tar_drug():
    global ac_var_cefp,ac_var_cotri,ac_var_amik,ent_var_norf,ent_var_gent,ent_var_pen
    global eco_var_mero, eco_var_cefo, kpn_var_cot, kpn_var_imp
    global pae_var_imp, pae_var_ceft, pae_var_aztreo, sau_var_cefo, sau_var_clinda 
    global count
    det0=patAGEEL.get()
    det1=patSEXEL.get()
    det4=patORGEL.get()
    if count==1:
        doc_submit.config(state='disabled')
        
    elif det4 == 'ac':
        orglbl = Label(r, text="Select your resistive drug: ", bg='white' , font = 30)
        orglbl.place(x=100, y=330)
        ac_var_cefp = IntVar()
        cbs1 = Checkbutton(r, text="Cefepime", font = 30, variable=ac_var_cefp, bg='white')
        cbs1.place(x=350, y=330)
        ac_var_cotri = IntVar()
        cbs2 = Checkbutton(r, text="Cotrimoxazole", font = 30, variable=ac_var_cotri, bg='white')
        cbs2.place(x=550, y=330)
        ac_var_amik=IntVar()
        cbs3 = Checkbutton(r, text="Amikacin", font = 30, variable=ac_var_amik, bg='white')
        cbs3.place(x=750, y=330)
        count=1
        proceed_sau = Button(r, text='Proceed', bg='white', font = 20,command=dec_ac)
        proceed_sau.place(x=950, y=330)
        
        
    elif det4 == 'ent':
        orglbl = Label(r, text="Select your resistive drug", bg='white' , font = 30)
        orglbl.place(x=100, y=330)
        ent_var_norf = IntVar()
        cbs1 = Checkbutton(r, text="Norfloxacin(U)", font = 30, variable=ent_var_norf, bg='white')
        cbs1.place(x=350, y=330)
        ent_var_gent = IntVar()
        cbs2 = Checkbutton(r, text="Gentamicin", font = 30, variable=ent_var_gent, bg='white')
        cbs2.place(x=550, y=330)
        ent_var_pen = IntVar()
        cbs3 = Checkbutton(r, text="Penicillin", font = 30, variable=ent_var_pen, bg='white')
        cbs3.place(x=750, y=330)
        count=1
        proceed_sau = Button(r, text='Proceed', bg='white', font = 20,command=dec_ent)
        proceed_sau.place(x=950, y=330)
        

    elif det4 == 'kpn':
        orglbl = Label(r, text="Select your resistive drug", bg='white' , font = 30)
        orglbl.place(x=100, y=330)
        kpn_var_cot = IntVar()
        cbs1 = Checkbutton(r, text="CoT", font = 30, variable=kpn_var_cot, bg='white')
        cbs1.place(x=450, y=330)
        kpn_var_imp = IntVar()
        cbs2 = Checkbutton(r, text="Imipenem", font = 30, variable=kpn_var_imp, bg='white')
        cbs2.place(x=650, y=330)
        count=1
        proceed_sau = Button(r, text='Proceed', bg='white', font = 20,command=dec_kpn)
        proceed_sau.place(x=950, y=330)
        

    elif det4 == 'eco':
        orglbl = Label(r, text="Select your resistive drug", bg='white' , font = 30)
        orglbl.place(x=100, y=330)
        eco_var_mero = IntVar()
        cbs1 = Checkbutton(r, text="Meropenem", font = 30, variable=eco_var_mero, bg='white')
        cbs1.place(x=450, y=330)
        eco_var_cefo = IntVar()
        cbs2 = Checkbutton(r, text="Cefotaxime", font = 30, variable=eco_var_cefo, bg='white')
        cbs2.place(x=650, y=330)
        count=1
        proceed_sau = Button(r, text='Proceed', bg='white', font = 20,command=dec_eco)
        proceed_sau.place(x=950, y=330)
        

    elif det4 == 'pae':
        orglbl = Label(r, text="Select your resistive drug", bg='white' , font = 30)
        orglbl.place(x=100, y=330)
        pae_var_imp = IntVar()
        cbs1 = Checkbutton(r, text="Imipenem", font = 30, variable=pae_var_imp, bg='white')
        cbs1.place(x=350, y=330)
        pae_var_ceft = IntVar()
        cbs2 = Checkbutton(r, text="Ceftazidime", font = 30, variable=pae_var_ceft, bg='white')
        cbs2.place(x=550, y=330)
        pae_var_aztreo = IntVar()
        cbs3 = Checkbutton(r, text="Aztreonam", font = 30, variable=pae_var_aztreo, bg='white')
        cbs3.place(x=750, y=330)
        count=1
        proceed_sau = Button(r, text='Proceed', bg='white', font = 20,command=dec_pae)
        proceed_sau.place(x=950, y=330)
        
    elif det4 == 'sau':
        orglbl = Label(r, text="Select your resistive drug", bg='white' , font = 30)
        orglbl.place(x=100, y=330)
        sau_var_clinda = IntVar()
        cbs1 = Checkbutton(r, text="Clindamicin", font = 30, variable=sau_var_clinda, bg='white')
        cbs1.place(x=450, y=330)
        sau_var_cefo = IntVar()
        cbs2 = Checkbutton(r, text="Cefoxtime", font = 30, variable=sau_var_cefo, bg='white')
        cbs2.place(x=650, y=330)
        count=1
        proceed_sau = Button(r, text='Proceed', bg='white', font = 20,command=dec_sau)
        proceed_sau.place(x=950, y=330)
        
        
    else:
        lbl = Label(r, text='Incorrect input', fg='red', font=20)
        lbl.place(x=600,y=280)

# In[166]:

def dec_ent():
    global res1,res2    
    det1=patSEXEL.get()
    det2=int(patAGEEL.get())
    det3=int(ent_var_norf.get())
    det4=int(ent_var_gent.get())
    det5=int(ent_var_pen.get())
    if det1=='M':
        det1 = 0
    elif det1=='F':
        det1 = 1
    else:
        det1 = 2
    
    ans1 = dt3.pred(det1,det2,det3,det5)
    ans2 = dt4.pred(det1,det2, det3, det4)
    if ans1[0]==1:
        res1='Tetra is Resitant'
        R_res_lst.append('Tetra')
    else:
        res1='Tetra is Sensitive'
        S_res_lst.append('Tetra')
    if ans2[0]==1:
        res2='Ciproflox is Resistant'
        R_res_lst.append('Ciproflox')        
    else:
        res2='Ciproflox is Sensitive'
        S_res_lst.append('Ciproflox')
    result()
    

# In[167]:

def dec_ac():
    global res1,res2    
    det1=patSEXEL.get()
    det2=int(patAGEEL.get())
    det3=int(ac_var_cefp.get())
    det4=int(ac_var_cotri.get())
    det5=int(ac_var_amik.get())
    if det1=='M':
        det1 = 0
    elif det1=='F':
        det1 = 1
    else:
        det1 = 2
    
    ans1 = dt1.pred(det1,det2,det3,det4,det5)
    ans2 = dt2.pred(det1,det2, det5, det4)
    if ans1[0]==1:
        res1='Aztreonam is Resitant'
        R_res_lst.append('Aztreonam')
    else:
        res1='Aztreonam is Sensitive'
        S_res_lst.append('Aztreonam')
    if ans2[0]==1:
        res2='Ceftazidime is Resistant'
        R_res_lst.append('Ceftazidime')
    else:
        res2='Ceftazidime is Sensitive'
        S_res_lst.append('Ceftazidime')
    result()


# In[167]:

def dec_pae():
    global res1,res2    
    det1=patSEXEL.get()
    det2=int(patAGEEL.get())
    det3=int(pae_var_imp.get())
    det4=int(pae_var_ceft.get())
    det5=int(pae_var_aztreo.get())
    if det1=='M':
        det1 = 0
    elif det1=='F':
        det1 = 1
    else:
        det1 = 2
    
    ans1 = dt9.pred(det1,det2,det4,det3)
    ans2 = dt10.pred(det1,det2, det4, det5)
    if ans1[0]==1:
        res1='Amikacin is Resitant'
        R_res_lst.append('Amikacin')
    else:
        res1='Amikacin is Sensitive'
        S_res_lst.append('Amikacin')
    if ans2[0]==1:
        res2='Cefepime is Resistant'
        R_res_lst.append('Cefepime')
    else:
        res2='Cefepime is Sensitive'
        S_res_lst.append('Cefepime')
    result()

# In[ ]:
def dec_kpn():
    global res1,res2    
    det1=patSEXEL.get()
    det2=int(patAGEEL.get())
    det3=int(kpn_var_cot.get())
    det4=int(kpn_var_imp.get())
    if det1=='M':
        det1 = 0
    elif det1=='F':
        det1 = 1
    else:
        det1 = 2
    
    ans1 = dt5.pred(det3,det4)
    ans2 = dt6.pred(det1,det2, det3, det4)
    if ans1[0]==1:
        res1='Gentamicin is Resitant'
        R_res_lst.append('Gentamicin')
    else:
        res1='Gentamicin is Sensitive'
        S_res_lst.append('Gentamicin')
    if ans2[0]==1:
        res2='Meropenem is Resistant'
        R_res_lst.append('Meropenem')
    else:
        res2='Meropenem is Sensitive'
        S_res_lst.append('Meropenem')
    result()

# In[ ]:

def dec_eco():
    global res1,res2    
    det1=patSEXEL.get()
    det2=int(patAGEEL.get())
    det3=int(eco_var_mero.get())
    det4=int(eco_var_cefo.get())
    if det1=='M':
        det1 = 0
    elif det1=='F':
        det1 = 1
    else:
        det1 = 2
    
    ans1 = dt8.pred(det1,det2,det3,det4)
    ans2 = dt7.pred(det3, det4)
    if ans1[0]==1:
        res1='Imipenem is Resitant'
        R_res_lst.append('Impipenem')
    else:
        res1='Imipenem is Sensitive'
        S_res_lst.append('Imipenem')
    if ans2[0]==1:
        res2='CoT is Resistant'
        R_res_lst.append('CoT')
    else:
        res2='CoT is Sensitive'
        S_res_lst.append('CoT')
    result()

# In[167]:

def dec_sau():
    global res1,res2    
    det1=patSEXEL.get()
    det2=int(patAGEEL.get())
    det3=int(sau_var_clinda.get())
    det4=int(sau_var_cefo.get())
    if det1=='M':
        det1 = 0
    elif det1=='F':
        det1 = 1
    else:
        det1 = 2
    
    ans1 = dt11.pred(det1,det2,det4,det3)
    ans2 = dt12.pred(det1,det2, det4, det3)
    if ans1[0]==1:
        res1='Erythromicin is Resitant'
        R_res_lst.append('Erythromicin')
    else:
        res1='Erythromicin is Sensitive'
        S_res_lst.append('Erythromicin')
    if ans2[0]==1:
        res2='Penicilin is Resistant'
        R_res_lst.append('Penicillin')
    else:
        res2='Penicilin is Sensitive'
        S_res_lst.append('Penicillin')
    result()
    

# In[167]:
def result():
    result_frame = Tk()
    w = 500
    h = 400

    ws = result_frame.winfo_screenwidth() 
    hs = result_frame.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2) + 100

    result_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))
    result_frame.config(bg='white')
    global R_Drugs, S_Drugs, df, f1,f2
    global R_res_lst,S_res_lst

    
    R_Drugs=list(set().union(R_Drugs,R_res_lst))
    S_Drugs=list(set().union(S_Drugs,S_res_lst))
    

    label1= Label(result_frame, text = res1, font = 50, bg='white')
    label1.place(x=170,y=50)
    label2= Label(result_frame, text = res2, font = 50, bg='white')
    label2.place(x=170,y=100)
    result_frame.title('Result')
    
    s=list(set(S_Drugs)&set(R_Drugs))
    for i in s:
    	S_Drugs.remove(i)
    RDrugs = ','.join(map(str, R_Drugs))
    SDrugs = ','.join(map(str, S_Drugs))
    if f1==1:
        df.loc[index,'R_Drugs']=RDrugs
        df.loc[index,'S_Drugs']=SDrugs
        df.to_csv('pat_history.csv')
    elif f2==1:
         with open('pat_history.csv','a') as f1:
            #df_fr_rd = pd.read_csv(pat_db)
            data = [[NewPatId,RDrugs,SDrugs]]
            df2 = pd.DataFrame(data)
            df2.to_csv(f1, header=False)


    label3= Label(result_frame, text = 'Resistant Drugs: \n'+RDrugs, font=20, fg='red', bg='white', wraplength=400, relief='groove')
    label3.place(x=50,y=200)
    label4= Label(result_frame, text = 'Sensitive Drugs: '+SDrugs, font=20, bg='white', wraplength=400, relief='groove')
    label4.place(x=50,y=300)
    result_frame.mainloop()


# In[ ]:

def end():
    r.destroy()
    login()
 
def DelUser():
    os.remove(creds)
    rootA.destroy()
    Signup()


if os.path.isfile(creds):
    Login()
    
else:
    Signup()


# end
