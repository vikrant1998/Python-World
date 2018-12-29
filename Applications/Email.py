import imaplib
import email
import email.parser
import os
import re

"""
Reads out any latest email
"""

def SpeakSentence(sentence):
    os.system("say " + sentence)

def GetEmail():
    myusername = 'email@gmail.com'
    mypassword = 'password'

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(myusername, mypassword)
    mail.list()

    mail.select("inbox")

    result, data = mail.search(None, "ALL")
    if data == None or data == [] or data == ['']: return None, None, None

    ids = data[0] # data is a list.
    id_list = ids.split() # ids is a space separated string
    if id_list == None or id_list == []:
        return None, None, None
    latest_email_id = id_list[-1] # get the latest

    result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
    raw_email = data[0][1].decode('utf8')

    msg = email.message_from_string(raw_email)

    mailBody = list()
    b = email.message_from_string(str(msg))
    if b.is_multipart():
        for payload in b.get_payload():
            mailBody.append(payload.get_payload())
    else:
        mailBody.append(b.get_payload())

    if len(mailBody) > 1: mailBody = mailBody[0]


    fromEmail = msg['From'].split('<')[0].strip()

    mailBody = mailBody.split()
    mailBody = " ".join(mailBody)

    mailSubject = msg['Subject'].split()
    mailSubject = " ".join(mailSubject)

    fromEmail = re.sub("'", "", fromEmail)
    fromEmail = re.sub('"', '', fromEmail)
    mailBody = re.sub("'", "", mailBody)
    mailBody = re.sub('"', '', mailBody)
    mailSubject = re.sub("'", "", mailSubject)
    mailSubject = re.sub('"', '', mailSubject)

    return fromEmail, mailSubject, mailBody

if __name__ == "__main__":

    while True:
        fromEmail, subject, body = GetEmail()

        if fromEmail != None:
            print (fromEmail)
            print (subject)
            print (body)
            SpeakSentence("You have a new email from " + fromEmail)
            SpeakSentence("Subject reads " + subject)
            SpeakSentence("The message is " + body)
