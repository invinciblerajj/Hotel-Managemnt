import random as rd
import datetime as dt
#some key terms
name=[]
add=[]
phn=[]
chkin=[]
chkot=[]
roomno=[]
cstid=[20]
rc=[] #Room Charges
oc=[] #other carges
room=[]
tprice=[]
p=[]
#Main Function
file=open("Hotel Management.txt","a+")
def main():
    
    print("\t\t\t\t\t WELCOME TO HOTEL PANCHAMRITAM:)\n")
    print("\t\t\t1.Rooms Info\n")
    print("\t\t\t2.Booking\n")
    print("\t\t\t3.Room Service(Menu Card)\n")
    print("\t\t\t4.Payment\n")
    print("\t\t\t5.Record\n")
    print("\t\t\t0.Exit\n")

    ch=int(input("What do you want to do:)?\n->"))
    if ch==1:
        print("Follwing arr the description of the Rooms :)")
        Room_Info()
    elif ch==2:
         print("Please fill below details :)")
         Booking()
    elif ch==3:
        print("Select your favourite food you want to have :)\n->")
        Menu_card()
    elif ch==4:
        print(" ")
        Pay()
    elif ch==5:
        print(" ")
        Record()
    elif ch==0:
        exit()
def Room_Info():
    print("	    ------ HOTEL ROOMS INFO ------") 
    print("") 
    print("STANDARD NON-AC") 
    print("---------------------------------------------------------------") 
    print("Room amenities include:\n-1 Double Bed\n-Television\n-Telephone") 
    print("-Double-Door Cupboard \n-1 Coffee table with 2 sofa\n-Balcony and an attached washroom with hot/cold water.\n") 
    print("STANDARD AC") 
    print("---------------------------------------------------------------") 
    print("Room amenities include: \n-1 Double Bed\n-Television\n-Telephone") 
    print("-Double-Door Cupboard\n-1 Coffee table with 2 sofa") 
    print("-Balcony and an attached washroom with hot/cold water + Window/Split AC.\n") 
    print("3-Bed NON-AC") 
    print("---------------------------------------------------------------") 
    print("Room amenities include: \n-1 Double Bed + 1 Single Bed\n-Television") 
    print("-Telephone\n-a Triple-Door Cupboard\n-1 Coffee table with 3 sofa") 
    print("-1 Side table\n-Balcony with an Accent table with 2 Chair and an attached washroom with hot/cold water.\n")  
    print("3-Bed AC") 
    print("---------------------------------------------------------------") 
    print("Room amenities include: \n-1 Double Bed + 1 Single Bed\n-Television") 
    print("-Telephone\n-a Triple-Door Cupboard\n-1 Coffee table with 3 sofa ") 
    print("-1 Side table\n-Balcony with an Accent table with 2 Chair and an attached washroom with hot/cold water + Window/Split AC.\n\n") 
    print()
    n=int(input("Press 0 to go back:"))
    if n==0:
        main()
    else:
        exit()
