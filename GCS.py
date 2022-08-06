import os
import time
import pyotp
import qrcode
from datetime import datetime

#define clear function
def clear():
    os.system("cls")

def login():
    # Initialization
    admin_details = []
    count = 1

    file = open("login.txt", "r")
    logfile = open("log-management.txt", 'a')  
    lines=[]
    with open("login.txt",'r') as f:
        lines = f.readlines()

    while(count < 3):
        # User 
        username = input("Username: ").strip().title()
        password = input("Password: ")
        print(count)
        # Check admin login credentials
        # Convert data in admin login credentials file to list
        for line in lines:
            admin_details = eval(line)
            # Assign username and password in list to variable
            a = admin_details[0]
            b = admin_details[1]
            # Execute code if login credentials inputted are correct
            if(a == username and b == password):
                now = datetime.now
                time = now.strftime('%H:%M:%S')
                logs = []
                logs.append(username)
                logs.append(time)
                #append to list logs


                logfile.write(str(logs))
                logfile.write("\n")

                #close file
                file.close()
                logfile.close()
                menu()
            else:
                print("Try again!")
                count = count + 1
        
 

    if(count == 3):
        print("Error: You have been locked out for safety purposes.")
        print("Please contact administrator")
        time.sleep(10)


    # Close file
    

def Factor_Auth():
    #2FA page (Factor_Auth)
    #code for Factor Authentication
    x=pyotp.random_base32()
    print(x)
    t=pyotp.TOTP(x)
    print(t.now())

    auth_str=t.provisioning_uri(name="user" ,issuer_name='Authenticator')
    print(auth_str)

    img=qrcode.make(auth_str)
    img.show()

    code = input("Enter 6 Digit Pin: ")
    if(code == t.now()):
        menu()
    else:
        print("Error")

def login_register():
    #open login file for appending
    loginFile = open('login.txt','a')
    
    #get login input
    a = input("Enter Username: ").strip().title()
    b = input("Enter Password: ")
    c = "Approve"
    print("Registration Successful!")
    #print("Your unique ID is: ", newID) ----to be tested
    
    
    #allow login time to read their ID
    continueToNext = input("Type anything to continue....")

    #append login information into a list
    loginList = []
    loginList.append(a)
    loginList.append(b)
    loginList.append(c)

    loginFile.write(str(loginList))
    loginFile.write("\n")

    #close login file
    loginFile.close()
    menu()



def menu(): 
    clear()
    print("\n")
    print("Welcome to die")
    print("======main menu======")
    print("Choose your destiny")
    print("1. Admin")
    print("2. Club Advisor/Society Committee Member")
    print("3. Student")
    print("4. Exit")
    print("=====================")
    
    #User input
    choice = input(("Please Select the option you would like to choose: ")).strip()
    
    #redirect
    if choice == '1':
        Admin()
    elif choice == '2':
        Club_Advisor()
    elif choice == '3':
        Student()
    elif choice == '4':
        exit()
    #error
    else:
        print("Invalid Input")
        menu()
        
def Admin(): #edit IMPORTANT
    
    #admin functions
    '''1. Classroom booking
       2. Check status
       3. Update club details
       4. Monthly activity report
       5. Submit club announcements '''

    print("<------------------------------->")
    print("Announcement:")
    #Display()
    print("<------------------------------->")

    print("1. Create Club")
    print("2. Classroom Booking Status")
    print("3. Make an announcement")
    print("4. Report on Classroom Bookings")
    print("5. Register for Login")
    print("6. Reply to student enquiries")
    print("7. Exit")
    
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        RegisterCb()
    elif choice == '2':
        Classroom_Booking()
    elif choice == '3':
        Announcement_review()
    elif choice == '4':
        View_Classroom_Booking()
        menu()
    elif choice == '5':
        login_register()
    elif choice == '6':
        Admin_Enquire()
    elif choice == '7':
        menu()
    #error
    else:
        print("Invalid Input")
        menu()
        
