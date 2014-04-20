import urllib2
import smtplib

from bs4 import BeautifulSoup

def func(send_email):
    url = urllib2.urlopen("http://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list")
    data = url.read()
    soup = BeautifulSoup(data)
    if soup.find('div', class_="answers-subheader").h2.__str__() != "'<h2>\n</h2>":
        message = "Congrats , You got a answer."
        try:
            smtpObj = smtplib.SMTP('127.0.0.1', 25, 'localhost')
            smtpObj = smtplib.SMTP('localhost')
            smtpObj.sendmail(sender, receivers, message)        
            print "Successfully sent email"
        except:
            print "Error: unable to send email"
    return "Done"
    print "Still waiting for answer."
    return "No"

if __name__ == '__main__':
    send_email = "No"
    while send_email == "No":
        send_email = func(send_email) 
