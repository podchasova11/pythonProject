Class BasePage():

@HandleExcElementsDecorator()
    def current_page_is(self, link):
        print(f"{datetime.now()}   current_page = {self.driver.current_url}")
        print(f"{datetime.now()}   link = {link}")
        return link == self.driver.current_url
