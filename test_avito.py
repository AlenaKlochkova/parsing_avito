import pytest
from selenium import webdriver
from yandex_object import Yandex_Object
from avito_object import Avito_Object
import constants

@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_one(browser):
    yandex = Yandex_Object(browser)
    yandex.search('avito')
    yandex.result_selection()

def test_two(browser):
    avito = Avito_Object(browser)
    avito.go_to(constants.avito_site)
    avito.set_city('Рыбинск')
    avito.option(constants.estate)
    avito.option(constants.estate_new)
    avito.list_processing(constants.flats_list, avito.flat_profile, ceil=5)









