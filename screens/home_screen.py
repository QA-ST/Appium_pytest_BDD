import allure
from config.base_class import BaseClass
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

class HomeScreen(BaseClass):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.folder_dropdown = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/sp_text")
        self.task_title_text = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/tv_title")
        self.task_date_and_time_text = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/tv_time")
        self.task_delete_button = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/iv_delete")
        self.confirm_delete_ok = (AppiumBy.ID, "android:id/button1")
        self.task_completed_checkbox = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/cb_task")

    def get_nothing_todo_message(self):
        element = self.wait.until(
            EC.visibility_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nothing to do…")')
            )
        )
        return element.text

    def select_folder(self, folder_name):
        with allure.step(f"Selected Folder: {folder_name} from Dropdown"):
            self.wait.until(EC.visibility_of_element_located(self.folder_dropdown)).click()
            self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{folder_name}")')
                )
            ).click()

    def get_selected_folder(self):
        element = self.wait.until(EC.visibility_of_element_located(self.folder_dropdown))
        return element.text

    def get_created_task_title(self):
        element = self.wait.until(EC.visibility_of_element_located(self.task_title_text))
        return element.text

    def get_created_task_date_and_time(self):
        element = self.wait.until(EC.visibility_of_element_located(self.task_date_and_time_text))
        return element.text

    def select_task_for_edit(self):
        with allure.step("Selected created task for edit"):
            self.wait.until(EC.visibility_of_element_located(self.task_title_text)).click()

    def delete_task(self):
        with allure.step("Clicked on Delete icon"):
            self.wait.until(EC.visibility_of_element_located(self.task_delete_button))
            self.wait.until(EC.element_to_be_clickable(self.task_delete_button)).click()
            with allure.step("Confirmed Delete action"):
                self.wait.until(EC.element_to_be_clickable(self.confirm_delete_ok))
                self.wait.until(EC.element_to_be_clickable(self.confirm_delete_ok)).click()
    
    def mark_as_completed_task(self):
        with allure.step("Marked task as completed"):
            self.wait.until(EC.visibility_of_element_located(self.task_completed_checkbox)).click()

    def mark_as_completed_task_validation(self):
        element = self.wait.until(EC.visibility_of_element_located(self.task_delete_button))
        return element.is_displayed()