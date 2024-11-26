from tkinter import*
import sqlite3

root= Tk()
root.title("PERSONAL INFO")
root.geometry('2000x2000')

root.configure(bg='#e3e7e1')
conn=sqlite3.connect('Personal_info.db')

c=conn.cursor()



def submit():
    conn=sqlite3.connect('C:/Users/STUDENTS.DESKTOP-G4BV2BC/Desktop/vincepersonalinfo.db')

    c=conn.cursor()

    c.execute("INSERT INTO Student_infos  VALUES(:f_name,:l_name,:age,:address,:email,:number,:sex,:birthday,:mothers_name,:fathers_name,:emergency_contact)",
            {
                  'f_name':f_name.get(),
                  'l_name':l_name.get(),
                  'age':age.get(),
                  'address':address.get(),
                  'email':email.get(),
                  'number':number.get(),
                  'sex':sex.get(),
                  'birthday':birthday.get(),
                  'mothers_name':mothers_name.get(),
                  'fathers_name':fathers_name.get(),
                  'emergency_contact':emergency_contact.get()

              })

    conn.commit()
    conn.close()
    
    f_name.delete(0,END)
    l_name.delete(0,END)
    age.delete(0,END)
    address.delete(0,END)
    email.delete(0,END)
    number.delete(0,END)
    sex.delete(0,END)
    birthday.delete(0,END)
    mothers_name.delete(0,END)
    fathers_name.delete(0,END)
    emergency_contact.delete(0,END)

def query():
    conn=sqlite3.connect('C:/Users/STUDENTS.DESKTOP-G4BV2BC/Desktop/vincepersonalinfo.db')

    c=conn.cursor()

    c.execute("SELECT *,oid FROM Student_infos")
    records=c.fetchall()

    print_records=''
    for record in records:
        print_records+=str(record[0])+""+str(record[1])+""+str(record[2])+"" +str(record[3])+""+ str(record[4])+""+ str(record[5])+""+ str(record[6])+""+ str(record[7])+""+ str(record[8])+""+ str(record[9])+""+ str(record[10])+""+"\t"+str(record[11])+"\n"                   
        query_label=Label(root,text=print_records)
        query_label.grid(row=19,column=0,columnspan=2)
    
    conn.commit()
    conn.close()

def delete():
    conn=sqlite3.connect('C:/Users/STUDENTS.DESKTOP-G4BV2BC/Desktop/vincepersonalinfo.db')

    c=conn.cursor()
    c.execute("DELETE from Student_infos WHERE oid="+delete_box.get())

    delete_box.delete(0,END)
    conn.commit()
    conn.close()

def update():
    conn=sqlite3.connect('C:/Users/STUDENTS.DESKTOP-G4BV2BC/Desktop/vincepersonalinfo.db')

    c=conn.cursor()

    record_id=delete_box.get()
    
    c.execute(""" UPDATE Student_infos SET
        f_name=:first,
        l_name=:last,
        age=:age,
        address=:address,
        email=:email,
        number=:number,
        sex=:sex,
        birthday=:birthday,
        mothers_name=:mothers_name,
        fathers_name=:fathers_name,
        emergency_contact=:emergency_contact
        

        WHERE oid=:oid""",
        {
        'first':f_name_editor.get(),
        'last':l_name_editor.get(),
        'age':age_editor.get(),
        'address':address_editor.get(),
        'email':email_editor.get(),
        'number':number_editor.get(),
        'sex':sex_editor.get(),
        'birthday':birthday_editor.get(),
        'mothers_name':mothers_name_editor.get(),
        'fathers_name':fathers_name_editor.get(),
        'emergency_contact':emergency_contact_editor.get(),
        'oid':record_id
        
        })
    
    conn.commit()
    conn.close()
    