def Menu_card():
    c=int(input("Enter Customer ID:"))
    a=0
    r=0
    l=len(cstid)
    for i in range(0,l):
        if cstid[i]==c:
            a=1
            print("-------------------------------------------------------------------------") 
            print("				    Hotel AnCasa") 
            print("-------------------------------------------------------------------------") 
            print("				    Menu Card") 
            print("-------------------------------------------------------------------------") 
            print("\n BEVARAGES				 26 Dal Fry................ 140.00") 
            print("----------------------------------	 27 Dal Makhani............ 150.00") 
            print(" 1 Regular Tea............. 20.00	 28 Dal Tadka.............. 150.00") 
            print(" 2 Masala Tea.............. 25.00") 
            print(" 3 Coffee.................. 25.00	 ROTI") 
            print(" 4 Cold Drink.............. 25.00	 ----------------------------------") 
            print(" 5 Bread Butter............ 30.00	 29 Plain Roti.............. 15.00") 
            print(" 6 Bread Jam............... 30.00	 30 Butter Roti............. 15.00") 
            print(" 7 Veg. Sandwich........... 50.00	 31 Tandoori Roti........... 20.00") 
            print(" 8 Veg. Toast Sandwich..... 50.00	 32 Butter Naan............. 20.00") 
            print(" 9 Cheese Toast Sandwich... 70.00") 
            print(" 10 Grilled Sandwich........ 70.00	 RICE") 
            print("					 ----------------------------------") 
            print(" SOUPS				 33 Plain Rice.............. 90.00") 
            print("----------------------------------	 34 Jeera Rice.............. 90.00") 
            print(" 11 Tomato Soup............ 110.00	 35 Veg Pulao.............. 110.00") 
            print(" 12 Hot & Sour............. 110.00	 36 Peas Pulao............. 110.00") 
            print(" 13 Veg. Noodle Soup....... 110.00") 
            print(" 14 Sweet Corn............. 110.00	 SOUTH INDIAN") 
            print(" 15 Veg. Munchow........... 110.00	 ----------------------------------") 
            print("					 37 Plain Dosa............. 100.00") 
            print(" MAIN COURSE				 38 Onion Dosa............. 110.00") 
            print("----------------------------------	 39 Masala Dosa............ 130.00") 
            print(" 16 Shahi Paneer........... 110.00	 40 Paneer Dosa............ 130.00") 
            print(" 17 Kadai Paneer........... 110.00	 41 Rice Idli.............. 130.00") 
            print(" 18 Handi Paneer........... 120.00	 42 Sambhar Vada........... 140.00") 
            print(" 19 Palak Paneer........... 120.00") 
            print(" 20 Chilli Paneer.......... 140.00	 ICE CREAM") 
            print(" 21 Matar Mushroom......... 140.00	 ----------------------------------") 
            print(" 22 Mix Veg................ 140.00	 43 Vanilla................. 60.00") 
            print(" 23 Jeera Aloo............. 140.00	 44 Strawberry.............. 60.00") 
            print(" 24 Malai Kofta............ 140.00	 45 Pineapple............... 60.00") 
            print(" 25 Aloo Matar............. 140.00	 46 Butter Scotch........... 60.00") 
            print("Press 0 -to end ")
            ch=1
            while ch!=0:
                print(" ")
                ch=int(input("Choose anything you want to have or press 0 to end\n->"))
                # if-elif-conditions to assign item
                # prices listed in menu card
                if ch==1 or ch==31 or ch==32:
                    rs=20
                    r+=rs
                elif ch<=4 and ch>=2:
                    rs=25
                    r+=rs
                elif ch<=6 and ch>=5:
                    rs=30
                    r=r+rs 
                elif ch<=8 and ch>=7:
                    rs=50
                    r=r+rs 
                elif ch<=10 and ch>=9: 
                    rs=70
                    r=r+rs 
                elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38: 
                    rs=110
                    r=r+rs 
                elif ch<=19 and ch>=18: 
                    rs=120
                    r=r+rs 
                elif (ch<=26 and ch>=20) or ch==42: 
                    rs=140
                    r=r+rs 
                elif ch<=28 and ch>=27: 
                    rs=150
                    r=r+rs 
                elif ch<=30 and ch>=29: 
                    rs=15
                    r=r+rs 
                elif ch==33 or ch==34: 
                    rs=90
                    r=r+rs 
                elif ch==37: 
                    rs=100
                    r=r+rs 
                elif ch<=41 and ch>=39: 
                    rs=130
                    r=r+rs 
                elif ch<=46 and ch>=43: 
                    rs=60
                    r=r+rs 
                elif ch==0: 
                    pass
                else: 
                    print("Wrong Choice..!!") 
            print("Total Bill: ",r)
            # updates restaurant charges and then 
            # appends in 'rc' list
            L1=len(rc)
            for pos in range(0,L1):
                b=rc[pos]
                print("Room charge",b)
                tp=b+r
                tp1=str(tp)
                print("Total Price",tp)
                tprice.append(tp)
                file.writelines(["Total-Charges:",tp1,'\n'])
        else:
            pass
    if a==0:
        print("Invalid Customer ID :(")
    n1=int(input("Press 0 to go back\n->"))
    if n1==0:
        main()
    else:
        exit()          
