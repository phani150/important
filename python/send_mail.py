#!/usr/bin/python3
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.login("phanivr99@gmail.com", "Phanindra099!@#")

#Send the mail
msg = "Hello World !" # The /n separates the message from the headers
server.sendmail("phanivr99@gmail.com", "dph8086@gmail.com", msg)