def edit():
    editor=Tk()
    editor.title('Update Record from database')
    editor.geometry("2000x2000")
    
    conn=sqlite3.connect('C:/Users/STUDENTS.DESKTOP-G4BV2BC/Desktop/vincepersonalinfo.db')

    c=conn.cursor()

    record_id=delete_box.get()
    c.execute("SELECT* FROM Student_infos WHERE oid="+record_id)
    records=c.fetchall()

    global f_name_editor
    global l_name_editor
    global age_editor
    global address_editor
    global email_editor
    global number_editor
    global sex_editor
    global birthday_editor
    global mothers_name_editor
    global fathers_name_editor
    global emergency_contact_editor
    

    f_name_editor=Entry(editor,width=30, bg='#f0f8ff')
    f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))
    l_name_editor=Entry(editor,width=30, bg='#f0f8ff')
    l_name_editor.grid(row=1,column=1,padx=20)
    age_editor=Entry(editor,width=30, bg='#f0f8ff')
    age_editor.grid(row=2,column=1,padx=20)
    address_editor=Entry(editor,width=30, bg='#f0f8ff')
    address_editor.grid(row=3,column=1,padx=20)
    email_editor=Entry(editor,width=30, bg='#f0f8ff')
    email_editor.grid(row=4,column=1,padx=20)
    number_editor=Entry(editor,width=30, bg='#f0f8ff')
    number_editor.grid(row=5,column=1,padx=20)
    sex_editor=Entry(editor,width=30, bg='#f0f8ff')
    sex_editor.grid(row=6,column=1,padx=20)
    birthday_editor=Entry(editor,width=30, bg='#f0f8ff')
    birthday_editor.grid(row=7,column=1,padx=20)
    mothers_name_editor=Entry(editor,width=30, bg='#f0f8ff')
    mothers_name_editor.grid(row=8,column=1,padx=20)
    fathers_name_editor=Entry(editor,width=30, bg='#f0f8ff')
    fathers_name_editor.grid(row=9,column=1,padx=20)
    emergency_contact_editor=Entry(editor,width=30, bg='#f0f8ff')
    emergency_contact_editor.grid(row=10,column=1,padx=20)
    
    f_name_label=Label(editor,text="First Name")
    f_name_label.grid(row=0,column=0,pady=(10,0))
    l_name_label=Label(editor,text="Last Name")
    l_name_label.grid(row=1,column=0)
    age_label=Label(editor,text="Age")
    age_label.grid(row=2,column=0)
    address_label=Label(editor,text="Address")
    address_label.grid(row=3,column=0)
    email_label=Label(editor,text="Email")
    email_label.grid(row=4,column=0)
    number_label=Label(editor,text="Number")
    number_label.grid(row=5,column=0)
    sex_label=Label(editor,text="Sex")
    sex_label.grid(row=6,column=0)
    birthday_label=Label(editor,text="Birthday")
    birthday_label.grid(row=7,column=0)
    mothers_name_label=Label(editor,text="Mothers Name")
    mothers_name_label.grid(row=8,column=0)
    fathers_name_label=Label(editor,text="Fathers Name")
    fathers_name_label.grid(row=9,column=0)
    emergency_contact_label=Label(editor,text="Emergency Contact")
    emergency_contact_label.grid(row=10,column=0)






    
    for record in records:  
        f_name_editor.insert(0, record[0] if record[0] else "")
        l_name_editor.insert(0, record[1] if record[1] else "")
        age_editor.insert(0, record[2] if record[2] else "")
        address_editor.insert(0, record[3] if record[3] else "")
        email_editor.insert(0, record[4] if record[4] else "")
        number_editor.insert(0, record[5] if record[5] else "")
        sex_editor.insert(0, record[6] if record[6] else "")
        birthday_editor.insert(0, record[7] if record[7] else "")
        mothers_name_editor.insert(0, record[8] if record[8] else "")
        fathers_name_editor.insert(0, record[9] if record[9] else "")
        emergency_contact_editor.insert(0, record[10] if record[10] else "")

   
    save_btn=Button(editor,text="Save Record",command=update)
    save_btn.grid(row=15, column=0,columnspan=2,pady=20,padx=10,ipadx=140) 

   

                  
    conn.commit()
    conn.close()       
                
    
'''

c.execute("""CREATE TABLE "Student_infos" (
	"f_name"	TEXT,
	"l_name"	TEXT,
	"age"	INTEGER,
	"address"	TEXT,
	"email"	TEXT,
	"number"	INTEGER,
	"sex"	TEXT,
	"birthday"	TEXT,
	"mothers_name"	TEXT,
	"fathers_name"	TEXT,
	"emergency_contact"	INTEGER
)""";

'''

f_name=Entry(root,width=30)
f_name.grid(row=0, column=1,padx=20)
l_name=Entry(root,width=30)
l_name.grid(row=1, column=1,padx=20)
age=Entry(root, width=30)
age.grid(row=2, column=1,padx=20)
address=Entry(root, width=30)
address.grid(row=3, column=1,padx=20)
email=Entry(root, width=30)
email.grid(row=4, column=1,padx=20)
number=Entry(root, width=30)
number.grid(row=5, column=1,padx=20)
sex=Entry(root, width=30)
sex.grid(row=6, column=1,padx=20)
birthday=Entry(root, width=30)
birthday.grid(row=7, column=1,padx=20)
mothers_name=Entry(root, width=30)
mothers_name.grid(row=8, column=1,padx=20)
fathers_name=Entry(root, width=30)
fathers_name.grid(row=9, column=1,padx=20)
emergency_contact=Entry(root, width=30)
emergency_contact.grid(row=10, column=1,padx=20)


delete_box=Entry(root,width=30)
delete_box.grid(row=14,column=1, padx=30)

f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1, column=0)
age_label=Label(root,text="Age")
age_label.grid(row=2, column=0)
address_label=Label(root,text="Address")
address_label.grid(row=3, column=0)
email_label=Label(root,text="Email")
email_label.grid(row=4, column=0)
number_label=Label(root,text="Number")
number_label.grid(row=5, column=0)
sex_label=Label(root,text="Sex")
sex_label.grid(row=6, column=0)
birthday_label=Label(root,text="Birthday")
birthday_label.grid(row=7, column=0)
mothers_name_label=Label(root,text="Mothers Name")
mothers_name_label.grid(row=8, column=0)
fathers_name_label=Label(root,text="Fathers Name")
fathers_name_label.grid(row=9, column=0)
emergency_contact_label=Label(root,text="Emergency Contact")
emergency_contact_label.grid(row=10, column=0)



delete_box_label=Label(root,text="Select ID No.")
delete_box_label.grid(row=14,column=0)

submit_btn=Button(root,text="Add Record",command=submit, bg='#f0f8ff')
submit_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=120)

query_btn=Button(root,text="Show Records",command=query, bg='#f0f8ff')
query_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=139)

query_btn=Button(root, text="Delete Record", command=delete, bg='#f0f8ff')
query_btn.grid(row=17, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

update_btn=Button(root,text="Edit Record",command=edit, bg='#f0f8ff')
update_btn.grid(row=13,column=0,columnspan=2,pady=10,padx=10,ipadx=141)






root.mainloop()
