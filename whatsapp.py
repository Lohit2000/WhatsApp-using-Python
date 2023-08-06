import pywhatkit

phone = input("enter phn num: ")
mesg = input("enter mesg")

pywhatkit.sendwhatmsg_instantly(phone,mesg)