def Club_Advisor():
    
    #admin functions
    
    print("<------------------------------->")
    print("Announcement:")
    #Display()
    print("<------------------------------->")

    print("1. Classroom booking")
    print("2. Check status")
    print("3. Update club details")
    print("4. Monthly activity report")
    print("5. Submit club announcements")
    print("6. Reply to student enquiries")
    print("7. Exit")
    
    choice = input("Enter your choice: ").strip() 

    if choice == '1':
        RegisterCl()
    elif choice == '2':
        Classroom_Search()
    elif choice == '3':
        updateClub()
    elif choice == '4':
        monthlyActivityReportMenu()
        
    elif choice == '5':
        Announcement()
    elif choice == '6':
        Admin_Enquire()
    elif choice == '7':
        menu()
    #error
    else:
        print("Invalid Input")
        menu()
        
def Student():
    
    #admin functions
    '''1. Classroom booking
       2. Check status
       3. Update club details
       4. Monthly activity report
       5. Submit club announcements '''
    
    print("<------------------------------->")
    print("Announcement:")
    #Display()
    print("<------------------------------->")

    print("1. Register")
    print("2. Post enquiry")
    print("3. Search Clubs")
    print("4. View Club Info")
    print("5. View Enquiry")
    print("6. Exit")
    
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        RegisterSt()
    elif choice == '2':
        Student_Enquire()
    elif choice == '3':
        Club_Search()
    elif choice == '4':
        viewClub()
    elif choice == '5':
        Enquire_view()
    elif choice == '6':
        menu()
    #error
    else:
        print("Invalid Input")
        menu()

def monthlyActivityReportMenu():
    print("===Monthly Activity Report===")
    print("1. Create New Report")
    print ("2. View Report")

    choice = input("Enter Choice: ").strip()
    if choice == "1":
        MonthlyActivityReport()
    elif choice == "2":
        MarReport()        
    
def RegisterSt():
    #open student file for appending
    studentFile = open('student.txt','a')
    
    #get student input
    TPno = input("Enter TP number: ").strip().upper()
    name = input("Enter name: ").title()
    intake = input("Enter intake: ").strip().upper()
    contactNumber = int(input("Enter contact number, Please Start with 60: ").strip())
    club_name= input("Enter Club Name: ").strip()
    print("Registration Successful!")
    #print("Your unique ID is: ", newID) ----to be tested
    
    
    #allow student time to read their ID
    continueToNext = input("Type anything to continue....")

    #append student information into a list
    studentList = []
    studentList.append(TPno)
    studentList.append(name)
    studentList.append(club_name)
    studentList.append(intake)
    studentList.append(contactNumber)

    '''add age if necessary'''

    studentFile.write(str(studentList))
    studentFile.write("\n")

    #close patient file
    studentFile.close()
    menu()

def RegisterCl():
    #open student file for appending
    classFile = open('classroom.txt','a')
    
    #get student input
    class_name = input("Enter Classroom Name: ").strip().upper()
    size = int(input("Enter Classroom Size: ").strip())
    num_of_seats = int(input("Enter Number of Seats in Classroom: ").strip())
    projector = input("Does Classroom have a projector? y/n:  ").strip().lower()
    club_name= input("Enter Club Name: ").strip().title()
    status= "pending"
    print("Registration Pending!")
    #print("Your unique ID is: ", newID) ----to be tested
    
    
    #allow student time to read their ID
    continueToNext = input("Type anything to continue....")

    #append student information into a list
    classList = []
    classList.append(class_name)
    classList.append(size)
    classList.append(num_of_seats)
    classList.append(projector)
    classList.append(club_name)
    classList.append(status)

    classFile.write(str(classList))
    classFile.write("\n")

    #close patient file
    classFile.close()
    menu()

