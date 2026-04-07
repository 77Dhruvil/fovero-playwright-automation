class BasePage:

    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def wait(self, selector):
        self.page.locator(selector).wait_for(state="visible")