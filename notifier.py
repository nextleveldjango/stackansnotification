import sys
import time
import urllib2

from bs4 import BeautifulSoup


def send_email():
    print('SENDING EMAIL')


def main(email_sent, url):
    """
    """
    try:
        url = urllib2.urlopen(url)
        data = url.read()

        soup = BeautifulSoup(data)
        if(not soup):
            raise Exception

        answer_div = soup.find('div', class_="answers-subheader")
        if(not answer_div):
            raise Exception
        assert answer_div.h2.__str__() != "<h2>\n</h2>"
        send_email()
        print("Got Answer, :) :-> Email Sent")
        return True
    except AssertionError:
        print('No Answer') 
        time.sleep(5)
        return False
    except Exception as exc:
        print('Problem with Url, please pass valid stackoverflow url', exc.message)
        return True


if __name__ == '__main__':
    """
    """
    try:
        url = sys.argv[1]
    except KeyError:
        print('Please pass valid stackoverflow url')
        sys.exit()
    email_sent = False
    while(not email_sent):
        email_sent = main(email_sent, url) 
