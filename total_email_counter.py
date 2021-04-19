from funcs import checkinbox,checkemail,deleteEmail
while True:
   while True:
      
   #do something
      user = input("Enter your Email Address : ")
      passw = input("Enter your Password : ")
      
      while True:
         imapserver = input("""Select imap mail server or Enter if any other 
         1.imap.gmail.com(Gmail Server)
         2.Not Gmail Server..? Enter other imap Server if not
         Enter 1 or 2 : """)   
         choice = int(imapserver)
         if choice==1:     
               print ("imap.gmail.com is selected")
               imapserver = "imap.gmail.com"
               break
         elif choice==2:
               imapserver = input("Enter imap Server : ")
               break
         else:
               input("Wrong option selection. Enter any key to try again..")
               continue

      regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
      

      while True:
         opt = input("""--Enter any Option Below--
         1.CHECK TOTAL NUMBER OF EMAILS IN FOLDER
         2.DELETE ALL EMAILS FROM THE FOLDER
         Enter 1 or 2 : """)   
         opts = int(opt)
         if opts==1:   
               checkemail(user,passw,imapserver)
               checkinbox(user,passw,imapserver)
               break
         elif opts==2:
               checkemail(user,passw,imapserver)
               deleteEmail(user, passw, imapserver)
               break
         else:
               input("Wrong option selection. Enter any key to try again..")
               continue
      answer = str(input("Run Again(y/n): "))
      
      if answer in ('y', 'n'):
         break
      print("invalid input.")
   if answer == 'y':
      continue
   else:
      print("Exiting the Script..")
      break