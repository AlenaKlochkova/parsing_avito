from selenium.webdriver.common.by import By

yandex_find = (By.CSS_SELECTOR, 'button.button')
yandex_search_bar = (By.ID, 'text')
yandex_suggest = (By.CLASS_NAME, 'mini-suggest__popup-content')
login_button = (By.CSS_SELECTOR, '.button2_theme_action')
avito_site = 'https://www.avito.ru/'
avito_link = (By.CSS_SELECTOR, 'ul#search-result a')
avito_city_choice = (By.CSS_SELECTOR, 'div.main-select-JJyaZ:nth-child(1)')
city_input = (By.CSS_SELECTOR, '.suggest-input-rORJM')
city_suggest = (By.CLASS_NAME, 'suggest-suggest-content-raQZy')
show_city = (By.CLASS_NAME, 'popup-buttons-WICnh')
estate = (By.CSS_SELECTOR, 'a.link-link-MbQDP:nth-child(2)')
estate_new = (By.CSS_SELECTOR, 'li.rubricator-list-item-item-WKnEv:nth-child(2) > div:nth-child(1) > a:nth-child(1)')
flats_list = (By.CLASS_NAME, 'iva-item-sliderLink-uLz1v')
flat_price = (By.CSS_SELECTOR, '.js-item-price')
flat_image = (By.CSS_SELECTOR, 'div.gallery-img-wrapper:nth-child(1) > div:nth-child(1) > img:nth-child(2)')
flat_size = ((By.CLASS_NAME, 'item-params-list-item'), 1)



