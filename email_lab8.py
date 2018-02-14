import smtplib
 
server = smtplib.SMTP('smtp.gmail.com',587)#start session
server.starttls()#opening the session
server.login("nithind7026@gmail.com", "7026378456")#logging into the account
msg = "heyyyyy.....how art thou doing"#the actual message
server.sendmail("nithind7026@gmail.com", "nischay.17cs@cmr.edu.in", msg)#sending the mail
print("sucess")
server.quit()#closing the server