def RegisterCb():
    clubFile = open('club.txt','a')

    clubName = input("Enter club name: ").title()
    clubHead = input("Enter Club President name: ").title()
    clubContact = int(input("Enter contact number, Please Start with 60: ").strip())

    clubList = []

    clubList.append(clubName)
    clubList.append(clubHead)
    clubList.append(clubContact)

    clubFile.write(str(clubList))
    clubFile.write("\n")

    clubFile.close()
    menu()

def MonthlyActivityReport():
    marFile = open('mar.txt','a')

    clubName = input("Enter club name: ").title()
    EventName = input("Enter event name: ").title()
    attendees = input("Attendees and participants: ").title()
    numOfClubeMem = int(input("Total number of Club Members: ").strip())
    spending = int(input("Enter total of monthly spendings: ").strip())

    marList = []

    marList.append(clubName)
    marList.append(EventName)
    marList.append(attendees)
    marList.append(numOfClubeMem)
    marList.append(spending)

    marFile.write(str(marList))
    marFile.write("\n")

    marFile.close()
    

def MarReport():
    
    marfile = open("mar.txt", 'r')
    print("Print out Monthly Activity Report")
    Name = input("Enter club name: ").title()

    for line in marfile:
        marList = eval(line)
        clubName = marList[0]
        EventName = marList[1]
        attendees = marList[2]
        numOfClubeMem = marList[3]
        spending = marList[4]
        MonthlyReport = []

        
        if Name == clubName:
            MonthlyReport.append(clubName)
            MonthlyReport.append(EventName)
            MonthlyReport.append(attendees)
            MonthlyReport.append(numOfClubeMem)
            MonthlyReport.append(spending)
            print("Student Status: ",', '.join(map(str, MonthlyReport)))
          
    returntoMainMenu = input(("Press anything to continue!.."))
        # # time.sleep(20)           
    menu()
           

    marfile.close()

# menu()

'''def Search():

   print("1. Student")
    print("2. Club")
    print("3. Classroom")

    choice = input("Enter your choice: ")

    if choice == '1':
        Student_Search()
    elif choice == '2':
        Club_Search()
    elif choice == '3':
        Classroom_Search()'''
    

def Student_Search():
    #open student text file
    studentFile = open('student.txt','r')
    print("====Search Student Information====")
    
    #gets input from student
    findName = input("Search Student Name: ")

    #evaluates all lines in student file
    
    for x in studentFile:
        studentList = eval(x)
        TPno = studentList[0]
        name = studentList[1]
        club_name = studentList[2]
        intake = studentList[3]
        contactNumber = studentList[4]
        student = []

        #if ID input by student matches ID in line of text file, then it will print then student status
        if findName == name:
            student.append(TPno)
            student.append(name)
            student.append(club_name)
            student.append(intake)
            student.append(contactNumber)
            print("Student Status: ",', '.join(map(str, student)))
    
    time.sleep(10)
    menu()

def Classroom_Search():
    #open vaccination file
    classroomFile = open("classroom.txt",'r')
    findClassroom = input("Search Classroom: ")
    
    #checks all lines in vaccination.txt
    for line in classroomFile:
        classroomList = eval(line)
        classroomName = classroomList[0]
        num_of_seats = classroomList[1]
        club_name = classroomList[2]
        status = classroomList[3]
        classroom = []
    
        #if ID input by student matches ID in line of text file, then it will print then student status
        if findClassroom == classroomName:
            classroom.append(classroomName)
            classroom.append(num_of_seats)
            classroom.append(club_name)
            classroom.append(status)
            print("Classroom Status: ",', '.join(map(str, classroom)))
        
        else:
            print("The system does not recognise this classroom name")
    
    time.sleep(10)
    menu()

def Club_Search():
    #open vaccination file
    clubFile = open('club.txt','r')
    findClub = input("Enter Club name: ")
    
    #checks all lines in vaccination.txt
    for line in clubFile:
        clubList = eval(line)
        clubName = clubList[0]
        clubHead = clubList[1]
        clubContact = clubList[2]
        club = []
    
        #if ID input by student matches ID in line of text file, then it will print then student status
        #while loop
        if findClub == clubName:
            club.append(clubName)
            club.append(clubHead)
            club.append(clubContact)
            print("Club Status: ",', '.join(map(str, club)))

    time.sleep(10)
    menu()
    
