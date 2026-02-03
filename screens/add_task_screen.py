import allure
from config.base_class import BaseClass
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

class AddTaskScreen(BaseClass):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.add_new_task_button = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/fab")
        self.task_name_field = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/et_name")
        self.select_folder_button = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/btn_folder")
        self.work_folder = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Work")')
        self.high_priority_button = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/btn_high")
        self.select_date_button = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/btn_date")
        self.date_ok_button = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/ok")
        self.select_time_button = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/btn_time")
        self.time_ok_button = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/ok")
        self.reminder_toggle_button = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/switch_remind")
        self.repeat_toggle_button = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/switch_repeat")
        self.comment_field = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/et_comments")
        self.done_icon = (AppiumBy.ACCESSIBILITY_ID, "Done")
        self.sub_task_field = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/et_subtask")
        self.add_sub_task_button = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/ib_subtask")
        self.sub_task_completed_checkbox = (AppiumBy.ID, "com.mykhailovdovchenko.to_dolist:id/cb_subtask")

    def click_on_add_new_task(self):
        with allure.step("Clicked Add New Task Icon"):
            self.wait.until(EC.visibility_of_element_located(self.add_new_task_button)).click()

    def enter_task_name(self, task_name):
        with allure.step(f"Entered Task name: {task_name}"):
            self.wait.until(EC.visibility_of_element_located(self.task_name_field)).send_keys(task_name)

    def select_folder(self):
        with allure.step("Selected Folder: Work"):  
            self.wait.until(EC.visibility_of_element_located(self.select_folder_button)).click()
            self.wait.until(EC.visibility_of_element_located(self.work_folder)).click()
       
    def select_priority(self):
        with allure.step("Selected Priority: High"):
            self.wait.until(EC.visibility_of_element_located(self.high_priority_button)).click()

    def select_date_and_time(self, date):
        # Select date
        self.wait.until(EC.visibility_of_element_located(self.select_date_button)).click()
        self.wait.until(
            EC.visibility_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{date}")')
            )
        ).click()
        with allure.step(f"Selected Date: {date}"):
            self.wait.until(EC.visibility_of_element_located(self.date_ok_button)).click()

        # Select time
        self.wait.until(EC.visibility_of_element_located(self.select_time_button)).click()
        self.wait.until(EC.visibility_of_element_located(self.time_ok_button)).click()

    def enable_reminder_and_repeat(self):
        with allure.step("Enabled Reminder and Repeat"):
            self.wait.until(EC.visibility_of_element_located(self.reminder_toggle_button)).click()
            self.wait.until(EC.visibility_of_element_located(self.repeat_toggle_button)).click()

    def enter_comment(self, comment):
        with allure.step(f"Entered comment: {comment}"):
            self.wait.until(EC.visibility_of_element_located(self.comment_field)).send_keys(comment)

    def add_sub_task(self, sub_task):
        with allure.step(f"Added sub task: {sub_task}"):
            self.wait.until(EC.visibility_of_element_located(self.sub_task_field)).send_keys(sub_task)
            self.wait.until(EC.visibility_of_element_located(self.add_sub_task_button)).click()

    def click_on_done(self):
        with allure.step("Clicked on Done button"):
            self.wait.until(EC.visibility_of_element_located(self.done_icon)).click()

    def mark_as_completed_sub_task(self):
        with allure.step("Marked sub task as completed"):
            self.wait.until(EC.visibility_of_element_located(self.sub_task_completed_checkbox)).click()
