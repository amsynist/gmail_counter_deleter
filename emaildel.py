

# def deleteEmailIMAP(user, password, IMAP):
#     mail = imaplib.IMAP4_SSL(IMAP)
#     mail.login(user, password)
#     mail.select("inbox")
#     typ, data = mail.search(None, 'ALL')
#     for num in data[0].split():
#         mail.store(num, '+FLAGS', r'(\Deleted)')
#     mail.expunge()
#     mail.close()
#     mail.logout()
    
# deleteEmailIMAP(email, passw, imapserver)


import re
import imaplib
import sys

# import imaplib

# input your email address
user = "sumanthreddybijjur09@gmail.com"
# input your email password
passw = "8184889343@2345"
# input imap server. Look at this https://www.arclab.com/en/kb/email/list-of-smtp-and-imap-servers-mailserver-list.html 
imapserver = "imap.gmail.com"
list_response_pattern = re.compile(
    r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)'
)
def checkinbox(user,passw,imapserver):
    imap = imaplib.IMAP4_SSL(imapserver)
    imap.login(user,passw)
    # select_folder = input("Enter the folder : ")   
    # imap.select("inbox")
    # status, messages = imap.select(select_folder)
    # messages = int(messages[0])
    # print(f"Total Number Mails in {select_folder} : {messages} ")
    f = open(r"C:\Users\KALYANI\Desktop\data.txt",'w')
    dir = imap.list()
    for i in imap.list()[1]:
        l = i.decode().split(' "/" ')
        for mails_dir in l:
            print (mails_dir)
            dir = mails_dir
            for line in re.findall("[Gmail]/.*", dir):        
                for lis in line[1]:
                    print(lis)
                    sys.stdout=open(f,"w")
                    print (lis)
                    sys.stdout.close()
                    
        

checkinbox(user,passw,imapserver)