def Classroom_Booking():
    #open vaccination file
    classroomFile = open("classroom.txt",'r')
    tempFile = open("temp.txt",'a')

    #list of classroom names
    classroomName = ["B14, B15, B16, B17, B18, B19, B20, B21, B22"]
    print("Classroom Name: ",', '.join(map(str, classroomName)))

    findClassroom = input("Search Classroom Name: ")
    

    #checks all lines in vaccination.txt
    for line in classroomFile:
        classroomList = eval(line)
        classroomName = classroomList[0]
        sizeOfClassroom = classroomList[1]
        numOfSeats = classroomList[2]
        projector = classroomList[3]
        clubName = classroomList[4]
        status = classroomList[5]
        classroom = []
    
        #if ID input by student matches ID in line of text file, then it will print then student status
        if findClassroom == classroomName:
            classroom.append(classroomName)
            classroom.append(sizeOfClassroom)
            classroom.append(numOfSeats)
            classroom.append(projector)
            classroom.append(clubName)
            classroom.append(status)
            print("Classroom Status: ",', '.join(map(str, classroom)))
            
            if status == 'pending':
                choice = input("Would you like to approve or rejcet this booking?: ").lower().strip()
                if choice == 'approve':
                    classroomNew=[]
                    classroomNew.append(classroomName)
                    classroomNew.append(sizeOfClassroom)
                    classroomNew.append(numOfSeats)
                    classroomNew.append(projector)
                    classroomNew.append(clubName)
                    classroomNew.append('approved')
                    tempFile.write(str(classroomNew))
                    tempFile.write("\n")
                    print("Status Update Successful!")
                    
                    

                elif choice == 'reject':
                    classroomNew=[]
                    classroomNew.append(classroomName)
                    classroomNew.append(sizeOfClassroom)
                    classroomNew.append(numOfSeats)
                    classroomNew.append(projector)
                    classroomNew.append(clubName)
                    classroomNew.append('rejected')
                    tempFile.write(str(classroomNew))
                    tempFile.write("\n")
                    print("Status Update Successful!")
                else:
                    print("Invalid Input, returning to Main Menu")
                    menu()
            else:
                print("Booking Updated")        
                
    tempFile.close()
    classroomFile.close()
    os.remove("classroom.txt")
    os.rename("temp.txt", "classroom.txt")
    
    menu()
    

def Student_Enquire():
    #collect input for enquiry
    #open student file for appending
    enquireFile = open('enquiry.txt','a')
    
    #get student input
    TPno = input("Enter TP number: ").strip().upper()
    name = input("Enter name: ").title().strip()
    intake = input("Enter intake: ").strip().upper()
    contactNumber = int(input("Enter contact number, Please Start with 60: ").strip())
    enquiry= input("Enter Question: ").strip()
    answer = "Empty"
    print("Enquiry accepted. Answer pending!")
    #print("Your unique ID is: ", newID) ----to be tested
    
    
    #allow student time to read their ID
    continueToNext = input("Type anything to continue....")

    #append student information into a list
    studentList = []
    studentList.append(TPno)
    studentList.append(name)
    studentList.append(intake)
    studentList.append(contactNumber)
    studentList.append(enquiry)
    studentList.append(answer)

    enquireFile.write(str(studentList))
    enquireFile.write("\n")

    #close patient file
    enquireFile.close()
    menu()

