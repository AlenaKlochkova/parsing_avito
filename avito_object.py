from driver_object import Driver_Object
import constants


class Avito_Object(Driver_Object):

    def set_city(self, input):

        """Изменяет город"""

        self.loading(constants.avito_city_choice)
        self.option(constants.avito_city_choice)
        self.search_bar_input(constants.city_input, constants.city_suggest, input)
        self.option(constants.show_city)

    def flat_profile(self):

        """Выводит в консоль данные по квартире, возвращает результат"""

        self.loading(constants.flat_image)
        price = f'Цена: {self.get_info(constants.flat_price)}'
        size = f'Площадь: {self.get_info(constants.flat_size)[14:]}'
        link = f'Ссылка: {self.driver.current_url}'
        print(price, size, link)
        return [price, size, link]

