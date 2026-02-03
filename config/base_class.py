from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from config.appium_server import AppiumServer
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

class BaseClass:

    driver = None
    options = None
    actions = None
    wait = None
    service = None
    
    def launch_app(self):
        """Launches the app using Appium"""
        try:
            server = AppiumServer()
            server.start()
            options = UiAutomator2Options()
            options.set_capability("uiautomator2ServerLaunchTimeout", 60000)  # 60 seconds
            options.device_name = "emulator-5554"
            options.set_capability("autoGrantPermissions", True)
            options.app_package = "com.mykhailovdovchenko.to_dolist"

            driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
            wait = WebDriverWait(driver, 30)
            actions = ActionChains(driver)
            print("Appium Driver, Wait, and Actions initialized successfully.")

            BaseClass.driver = driver
            BaseClass.options = options
            BaseClass.wait = wait
            BaseClass.actions = actions

        except Exception as e:
            print("Failed to launch the app")
            print(str(e))

    def close_app(self):
        """Closes the app and stops the Appium server"""
        try:
            server = AppiumServer()
            if self.driver:
                self.driver.quit() 
                server.stop()
        except Exception as e:
            print("Failed to close the app")
            print(str(e))