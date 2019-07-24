import requests
from bs4 import BeautifulSoup
import smtplib
import time

#Entering url for price tag on the website
URL = 'https://www.amazon.in/dp/B07QT54G6P?pf_rd_p=28cb3a23-65f5-4415-93d4-468016400904&pf_rd_r=2ZX1JZ601FP43NCFG1GV'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id = 'priceblock_ourprice').get_text()
    c_price = price[2:7]
    c_price = c_price.replace(',','')
    c_price = float(c_price)
    
    if c_price < 8000 :
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('surajsharma_bt2k16@dtu.ac.in','wsziebloacgxnufi')
    
    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/dp/B07QT54G6P?pf_rd_p=28cb3a23-65f5-4415-93d4-468016400904&pf_rd_r=2ZX1JZ601FP43NCFG1GV'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
            'srj4158@yahoo.com',
            'sanjanapcm11th@gmail.com',
            msg
            )
    print("HEY EMAIL HAS BEEN SENT")
    server.quit()
    

while(True):
    check_price()
    time.sleep(3600)


