from sys import exit
from random import randint
from textwrap import dedent
import datetime


class certDetails(object):
    def __init__(self, name):
        self.userName = name    
    title = ()
    subTitle = ()
    issuerOrg = ()
    issuerName = ()
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    
####
#Say hello to the user and get their name
def welcomeMessage():
    print("""
==========================================================================================    
                                        ~~CERTIFY-IFY~~
                                       
                              THE WONDERFUL CERTIFICATE CREATOR 
                        make your own certs yeeehaaa yippy hurrrayyyy

==========================================================================================    
    """)    
    print('Enter your name -- full name, fake name, whatevs...')
    yourName = input('>> ')
    print("""
    ..........
    """)
    print(f"You're name is {yourName}??? That's a name???")
    while True:
        confirm = input('y/n > ')
        if confirm == 'y' or confirm == 'n':
            break
    
    print("""
    ..........
    I don't care... Let's continue.
    ..........
    """)
    
    return yourName

####
#Ask them what their certification is for
def getCertDetails(cert):
    #Certification type
    print(f"So... {cert.userName}... what type of certification is this for?")
    cert.title = input('Enter a title >> ')
    
    #Certification title
    print("""
    ..........
    """)
    print(f"Wow... {cert.title}... that's so interesting... please continue.")
    cert.subTitle = input('Enter a Sub Title Description >> ')
    
    #Organization providing certificate
    cert.issuerOrg = input('Enter name of issuer Organization >> ')
    
    #Organization representative issuing certificate 
    cert.issuerName = input('Enter name of issuer Representative >> ')
    
    return cert

####
#Review the certification
def certReview(cert):
    print("""
    ..........
    """)
    print(f"Alrighty, {cert.userName}... Let's review your lies!")
    print(f"A) Certification Title: {cert.title}")
    print(f"B) Certification Sub-Title: {cert.subTitle}")
    print(f"C) Certification Issuing Org: {cert.issuerOrg}")
    print(f"D) Certification Issuer's Name: {cert.issuerName}")

####
#Does anything need to be edited?
def checkAccuracy():
    print("""
    ..........
    """)
    print(f"Are all of these details correct?")
    while True:
        confirm = input('y/n > ')
        if confirm == 'y':
            return True
        elif confirm == 'n':
            return False
        
####
#Select what to edit 
def selectModify(): 
    print("""
    ..........
    """)
    print(f"Select an item to modify:")
    modify = input('a/b/c/d > ')
    if modify == 'a' or modify == 'b' or modify == 'c' or modify == 'd':
        return modify
    else:
        selectModify()
    
####
#Edit certification
def editCert(cert, modify): 
    if modify == 'a':
        print(f"Current certification title is: {cert.title}")
        cert.title = input('Insert new title > ')
    elif modify == 'b':
        print(f"Current certification sub-title is: {cert.subTitle}")
        cert.subTitle = input('Insert new sub-title > ')
    elif modify == 'c':
        print(f"Current certification issuing org is: {cert.issuerOrg}")
        cert.issuerOrg = input('Insert issuing org > ')
    else:
        print(f"Current certification issuer's name: {cert.issuerName}")
        cert.issuerName = input('Insert new issuer name > ')      
    return

####
#Validate certification and print if all is a ok
def certValidation(cert):
    while True:
        certReview(cert)
        complete = checkAccuracy()
        if complete == True:
            printCert(cert)
            print("Enjoy your certification! Be sure to rub it in everyone's face!")
            return False
        else:
            modify = selectModify()
            editCert(cert, modify)
  
####
#Print Certification  -TODO make the equals center the title, align everything to center
def printCert(cert):
    leftTitle = int((90 - len(cert.title) - 4)/2)
    rightTitle = leftTitle
    leftTitle += 1 if (len(cert.title) % 2 == 1) else 0
    
    leftSubTitle = int((90 - len(cert.subTitle) - 4)/2)
    rightSubTitle = leftSubTitle
    leftSubTitle += 1 if (len(cert.subTitle) % 2 == 1) else 0
    
    leftIssuer = int((88 - len(cert.issuerName) - 4 - len(cert.issuerOrg))/2)
    rightIssuer = leftIssuer
    leftIssuer += 1 if ((len(cert.issuerName) + 4 + len(cert.issuerOrg)) % 2 == 1) else 0
    
    leftHereby = int((88 - len(str(cert.year)) - len(str(cert.month)) - len(str(cert.day)) - 35)/2)
    rightHereby = leftHereby
    leftHereby += 1 if ((len(str(cert.year)) + len(str(cert.month)) + len(str(cert.day)) + 1) % 2 == 1) else 0
    
    leftUser = int((88 - len(cert.userName))/2)
    rightUser = leftUser
    leftUser += 1 if ((len(cert.userName)) % 2 == 1) else 0
    
    leftShall = int((88 - len(cert.title) - 50)/2)
    rightShall = leftShall
    leftShall += 1 if ((len(cert.title)) % 2 == 1) else 0
    
    leftMay = int((88 - len(cert.userName) - 49)/2)
    rightMay = leftMay
    leftMay += 1 if (((len(cert.userName)) + 1) % 2 == 1) else 0
    
    print(f"""
==========================================================================================
==========================================================================================
=============================== OFFICIAL CERTIFICATION FOR ===============================
==========================================================================================
{'=' * leftTitle}  {cert.title.upper()}  {'=' * rightTitle}
========================================================================================== 
={' ' * (leftSubTitle - 1)}  {cert.subTitle.upper()}  {' ' * (rightSubTitle - 1)}=
={' ' * 88}=
={' ' * 88}=
={' ' * leftIssuer}{cert.issuerName.upper()} OF {cert.issuerOrg.upper()}{' ' * rightIssuer}= 
={' ' * 88}=
={' ' * leftHereby}HEREBY CERTIFIES THAT AS OF {cert.year}-{cert.month}-{cert.day} THAT{' ' * rightHereby}=
={' ' * 88}=
={' ' * leftUser}{cert.userName.upper()}{' ' * rightUser}=
={' ' * 88}=
={' ' * leftShall}SHALL FROM HENCE FORTH BE KNOWN AS AN OFFICIAL {cert.title.upper()}'er{' ' * rightShall}= 
={' ' * 88}=
={' ' * 88}=
={' ' * 88}=
={' ' * leftMay}MAY NO LIVING CREATURE TAKE THIS GLORY AWAY FROM {cert.userName.upper()}{' ' * rightMay}=
={' ' * 88}=
={' ' * 88}=
==========================================================================================
==========================================================================================
==========================================================================================
==========================================================================================


    """)   

###
#Run certificationify
userName = welcomeMessage()
cert = certDetails(userName)
getCertDetails(cert)
certValidation(cert)

