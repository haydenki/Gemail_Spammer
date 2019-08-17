# Gemail_Spammer, a simple script for playing a harmless prank on your friends.
# Written by haydenki, on 12/13/18

import smtplib

def start_screen():
    print("          _nnnn_ ")
    print("         dGGGGMMb")
    print("        @p~qp~~qMb     Gemail_Spammer.py")
    print("        M|@||@) M|")
    print("        @,----.JM|")
    print("       JS^\__/  qKL    MADE by haydenki")
    print("      dZP        qKRb")
    print("     dZP          qKKb")
    print("    fZP            SMMb")
    print("    HZM            MMMM")
    print("    FqM            MMMM")
    print("  __|\" .        |dS\"qML")
    print("  |    `.       | `' \Zq")
    print(" _)      \.___.,|     .'")
    print(" \____   )MMMMMP|   .'")
    print("      `-'       `--' hjm")
    print("[1] - Start gemail spammer")
    print("[2] - Exit")
    start_screen_choices()

def start_screen_choices():
    choice = input(">")
    if (str(choice) == "1"):
        get_details()
    elif (str(choice) == "2"):
        exit()
    while (str(choice) not in ["1","2"]): # This part is to handle user input and make sure its correct
        print("\"" + choice + "\" isnt a valid option, try again.") 
        start_screen_choices()
		
def get_details():
    # This fixes this weird glitch that prompts the user to type when their not supposed to.
    choice = "1"
    # Get all the info required to send the emails (login, msg, etc)
    global u_uid,u_pwd,target_email,target_subject,target_message,message_count,smtp_address
    smtp_address = input("Enter SMTP server address:")
    u_uid = input("Enter your email:")
    u_pwd = input("Enter your password:")
    target_email = input("Enter the email you want to spam:")
    target_subject = input("Enter the email subject:")
    target_message = input("Enter the email text:")
    message_count = int(input("# of emails to send:"))
    send_email()
    
def send_email():
    global send_count, failed_mail, successful_mail
    send_count = 1
    failed_mail = 0
    successful_mail = 0
    print("+----------------------------+")
    for i in range(message_count): ## for loop to send multiple emails
        try:
            # Attempt to connect to the smtp server
            mail_server = smtplib.SMTP(smtp_address)
            mail_server.ehlo()
            mail_server.starttls()
            # Attempt to login to email
            mail_server.login(u_uid, u_pwd)
            # Format messge then email it
            mail_message = "Subject: {}\n\n{}".format(target_subject,target_message)
            mail_server.sendmail(u_uid, target_email, mail_message)
            mail_server.quit()
            print(str(send_count) + " email(s) successfully sent!")
            send_count += 1
            successful_mail += 1
        except:
            print("email " + str(send_count) + " failed to send!")
            send_count += 1
            failed_mail += 1
    after_report()

def after_report():
    # Prints out a report on how many emails successully went through
    print("Spam completed.")
    print("Sent = " + str(successful_mail) + " Failed = " + str(failed_mail))

start_screen()
