from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import json


class Driver_Object():

    def __init__(self, driver):
        self.driver = driver

    def go_to(self, link):

        """Переходит по указанной ссылке"""

        self.driver.get(link)

    def loading(self, selector):

        """Ожидание загрузки страницы"""

        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.visibility_of_element_located(selector))

    def new_tab(self):

        """Переход на новую вкладку"""

        self.driver.switch_to.window(self.driver.window_handles[-1])

    def previous_tab(self):

        """Закрывает последнюю открытую вкладку, переходит на предыдущую вкладку"""

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def search_bar_input(self, selector1, selector2, input):

        """Находит поисковую строку, вводит запрос, нажимает ENTER"""

        search = self.driver.find_element(*selector1)
        search.send_keys(input)
        self.loading(selector2)
        search.send_keys(Keys.ENTER)

    def option(self, selector):

        """Ищет элемент и кликает по нему"""

        self.driver.find_element(*selector).click()

    def get_info(self, selector):

        """Возвращает информацию по найденному селектору"""

        if isinstance(selector[1], int) == True:
            item = self.driver.find_elements(*selector[0])[selector[1]]
        else:
            item = self.driver.find_element(*selector)
        return item.text

    def list_processing(self, selector, func, args=None, ceil=None):

        """Получает список элементов с одинаковым селектором, для каждого элемента
        открывает новую вкладку, выполняет действие, закрывает вкладку"""

        list_of_items = self.driver.find_elements(*selector)
        if ceil:
            list_of_items = list_of_items[:ceil+1]
        for item in list_of_items:
            item.click()
            self.new_tab()
            if args:
                func(args())
            else:
                func()
            self.previous_tab()

    def back_to_first(self):

        """Переходит на самую первую страницу"""

        while len(self.driver.window_handles) > 1:
            self.previous_tab()

    def open_file(self, file_name):

        """Открывает файл формата json для записи"""

        global file
        file = open(f'{file_name}.json', 'a', encoding='utf-8')

    def write_down(self, source):

        """Записывает указанные данные в открытый файл"""

        json.dump(source, file, indent=4, ensure_ascii=False)

    def close_file(self):

        """Закрывает открытый на данный момент файл"""

        file.close()
