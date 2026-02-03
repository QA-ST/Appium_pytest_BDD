from appium.webdriver.appium_service import AppiumService

class AppiumServer:
    def __init__(self):
        self.service = AppiumService()

    def start(self):
        self.service.start(
            args=['--address', '127.0.0.1', '--port', '4723'],
            timeout_ms=20000
        )
        assert self.service.is_running

    def stop(self):
        if self.service.is_running:
            self.service.stop()
