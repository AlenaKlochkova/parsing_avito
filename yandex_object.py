from driver_object import Driver_Object
import constants


class Yandex_Object(Driver_Object):

    def search(self, input):

        '''Загружает сайт Яндекс, подтверждает загрузку поисковой строки, вводит запрос,
        нажимает ENTER'''

        self.driver.get('https://yandex.ru/')
        self.loading(constants.yandex_find)
        self.search_bar_input(constants.yandex_search_bar, constants.yandex_suggest, input)

    def result_selection(self):

        """В списке результатов переходит по первой ссылке,
        переходит на новую вкладку"""

        self.loading(constants.login_button)
        self.driver.find_element(*constants.avito_link).click()
        self.new_tab()







