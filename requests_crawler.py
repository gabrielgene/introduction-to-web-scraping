import requests
from bs4 import BeautifulSoup
from utils import save_data, diff_price
import json
from twitter import notify_on_twitter

def requests_crawler(product_url):
    # Accesar a pagina do produto
    response = requests.get(product_url)

    # Faz com que o texto seja navegavel por seletores
    soup = BeautifulSoup(response.content, "html.parser")

    # Procura titulo do produto pelo seletor e extrai o texto
    title = soup.select(".js-header-product h1")[0].text

    # Procura o preço do produto e extrai o valor do atributo content
    price = soup.select(".price-template-price-block meta[itemprop='price']")[0]["content"]

    # Cria um objeto com o titulo e o preço
    data = {}
    data["title"] = title
    data["price"] = float(price)

    # Verifica se o preço novo é menor do que o antigo
    should_notify = diff_price(data["price"])

    # Salva o preço atual em arquivo
    save_data(data)

    print(data)

    # Se deve notificar notificamos no twitter
#     if should_notify:
    notify_on_twitter("Seu produto {} está custando R${}".format(title, price))
