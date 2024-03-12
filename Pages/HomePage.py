from Pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def clickon_DynamicId(self):
        self.click("Homepage_DynamicIDLink_Xpath")

    def clickon_SampleApp(self):
        self.click("HomePage_SampleAppLink_Xpath")
