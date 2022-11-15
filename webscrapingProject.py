from urllib.request import urlopen, Request
from bs4 import BeautifulSoup 

import keys3
from twilio.rest import Client
#from urllib.request import urlopen, Request



url = "https://coincodex.com/"



#given
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers = headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')


# Prints title (unnecessay)
print()
title = soup.title
print(title.text)
print()



tablerows = soup.findAll("tr")

counter = 1

for cell in range(1,6):
    td = tablerows[cell].findAll("td")
    print("Name: " + td[1].text)
    print("Current Price: " + td[2].text)
    print("% Change in the last 24 hours: " + td[3].text)
    percent_change = td[3].text

    # %change number
    format_change = float(percent_change.replace("%",""))
    format_change1 = format_change *.01

    #current price number
    current_price = td[2].text
    format_price = (current_price.replace("$",""))
    format_price1 = float(format_price.replace(",",""))
    format_price2 = format_price1*format_change1


    old_price = format_price1 - format_price2
    print("Price 24 hours ago: $ {:,.6f}".format(old_price))
    print()
    print()
#ONE AT A TIME
    input()



#NOTIFICATION PART

notification1 = "Bitcoin (BTC) has fallen below $40,000"
notification2 = "Ethereum (ETH) has fallen below $3,000"

myself = Client(keys3.accountSID, keys3.authToken)

TwilioNumber = "+18326482681"
myCellphone = '+18328040430'


if format_price1 < 40000:
    textmsg = myself.messages.create(to=myCellphone, from_= TwilioNumber, body = notification1)
    
if format_price2 < 3000:
    textmsg = myself.messages.create(to=myCellphone, from_= TwilioNumber, body = notification2)


