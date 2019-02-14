import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import time
import datetime


def create_browser():
    chrome_options = Options()
#     chrome_options.add_argument("--headless")

    chromedriver_path = "./chromedriver"

    return webdriver.Chrome(
        chromedriver_path,
        options=chrome_options,
    )

def diff_price(actual_price):
    with open('data.json') as f:
        data = json.load(f)
        return data["price"] >= actual_price

def browser_crawler(product_url):
    browser = create_browser()
    browser.get(product_url)

    title = browser.find_element_by_css_selector(".js-header-product h1").text
    price = browser.find_element_by_css_selector(
        ".price-template-price-block meta[itemprop='price']"
    ).get_attribute("content")

    browser.close()

    data = {}
    data["title"] = title
    data["price"] = float(price)
    save_data(data)
    notify_on_twitter("Seu produto {} está custando R${}".format(title, price))

def save_data(data):
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)

def requests_crawler(product_url):
    response = requests.get(product_url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.select(".js-header-product h1")[0].text
    price = soup.select(".price-template-price-block meta[itemprop='price']")[0]["content"]

    data = {}
    data["title"] = title
    data["price"] = float(price)
    save_data(data)
    print(diff_price(data["price"]))

    notify_on_twitter("Seu produto {} está custando R${}".format(title, price))

def notify_on_twitter(message):
    browser = create_browser()

    browser.get('https://twitter.com/login')

    user = 'BNotificator'
    login_input = browser.find_element_by_css_selector('input.js-username-field')
    login_input.click()
    login_input.send_keys(user)

    time.sleep(1)

    password = 'campusworkshop'
    pass_input = browser.find_element_by_css_selector('input.js-password-field')
    pass_input.click()
    pass_input.send_keys(password)

    browser.find_element_by_css_selector('button.submit').click()

    profile_url = 'https://twitter.com/gabrielgene_'

    browser.get(profile_url)

    browser.find_element_by_css_selector('button.NewTweetButton').click()
    time.sleep(1)

    text_area = browser.find_element_by_css_selector('div#tweet-box-global')
    text_area.click()

    now = datetime.datetime.now()
    hour = now.strftime("%Y-%m-%d %H:%M:%S")
    text_area.send_keys("{} - {}".format(message, hour))

    browser.find_element_by_css_selector('div.TweetBoxToolbar > div.TweetBoxToolbar-tweetButton.tweet-button > button').click()


    time.sleep(3)

    browser.close()


start_time = time.time()
product_url = "https://www.magazineluiza.com.br/controle-para-ps4-sem-fio-dualshock-4-sony-preto/p/043179500/ga/cops/"
browser_crawler(product_url)
# requests_crawler(product_url)
print("--- %s seconds ---" % (time.time() - start_time))
