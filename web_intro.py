import requests
from bs4 import  BeautifulSoup as bs 
from urllib.request import urlopen
import logging

"""Objective is to get data from web for eg getting reviews of product from flipkart"""

# filpkart_url = 'https://www.flipkart.com/search?q=' + 'iphone+14+pro' 
# url_client= urlopen(filpkart_url) #it will open the respective url which is passed
# flipkart_page = url_client.read()   #url_client.read() it will read all the html of that page 
# # print(flipkart_page)
# filpkart_html = bs(flipkart_page,'html.parser')  #this will little bit beautify the html content of page so that we can read it using beautifulsoap
# # print(filpkart_html)
# url_of_product = 'https://www.flipkart.com'+'https://www.flipkart.com/apple-iphone-14-pro-deep-purple-128-gb/p/itm75f73f63239fa?pid=MOBGHWFHYGAZRWFT&lid=LSTMOBGHWFHYGAZRWFTJTZIDA&marketplace=FLIPKART&q=iphone+14+pro&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&fm=organic&iid=5357cd85-2d3c-4fe8-a3fe-7b08e47f383d.MOBGHWFHYGAZRWFT.SEARCH&ppt=hp&ppn=homepage&ssid=11cwgenxcw0000001678788095972&qH=73a41d19c3188cc2'
# #getting each product block by using div and their class name instead of going one by one using url
# bigbox = filpkart_html.find_all("div",{"class" : "_1AtVbE col-12-12"})
# # print(len(bigbox))
# del bigbox[0:3] #bcoz it contain some starting boxes which is not of product
# #now we have to reach to our href which is inside of div inside of div check at html inspect
# bigbox[0].div.div.div.a #we have reached to a tag now get the href
# bigbox[0].div.div.div.a['href']
# #print(bigbox[0].div.div.div.a['href']) #finally getting href which is inside of a tag this is for single block for whole boxes we have to ierate using loop
# """Now if we append this with flipkart url we will directly reached to the product"""
# productlink = "https://www.flipkart.com" + bigbox[0].div.div.div.a['href'] # we have got the product 1 
# #for all the product just iterate 
# # for i in bigbox:
# #     print("https://www.flipkart.com" + i.div.div.div.a['href'])

# product_req = requests.get(productlink) #scrap whole data of the page
# product_html=bs(product_req.text,'html.parser')
# # print(product_html)
# """Now out of whole data we have to scrap the required data which in this case is review same inspect the page get the desired div and class and return it"""

# review_box = product_html.find_all("div",{"class" : "_16PBlm"})
# # print(prod_box)
# """Getting name and its comment"""
# name = review_box[0].div.div.find_all("p",{"class": "_2sc7ZR _2V5EHH"})[0].text
# print(name)
# comment = review_box[0].div.div.div.p
# print(comment.text)
# print(" ")

# """Getting name and particular review"""
# for i in review_box:
#     print(i.div.div.find_all("p",{"class": "_2sc7ZR _2V5EHH"})[0].text )
#     print((i.div.div.div.p).text)
#     print(" ")
    

    
yt_url = 'https://www.youtube.com/watch?v=' + 'hUSYT183EB8'
url_yt = urlopen(yt_url)
# print(url_yt)
url_html = url_yt.read()
# print(url_html)
clean_html = bs(url_html,'html.parser')
print(clean_html)
bigbox = clean_html.find_all('div',{'class':'class="style-scope ytd-expander"'})
print(len(bigbox))