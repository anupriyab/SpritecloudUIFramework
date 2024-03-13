from Pages.BasePage import BasePage


class DynamicIdPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def clickon_DynamicIdButton(self):
        """
        clicks on Dynamic ID Button
        """
        self.click("DynamicIDPage_Button_Xpath")
        print("Dynamic Id is clicked")
