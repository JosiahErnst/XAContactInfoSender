from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Student
import smtplib

# The method to create the homePage and POST the information entered
def homePage(request):
    if request.method == "POST":
        form = Student(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
    else:
        form = Student()
    return render(request, 'homeSite/base.html', {"form" : form})

# Uses the POSTed information from above and utilizes the methods below to send the information to the Chi
# Alpha campus directors
def thankYou(request):
    fname = request.POST['first_name']
    lname = request.POST['last_name']
    email = request.POST['email']
    phone = request.POST['phone']
    major = request.POST['major']
    church = request.POST['church']
    churchLoc = request.POST['churchLocation']
    pastor = request.POST['pastor']
    gradYear = request.POST['gradYear']
    notListed = request.POST['ifNotListed']
    counter = 0
    emailSender(request.POST['First_Choice_College'], "first", fname, lname, email, phone, major, church, churchLoc, pastor, gradYear, notListed, counter)
    emailSender(request.POST['Second_Choice_College'], "second", fname, lname, email, phone, major, church, churchLoc, pastor, gradYear, notListed, counter)
    emailSender(request.POST['Third_Choice_College'], "third", fname, lname, email, phone, major, church, churchLoc, pastor, gradYear, notListed, counter)
    emailCopySender("2", fname, lname, email, phone, major, church, churchLoc, pastor, gradYear)
    return render(request, 'homeSite/thankYou.html', {})

# This method takes in the selections the student made and matches them to their respective spots
# in the formated email, then sends said email
def emailSender(collegeChoice, priority, fname, lname, email, phone, major, church, churchLoc, pastor, gradYear, notListed, counter):
    if (collegeChoice == "12"):
        return
    if (collegeChoice == "13" and counter == 0):
        notListedSender(fname, lname, email, phone, major, church, churchLoc, pastor, gradYear, notListed)
        counter += 1
        return
    SENDING_EMAIL = "joshua@chialpha.org"
    RECEIVING_EMAILS = {"5": "emails of the directors", 
                        "7": "jd.winkelman@gmail.com", 
                        "9": "riverfallsxa@gmail.com",
                        "3": "chialphauwec@gmail.com",
                        "4": "newchialpha@gmail.com",
                        "6": "chialphamadison@gmail.com",
                        "8": "joshua@chialpha.org",
                        "10": "chialpha@uwsp.edu",
                        "11": "kalynmzimmer@gmail.com",
                        "2": "jonriemer316@gmail.com",
                        "1": "jen.broberg@gmail.com",
                        }
    # SENDER_PASS was purposely changed to a password that would not work, for security reasons
    SENDER_PASS = "Password goes here"
    message = "Student Information:  \n Name: "+ str(fname) +" "+ str(lname) +"\n Email: "+ str(email) +" \n Phone Number: "+ str(phone) +" \n Major: "+ str(major) +" \n Church: "+ str(church) +" \n Church Location: "+ str(churchLoc) +" \n Pastor: "+ str(pastor) +" \n Graduation Year: "+ str(gradYear) +" \n"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=SENDING_EMAIL, password=SENDER_PASS)
        connection.sendmail(
            from_addr=SENDING_EMAIL,
            to_addrs=RECEIVING_EMAILS[collegeChoice],
            msg=f"Subject:New Student Info from "+ str(fname) +" "+ str(lname) +"! You were their "+ str(priority) +" choice \n\n" + message)
    return

# In the case of the student selecting Not Listed, the not listed college is then sent to the director for the state to
# forward on to the out of state colleges
def notListedSender(fname, lname, email, phone, major, church, churchLoc, pastor, gradYear, request):
    SENDING_EMAIL = "joshua@chialpha.org"
    RECEIVING_EMAILS = "joshua@chialpha.org"
    # SENDER_PASS was purposely changed to a password that would not work, for security reasons
    SENDER_PASS = "Password goes here"
    message = "Student Information:  \n Name: "+ str(fname) +" "+ str(lname) +"\n Email: "+ str(email) +" \n Phone Number: "+ str(phone) +" \n Major: "+ str(major) +" \n Church: "+ str(church) +" \n Church Location: "+ str(churchLoc) +" \n Pastor: "+ str(pastor) +" \n Graduation Year: "+ str(gradYear) +" \n Colleges Selected Outside WI: "+ str(request)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=SENDING_EMAIL, password=SENDER_PASS)
        connection.sendmail(
            from_addr=SENDING_EMAIL,
            to_addrs=RECEIVING_EMAILS,
            msg=f"Subject:Student Info for "+ str(fname) +" "+ str(lname) +"! \n\n" + message)
    return

# This method simply acts as a way to send a confirmation email to the student with some of the information entered
def emailCopySender(receiver, fname, lname, email, phone, major, church, churchLoc, pastor, gradYear):
    SENDING_EMAIL = "joshua@chialpha.org"
    RECEIVING_EMAILS = {"1": "joshua@chialpha.org", 
                        "2": str(email), 
                        }
    # SENDER_PASS was purposely changed to a password that would not work, for security reasons
    SENDER_PASS = "Password goes here"
    message = "Student Information:  \n Name: "+ str(fname) +" "+ str(lname) +"\n Email: "+ str(email) +" \n Phone Number: "+ str(phone) +" \n Major: "+ str(major) +" \n Church: "+ str(church) +" \n Church Location: "+ str(churchLoc) +" \n Pastor: "+ str(pastor) +" \n Graduation Year: "+ str(gradYear) +" \n"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=SENDING_EMAIL, password=SENDER_PASS)
        connection.sendmail(
            from_addr=SENDING_EMAIL,
            to_addrs=RECEIVING_EMAILS[receiver],
            msg=f"Subject:Copy of Student Info for "+ str(fname) +" "+ str(lname) +"! \n\n" + message)
    return
