"""
In this project, I will scrape data Frontpage Slickdeals from slickdeals.net.
For each deal, I will collect the information about the following:
    Vendor Name
    Item Name
    List Price (If available)
    Discounted price
"""

from bs4 import BeautifulSoup as soup
import requests as Req

# The url of the website we want to scrape data from
my_url = "https://slickdeals.net/"


page_url = Req.get(my_url)
page_soup = soup(page_url.content, "html.parser")

"""
Now we have all the information on the website.
But it is all garbled, just like a bowl of soup
We need to find what we are looking for and get it. 
There are multiple ways to obtain those list items. 
Observing that each deal is in a division with  class name fpItem
I will choose all division with that class name 
PS: At this stage https://beautifier.io/ is really nice source 
to better see the structure of the website

"""
deals = page_soup.findAll("div", attrs={"class":"fpItem"})
header = "Deal Name, Vendor, Original Price, Discounted Price\n"

"""
For a given container deal, which is a bs4 element, following functions will
find and return the 
- Item's Name
- Vendor's Name
- Original List Price
- Discounted Price
"""
def itemTitle(deal):
    return deal.find("a", attrs={"class":"itemTitle"}).text.strip().replace(",", "|")

def itemStore(deal):
    try:
        return deal.find("a", attrs={"class":"itemStore"}).text.strip()
    except:
        return deal.find("span", attrs={"class":"itemStore"}).text.strip()

def listPrice(deal):
    try:
        return deal.find("div", attrs={"class":"listPrice"}).text.strip()
    except:
        try:
            return deal.find("span", attrs={"class":"oldListPrice"}).text.strip() 
        except:
            return 'Not Available'

def itemPrice(deal):
    p = deal.find("div", attrs={"class":"itemPrice"}).text.strip().split("\n")[0].strip().replace(",", "")
    if "%" in p:
        return "Not Available"
    else:
        return p

f = open("Deals.csv", "w")
f.write(header)
for deal in deals[1:-2]:
    line = itemTitle(deal) + "," + itemStore(deal) + "," + listPrice(deal) + "," + itemPrice(deal)+ "\n" 
    f.write(line)
f.close()
