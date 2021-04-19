import re
import imaplib

def checkinbox(user,passw,imapserver):
   imap = imaplib.IMAP4_SSL(imapserver)
   try:
      imap.login(user,passw)
      print("Connecting and Fetching required info,Please Wait..")
      select_folder = input("Enter the folder : ")   
      imap.select(select_folder)
      status, messages = imap.select(select_folder)
      messages = int(messages[0])
      print(f"Total Number of Mails in {select_folder} : {messages} ")
   except Exception as err:
      print(' -- !! AUTHENTICATION-FAILED !! --')      
      print("It seems that password was incorrect.")
def checkemail(user,passw,imapserver):
   regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'    
   if(re.search(regex, user)):
      print("Valid Email Entered")
   else:      
      print("!! Enter a Valid Email and Try Again !!")

def deleteEmail(user, passw, imapserver):
   checkemail(user,passw,imapserver)
   mail = imaplib.IMAP4_SSL(imapserver)
   mail.login(user, passw)
   try:
      print("Connecting and Fetching required info,Please Wait..")
      mail.select("inbox")
      print(f"Deleting all Emails from the inbox")
      
      typ, data = mail.search(None, 'ALL')
      for num in data[0].split():
         mail.store(num, '+FLAGS', r'(\Deleted)')
         print("Deleting....")
      mail.expunge()
      print("Emails Deleted")
      mail.close()
      mail.logout()
   except Exception as err:
      print(' -- !! AUTHENTICATION-FAILED !! --')      
      print("It seems that password was incorrect.")