def Booking():
    nm=input("Name:")
    if nm==" " or nm==".":
        print("Name cannot be empty")
        Booking()
    ph=input("Phone Number:")
    if ph=='' or ph=='.':
        print("Phone number cannot be empty")
        Booking()
    ad=input("Address:")
    if ad=='' or ad=='.':
        print("Address cannot be empty")
        Booking()
    else:
        print("")
    name.append(nm)
    add.append(ad)
    phn.append(ph)
    file.writelines(["Customer Details",'\n'])
    file.writelines(["------------------",'\n'])
    file.writelines(['Name:',nm,'\n'])
    file.writelines(['Phone No.:',ph,'\n'])
    file.writelines(['Address:',ad,'\n'])
    a=str(dt.datetime.now())
    CI=input("Check-In(YYYY-MM-DD):")
    if CI>a:
        chkin.append(CI)
        file.writelines(['Check-IN Date(YYYY-MM-DD):',CI,'\n'])
        CO=input("Check-Out(YYYY-MM-DD):")
        chkot.append(CO)
        file.writelines(['Check-OUT Date(YYYY-MM-DD):',CO,'\n'])
        print(" ")
        if CO>CI:
            print("Please select the type of room:\n")
            print("\t\t\t-----ROOM TYPES-----\n")
            print("\t\t1.STANDARD AC\t\tcost-4000")
            print("\t\t2.STANDARD NON-AC\tcost-3500")
            print("\t\t3.NON-AC-3-BED\t\tcost-4500")
            print("\t\t4.AC-3-BED\t\tcost-5000")
            c=int(input("Select Room type:"))
            print(" ")
            if c==1:
                room.append("Standard AC")
                file.writelines(['Room-Type:',"Standard AC",'\n',"Price-4000"])
                print("Room Booked-Standard AC")
                print("Price-4000")
                rc.append(4000)
                
                
            elif c==2:
                room.append("Standard NON-AC")
                file.writelines(['Room-Type:',"Standard NON-AC",'\n',"Price-3500"])
                print("Room Booked -Standard NON-AC")
                print("Price-3500")
                rc.append(3500)
            elif c==3:
                room.append("NON AC 3-Bed")
                file.writelines(['Room-Type:',"NON AC 3-Bed",'\n',"Price-4500"])
                print("Room Booked-NON AC 3-Bed")
                print("Price-4500")
                rc.append(4500)
            elif c==4:
                room.append("AC 3-Bed")
                file.writelines(['Room-Type:',"AC 3-Bed",'\n',"Price-5000"])
                print("Room Booked AC 3-Bed")
                print("Price-5000")
                rc.append(5000)
            else:
                print("Invalid choice")
                
            #giving room nond customer id
            print(" ")
            rn=str(rd.randrange(100,501))
            cid=int(rd.randrange(99))
            cid1=str(cid)
            roomno.append(rn)
            cstid.append(cid)
            file.writelines(['Room No:',rn,'\n'])
            file.writelines(['Customer ID:',cid1,'\n'])
            file.writelines(["  ",'\n'])
            print("Successfully Done.")
            print("Your Room No. is:",rn)
            print("Customer ID:",cid)
            print(cid1)
            print(rc)
            
        else:
            print("Check-Out date must be after Check In date.")
            print(" ")
            Booking()
    else:
        print("Invalid Check In date")
        print(" ")
        Booking()
    ch1=int(input("Press 0 to go back:\n->"))
    if ch1==0:
        main()
    else:
        exit()
def Pay():
    print("Coming soon")
    c=int(input("Enter Customer ID:"))
    l=len(cstid)
    for i in range(0,l):
        if cstid[i]==c:
            print("\t\t\tSelect the mode of Payment:")
            print("")
            print("\t\t1.Credit/Debit Card")
            print("\t\t2.Cash")
            x=int(input("\n->"))
            print()

def Record():
    with open("Hotel Management.txt","r") as f:
        while True:
            line=f.readline()
            print(line)
            if not line:
                break

file.close()   
main()
    
    
       
        