def Admin_Enquire():
    #open enquire text file
    enquireFile = open('enquiry.txt','r')
    tempFile = open('temp.txt','a')
    print("====Search Enquiry Information====")
    
    #evaluates all lines in enquire file  

    enquire = []  
    for x in enquireFile:
        enquireList = eval(x)
        TPno = enquireList[0]
        name = enquireList[1]
        intake = enquireList[2]
        contactNumber = enquireList[3]
        enquiry = enquireList[4]
        answer = enquireList[5]
        
        
        enquire.append(TPno)
        enquire.append(name)
        enquire.append(intake)
        enquire.append(contactNumber)
        enquire.append(enquiry)
        enquire.append(answer)
        print("Student Status: ",', '.join(map(str, enquire)))

    enquireFile.close()    
    #Time to input answer
    findTP = input("Enter TP number: ").upper().strip()
    clear()
    print("Student Status: ",', '.join(map(str, enquire)))
    new_answer = input(str("Enter reply: "))
    #evaluate all lines every list
    enquireFile = open('enquiry.txt','r')
    for x in enquireFile:
        newList = eval(x)
        TPno = newList[0]
        name = newList[1]
        intake = newList[2]
        contactNumber = newList[3]
        enquiry = newList[4]
        answer = newList[5]
        nlist = []
    
        if findTP == TPno:
            nlist.append(TPno)
            nlist.append(name)
            nlist.append(intake)
            nlist.append(contactNumber)
            nlist.append(enquiry)
            nlist.append(new_answer)
            print("Student Status: ",', '.join(map(str, nlist)))
            tempFile.write(str(nlist))
            tempFile.write("\n")
        else:
            nlist.append(TPno)
            nlist.append(name)
            nlist.append(intake)
            nlist.append(contactNumber)
            nlist.append(enquiry)
            nlist.append(answer)
            
            tempFile.write(str(nlist))
            tempFile.write("\n")


    enquireFile.close()
    tempFile.close()

    os.remove('enquiry.txt')
    os.rename('temp.txt','enquiry.txt')
    menu()


def View_Classroom_Booking():
    classroomFile = open('classroom.txt','r')
    classroom = []
    for x in classroomFile:
        classList = eval(x)
        classroomName = classList[0]
        sizeOfClassroom = classList[1]
        numOfSeats = classList[2]
        projector = classList[3]
        clubName = classList[4]
        status = classList[5]
        
        classroom.append(classroomName)
        classroom.append(sizeOfClassroom)
        classroom.append(numOfSeats)
        classroom.append(projector)
        classroom.append(clubName)
        classroom.append(status)

        print("Classroom Booking Status: ",', '.join(map(str, classroom)))

    classroomFile.close() 
    menu()

def viewClub():
    clubFile = open('club.txt','r')

    club = []

    for x in clubFile:
        clubList = eval(x)
        clubName = clubList [0]
        clubHead = clubList [1]
        clubContact = clubList [2]

        club.append(clubName)
        club.append(clubHead)
        club.append(clubContact)

        print("Club List: ",', '.join(map(str,club))) 

    clubFile.close()    
def updateClub():
    clubFile= open('club.txt','r')
    tempFile = open('temp.txt','a')
    clubSearch = input("Enter Club Name: ").title()
    for x in clubFile:
        clubList = eval (x)
        clubName = clubList [0]
        clubHead = clubList [1]
        clubContact = clubList [2]

        club = []

        if clubSearch == clubName:

            clubName = input("Enter New Club Name: ").title()
            clubHead = input("Enter New Club Head: ").title()
            clubContact = int(input("Enter New Club Contact: ").strip())
            
            club.append(clubName)
            club.append(clubHead)
            club.append(clubContact)

            tempFile.write(str(club))
            tempFile.write("\n")

        else:
            club.append(clubName)
            club.append(clubHead)
            club.append(clubContact)

            tempFile.write(str(club))
            tempFile.write("\n")
    clubFile.close()
    tempFile.close()

    os.remove('club.txt')
    os.rename ('temp.txt','club.txt')

