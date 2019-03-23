from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

def save_data(data):
    # Salva os dados em arquivo
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)

def diff_price(actual_price):
    # Carrega os dados atuais
    with open('data.json') as f:
        data = json.load(f)
        # Compara o preço atual com o preço do arquivo
        return actual_price < data["price"]


def create_browser():
    # Define as configuracoes
    chrome_options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.add_argument("--headless")

    # Define o caminho do binario do chromedriver
    chromedriver_path = "./chromedriver"

    # Instancia o navegador
    return webdriver.Chrome(
        chromedriver_path,
        options=chrome_options,
    )