from selenium import webdriver
from yandex_object import Yandex_Object
from avito_object import Avito_Object
import constants


driver = webdriver.Firefox()
yandex = Yandex_Object(driver)
avito = Avito_Object(driver)

yandex.search('avito')
yandex.result_selection()
avito.set_city('Ярославль')
avito.option(constants.estate)
avito.option(constants.estate_new)
avito.open_file('avito_new')
avito.list_processing(constants.flats_list, avito.write_down, avito.flat_profile)
avito.close_file()
avito.back_to_first()
driver.quit()





