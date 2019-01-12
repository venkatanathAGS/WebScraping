from bs4 import BeautifulSoup as soap
from urllib.request import urlopen as uReq
my_url = "https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_6&otracker1=AS_QueryStore_OrganicAutoSuggest_0_6&as-pos=0&as-type=RECENT&as-searchtext=iphone"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soap = soap(page_html,"html.parser")


containers = page_soap.findAll("div",{"class":"_1-2Iqu row"})
#print(len(containers))
#print(soap.prettify(containers[0]))

container = containers[0]
name = container.findAll("div",{"class":"_3wU53n"})
#print(name[0].text)

price = container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
#print(price[0].text)

Ratings = container.findAll("div",{"class":"niH0FQ"})
#print(Ratings[0].text)

filename = "products.csv"
f= open(filename,"w" , encoding='utf-8')
headers = "ProductName , Price , Ratings\n"
f.write(headers)
#finalrating =[]
#rm_rupee = []

for container in containers:
    product_name = container.findAll("div",{"class":"_3wU53n"})
    name = product_name[0].text.strip()
    price_container = container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()
    rating_container = container.findAll("div",{"class":"niH0FQ"})
    Ratings = rating_container[0].text.strip()
    #print("productName : " + name)
    #print("Price : " + price)
    #print("Ratings : " + Ratings)

    #string parsing
    trim_price = price.split("₹")
    rm_rupee = "Rs" + trim_price[1]
    rm_rupee = ''.join(rm_rupee.split(','))
    rm_rupee = rm_rupee[0:7]
    split_rating = Ratings.split(",")
    finalrating = split_rating[0]
    finalrating = finalrating[0:3]

    print(name.replace(",","|") + " , " + rm_rupee + " , " + finalrating + "\n")
    f.write(name.replace(",","|") + " , " + rm_rupee + " , " + finalrating + "\n")
f.close()
