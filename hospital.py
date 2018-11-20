
#using exact mam arguments
import logging ##for logging exceptions
logging.basicConfig(filename='mylogfile')
import  pymysql
db=pymysql.connect(host="localhost",user="root",passwd="Vaibhav1*",db="newdb");##database exceptions

cursor =db.cursor()


category=["orthopedic","generalphysician"];
loc=["local","opd"];
i=[]; ##list for capturing sql result
i1=[];
countdx=0;
couuntdy=0;#for doctor password checking

#functons for patient class defined below
def checklogin(k,p):
    countdp = 0;  # for outer for loop
    countdnp = 0  # for inner for loop
    countdq=0;#for paswword total
    countdw=0;#for password count in loop
    count=0
    n = [];

    cursor.execute("SELECT username FROM patients");
    myresult = cursor.fetchall()
    n = myresult;
    # counting no of doctor result fetched
    for y in n:
        countdp = countdp + 1;

    for w in n:

        if (k == ''.join(w)):
            print("patient  logged in");
            print("now checking password.....")
            cursor.execute("SELECT password FROM patients");
            myresult = cursor.fetchall()
            i = myresult;
            # counting no of doctor result fetched
            for b in i:
                countdq = countdq + 1;#countdq is used for counting total no of password available

            for c in i:

                 if (p == ''.join(c)):
                    print("password correct");
                    break;
                 else:
                    countdw=countdw+1;
                    if (countdq == countdw):
                        print("password incorrect");
                        print("login again");


            break;
        else:
            countdnp = countdnp + 1;
            if (countdnp == countdp):
                print("patient  not signed up");
                count = count + 1;
                o = str(count);
                a = input("enter username");
                r = generateid();
                print(r);
                b = r + o;
                c = input("address");
                d = location();
                e = assigndoctor(r);
                f = assigntime(e);  # sending assigned doctor as argument to fetch doctor day and time.
                g = input("enter day you want to visit doctor is available 7 days")
                h= input("enter password")
                p = Patients(a, b, c, d, e, f, g,h);
                sql = "INSERT INTO patients (username,id,address,location,assignedDoctor,TimeVisit,dayvisit,password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)";
                val = (a, b, c, d, e, f, g,h);
                cursor.execute(sql, val);
                db.commit();












def generateid():
    print("select category");
    print(category);
    y = input("enter choice no");
    return (category[y]);
def location():
    print("select location");
    print(loc);
    m = input("enter choice no");
    return (loc[m]);
def assigndoctor(t):

    print("allocating available doctors based on department");#user category is doctors department
    ##sql command for extracting doctors based on department
    cursor.execute("SELECT name FROM doctors WHERE department LIKE '%s'"%(t))
    myresult = cursor.fetchall()
    for q in myresult:
        print(q);
    g=  input("select doctors ");#choose doctor name
    j=  input("do you want to see doctor details ");
    if(j==1):

        cursor.execute("SELECT * FROM doctors WHERE name LIKE '%s'"%(g));
        myresult = cursor.fetchall()
        for w in myresult:
            print(w);
    return g;#returning selected doctor name so that we can extract opd time in vaiable u below
def assigntime(u):
    print("asssigning day and time")
    cursor.execute("SELECT opdTime FROM doctors WHERE name LIKE '%s'"%(u));
    myresult = cursor.fetchall()
    for o in myresult:
        print(o);

    return o;




##function for doctor class defined below

def showpatientdetails(z):
    print("showing patients detail");
    cursor.execute("SELECT * FROM patients WHERE assignedDoctor LIKE '%s'" % (z));
    myresult = cursor.fetchall()
    for o in myresult:
        print(o);


def sortpatients(i):
    print("sorting patients ")
    cursor.execute("SELECT username,id FROM patients WHERE assignedDoctor LIKE '%s' ORDER BY id" % (i))
    myresult = cursor.fetchall()
    for o in myresult:
        print(o);





class Patients:


   def __init__(self,a,b,c,d,e,f,g,h):

       self.a=a;
       self.b=b;
       self.c=c;
       self.d=d;
       self.e=e;
       self.f=f;
       self.g=g;
       self.h=h;



k=input("enter patient name");
p=input("enter patient password")
checklogin(k,p);#checking for signup



