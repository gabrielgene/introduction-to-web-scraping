from utils import create_browser, save_data, diff_price
from twitter import notify_on_twitter


def browser_crawler(product_url):
    # Cria o navegador
    browser = create_browser()

    # Acessa a pagina do produto
    browser.get(product_url)

    # Pega o texto do titulo
    title = browser.find_element_by_css_selector(".js-header-product h1").text

    # Pega o preço pelo atrivuto content
    price = browser.find_element_by_css_selector(
        ".price-template-price-block meta[itemprop='price']"
    ).get_attribute("content")

    # Fecha o navegador
    browser.close()

    # Cria um objeto com o titulo e o preço
    data = {}
    data["title"] = title
    data["price"] = float(price)
    print(data)

    # Verifica se o preço novo é menor do que o antigo
    should_notify = diff_price(data["price"])

    # Salva o preço atual em arquivo
    save_data(data)

    # Se deve notificar notificamos no twitter
    if should_notify:
       notify_on_twitter("Seu produto {} está custando R${}".format(title, price))
