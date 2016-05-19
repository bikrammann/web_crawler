import requests
from bs4 import BeautifulSoup

# Change the url according to the currency you are trying to convert.
url = 'http://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=INR'

#This demonstration is for educational purposes only.
#You have to use custom header to go past their automatic crawler detection
#Otherwise you will get this message "WARNING: Automated extraction of rates is prohibited under the Terms of Use" and your program will stop.

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.108 Safari/537.36'}

r = requests.get(url, headers=header)
soup = BeautifulSoup(r.content,'html.parser')
td = soup.find_all("td", class_="leftCol")

rupees = float(td[-1].string[7:-4])
print('1 USD = {} Rupees'.format(rupees))