class Doctors:

     def __init__(self,n,pd):
        self.n=n;
        self.pd=pd;
        countd=0; #for outer for loop
        countdn=0  #for inner for loop
        countdx=0;
        countdy=0;
        #k= "("+"'"+n+"'"+","+")";
        x=[];
        i1=[];
        cursor.execute("SELECT name FROM doctors");
        myresult = cursor.fetchall()
        x=myresult;
       #counting no of doctor result fetched
        for y in x:
                   countd=countd+1;


        for w in x:

                if(n == ''.join(w)):
                   print("doctor logged in");
                   print("now checking password.....")
                   cursor.execute("SELECT password FROM doctors");
                   myresult = cursor.fetchall()
                   i1 = myresult;
                   # counting no of password result fetched
                   for d in i1:
                       countdx = countdx + 1;

                   for e in i1:
                       # displaying and sorting patients
                       if (pd == ''.join(e)):
                           print("doctor password correct");
                           f = input("do you want to see patient details")
                           if (f == 1):
                               showpatientdetails(p);
                           g = input("do you want to sort patients")
                           if (g == 1):
                               sortpatients(p);




                           break;
                       else:
                           countdy = countdy + 1;
                           if (countdy == countdx): #if any of the password doesnt match
                               print("doctor password incorrect");
                               print("login again");



                   break;
                else:
                    countdn=countdn+1;
                    if(countdn==countd):
                        print("doctor not signed up");



print("starting Doctor class")
print("starting authorisation")
p=input("enter doctor name");
z=input("enter doctor password")
d1=Doctors(p,z);

class Hod:
    def __init__(self,f):
        self.f=f;#f is name of hod
        print(f);

    def checkcritical(self):
        x=input("enter patient name");
        countp=0;
        countpn=0;
        val4=0;
        z=[];
        cursor.execute("SELECT username FROM patients")
        myresult = cursor.fetchall()
        z=myresult;
        for r in z:
            countp=countp+1;



        for w in z:
            if(x!=''.join(w)):
                countpn=countpn+1;
                if(countpn==countp):
                    print("exception raised");#checking exception
                    raise Exception("cannot check criticality ");






        y=input("enter patient department");
        z=input("given patient is critical or not");#enter integer 1 or 0
        if(z==1):

            cursor.execute("SELECT name FROM doctors WHERE department LIKE '%s' AND type LIKE 'seniorspecialist'" % (y))
            myresult = cursor.fetchall()
            for q in myresult:
                val4=''.join(q);
                break;

            print("new doctor assigned is")
            print(val4);
            cursor.execute("""UPDATE patients SET reffered =%s WHERE username =%s""",(val4,x));
            db.commit();
            print("tableupdated");

        else  :
           print("entered patient is not critical ")


print("starting HOD class");
print("starting authorisation")
d=[]#list for storing hod names;
counth=0;
counthn=0;
q=input("enter your name");
cursor.execute("SELECT name FROM doctors WHERE type LIKE 'seniorspecialist'")
myresult = cursor.fetchall()
d=myresult;

for f in d:
        counth=counth+1;



#checking wheter entered doctor is  a senior specialist or not:
for e in d:
    if(q == ''.join(e)):
        print("hod is seniorspecialist")
        q = "responbility to check patient criticallity"
        h = Hod(q)
        print("check patient criticality")
        try:
            h.checkcritical();
        except Exception as e:
            logging.exception(str(e))
            print("patient not present in database", e.args);



    else:
        counthn = counthn + 1;
        if(counthn==counth):
             print("entered doctor is not seniorspecialist")



class Admindepartment:
    #generating new id and passsword
    def __init__(self, g, ):
        self.g = g;
        print("generating login id and password");
        print("your loginid created is");
        print(g + "123");
        print("your password created is");
        print("12345");

    def showdetails(self):

        v=input("do you want to see patient detail")
        if(v==1):
            print("showing patients detail");
            cursor.execute("SELECT * FROM patients")
            myresult = cursor.fetchall()
            for o in myresult:
                print(o);

        b = input("do you want to see doctor detail")
        if (b == 1):

            print("showing doctor detail");
            cursor.execute("SELECT * FROM doctors")
            myresult = cursor.fetchall()
            for o in myresult:
                print(o);

    def adddoctors(self):
        print("calling specific doctor")
        g = input("enter doctor name")
        p = input("enter address");
        q = input("enter contact number ");
        r = input("enter specilisation");
        s = input("enter type");
        t = input("enter opdtime");
        u = input("department");
        v=  input("passsword")

        sql1 = "INSERT INTO doctors (name,address,contactNumber,specilisation,type,opdTime,department,password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)";
        val1 = (g, p, q, r, s, t, u,v);
        cursor.execute(sql1, val1);
        db.commit();

print("starting admin class")
print("creating new admin")
k = input("enter admin name")
a1 = Admindepartment(k);
a1.showdetails();
p=input("is there any  new doctor available ")
if(p==1):
    a1.adddoctors();
else:
    exit();