def Announcement():
    #open file
    announceFile = open('announcement.txt','a')


    #collect input from user
    subject = input("Enter Announcement: ")
    club = input("Enter Club: ")
    date = input("Enter date: ")
    time = int(input("Enter time: "))
    status = "null"

    #if-else to convert 
    if time == "EMPTY":
        time = str(time)
    elif time == "NULL" or "null":
        time = str(time)
    else:
        time = time
    
   
    announceList = []

    announceList.append(subject)
    announceList.append(club)
    announceList.append(date)
    announceList.append(time)
    announceList.append(status)

    announceFile.write(str(announceList))
    announceFile.write("\n")

    print("Press any key to continue... ")
    announceFile.close()
    menu()

def Announcement_review():
    #open announcement file
    File = open('announcement.txt','r')
    tempFile = open("tempt.txt", 'a')
    print("====Search Announcement Information====")
    
    #gets input from student
    findName = input("Search Club: ")

    

    #evaluates all lines in student file
    
    for x in File:
        announcementList = eval(x)
        club = announcementList[1]
        subject = announcementList[0]
        date = announcementList[2]
        time = announcementList[3]
        status = announcementList[4]
        announcement = []

        
    #if ID input by student matches ID in line of text file, then it will print then student status
    #comparison for what to set as display'''
    if findName == club:
            announcement.append(subject)
            announcement.append(club)
            announcement.append(date)
            announcement.append(time)
            announcement.append(status)
            print("Student Status: ",', '.join(map(str, announcement)))
            
            if status == 'null':
                choice = input("Would you like to approve or rejcet this announcement?: ").lower().strip()
                if choice == 'approve':
                    classroomNew=[]
                    classroomNew.append(subject)
                    classroomNew.append(club)
                    classroomNew.append(date)
                    classroomNew.append(time)
                    classroomNew.append('approved')
                    tempFile.write(str(classroomNew))
                    tempFile.write("\n")
                    print("Status Update Successful!")
                    
                    

                elif choice == 'reject':
                    classroomNew=[]
                    classroomNew.append(subject)
                    classroomNew.append(club)
                    classroomNew.append(date)
                    classroomNew.append(time)
                    classroomNew.append('rejected')
                    tempFile.write(str(classroomNew))
                    tempFile.write("\n")
                    print("Status Update Successful!")
                else:
                    print("Invalid Input, returning to Main Menu")
                    menu()
            else:
                print("Booking Updated")        
                
    tempFile.close()
    File.close()
    os.remove("announcement.txt")
    os.rename("tempt.txt", "announcement.txt")
    

    #end and return to menu
    user = input("Press anything to return to menu... ")
    menu()

def Display():
    announcementfile = open("announcement.txt", 'r')


    for line in announcementfile:
        announcementList = eval(line)
        subject = announcementList[0]
        club = announcementList[1]
        date = announcementList[2]
        time = announcementList[3]
        status = announcementList[4]
        announcement = []

        if status == "approved":
            announcement.append(subject)
            announcement.append(club)
            announcement.append(date)
            announcement.append(time)
            announcement.append(status)
            print("Student Status: ",', '.join(map(str, announcement)))

    input("Press anything to continue!..")
    login()
        
    

    announcementfile.close()

def Enquire_view():
    #open vaccination file
    enqFile = open('enquiry.txt','r')
    findTP = input("Enter TP no: ")
    
    #checks all lines in vaccination.txt
    for line in enqFile:
        clubList = eval(line)
        TPno = clubList[0]
        name = clubList[1]
        intake = clubList[2]
        contactNumber = clubList[3]
        enquiry = clubList[4]
        answer = clubList[5]
        club = []
    
        #if ID input by student matches ID in line of text file, then it will print then student status
        #while loop
        if findTP == TPno:
            club.append(TPno)
            club.append(name)
            club.append(intake)
            club.append(contactNumber)
            club.append(enquiry)
            club.append(answer)
            print("Club Status: ",', '.join(map(str, club)))
        else:
            print("Enquiry not found")

    time.sleep(10)
    menu()

Display()