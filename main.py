from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time

start_time = time.time()

url = "https://www.magazineluiza.com.br/controle-para-ps4-sem-fio-dualshock-4-sony-preto/p/043179500/ga/cops/"

seletor_nome = "div.header-product > h1"
seletor_preco = ".price-template-price-block meta[itemprop='price']"

response = requests.get(url).content

soup = BeautifulSoup(response, "html.parser")

# nome = soup.select(seletor_nome)[0].click()
# print(nome)

preco = soup.select(seletor_preco)[0]["content"]
print(preco)

print("--- %s seconds ---" % (time.time() - start_time))

chrome_options = Options()
chromedriver_path = "./chromedriver"

navegador = webdriver.Chrome(chromedriver_path, options=chrome_options)

navegador.get(url)
navegador_nome = navegador.find_element_by_css_selector("body > div.wrapper__main > div.wrapper__content.js-wrapper-content > div.wrapper__control > div.wrapper-product__content.wrapper-product__box-prime > div.wrapper-product__informations.js-block-product > button.button__buy.button__buy-product-detail.js-add-cart-button.js-main-add-cart-button.js-add-box-prime").click()


print(navegador_nome)

navegador_preco = navegador.find_element_by_css_selector(seletor_preco).get_attribute("content")


print(navegador_preco)

print("--- %s seconds ---" % (time.time() - start_time))