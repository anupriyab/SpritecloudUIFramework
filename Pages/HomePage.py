from Pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def clickon_DynamicId(self):
        """
        clicks on Dynamic ID Link
        """
        self.click("Homepage_DynamicIDLink_Xpath")

    def clickon_SampleApp(self):
        """
        clicks on SampleApp Link
        """
        self.click("HomePage_SampleAppLink_Xpath")

    def navigateBackToHomePage(self):
        """
        Navigate Back to Homepage
        """
        self.driver.back()

    def clickon_AjaxLink(self):
        """
        clicks on Ajax Link
        """
        self.click("HomePage_AjaxLink_Xpath")
