from requests_crawler import requests_crawler
from browser_crawler import browser_crawler
import time

start_time = time.time()

product_url = "https://www.magazineluiza.com.br/controle-para-ps4-sem-fio-dualshock-4-sony-preto/p/043179500/ga/cops/"

browser_crawler(product_url)
# requests_crawler(product_url)

print("--- %s seconds ---" % (time.time() - start_time))