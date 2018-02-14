import smtplib#simple mail transfer protocol
#prtocol-its a standard defined which is used to exchange data
server = smtplib.SMTP('smtp.gmail.com',587)#start session
server.starttls()#opening the session
#transport layer security 
server.login("nithind7026@gmail.com", "###########")#logging into the account
msg = "heyyyyy.....how art thou doing"#the actual message
server.sendmail("nithind7026@gmail.com", "nischay.17cs@cmr.edu.in", msg)#sending the mail
print("sucess")
server.quit()#closing the server
