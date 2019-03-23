import time
import datetime
from utils import create_browser

def notify_on_twitter(message):
    # Cria o navegador
    browser = create_browser()

    # Acessa a pagina de login do twitter
    browser.get('https://twitter.com/login')

    # Procura o campo de usuario, clica e digita o nome do usuario
    user = 'BNotificator'
    login_input = browser.find_element_by_css_selector('input.js-username-field')
    login_input.click()
    login_input.send_keys(user)

    time.sleep(1)

    # Procura o campo de senha, clica e digita o nome do senha
    password = 'campusworkshop'
    pass_input = browser.find_element_by_css_selector('input.js-password-field')
    pass_input.click()
    pass_input.send_keys(password)

    # Clica em login
    browser.find_element_by_css_selector('button.submit').click()

    # Acessa o meu perfil
    profile_url = 'https://twitter.com/gabrielgene_'
    browser.get(profile_url)

    # Clica em twittar pra mim
    browser.find_element_by_css_selector('button.NewTweetButton').click()
    time.sleep(1)

    # Procura o campo de texto e digita a mensagem de notificacao
    text_area = browser.find_element_by_css_selector('div#tweet-box-global')
    text_area.click()
    now = datetime.datetime.now()
    hour = now.strftime("%Y-%m-%d %H:%M:%S")
    text_area.send_keys("{} - {}".format(message, hour))

    # Clica no botão de twittar
    browser.find_element_by_css_selector('div.TweetBoxToolbar > div.TweetBoxToolbar-tweetButton.tweet-button > button').click()

    time.sleep(3)

    browser.close()