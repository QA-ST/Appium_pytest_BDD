from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from config.base_class import BaseClass
from screens.add_task_screen import AddTaskScreen
from screens.home_screen import HomeScreen
from pytest_bdd import scenarios, given, when, then, parsers
import pytest

scenarios("./featurefiles/ManageTodotasks.feature")

# Fixtures for driver and screen objects
@pytest.fixture(scope="module")
def app_context():
    base = BaseClass()
    base.launch_app()
    wait = BaseClass.wait
    actions = BaseClass.actions
    driver = BaseClass.driver
    home_screen = HomeScreen(driver)
    add_task_screen = AddTaskScreen(driver)
    yield {
        "base": base,
        "wait": wait,
        "actions": actions,
        "driver": driver,
        "home_screen": home_screen,
        "add_task_screen": add_task_screen
    }
    base.close_app()

@given("I launch the app")
def step_launch_app(app_context):
    pass  # App is launched in fixture

@when("I add a new task with name \"Test Task\" and select folder as Work")
def step_add_todo_task_name_and_folder(app_context):
    wait = app_context["wait"]
    actions = app_context["actions"]
    home_screen = app_context["home_screen"]
    add_task_screen = app_context["add_task_screen"]

    element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//android.widget.Button[@resource-id='android:id/button2']"))
    )
    actions.move_to_element(element).click().perform()
    # Validate without task screen
    no_task_message = home_screen.get_nothing_todo_message()
    print(no_task_message)
    # Add task
    add_task_screen.click_on_add_new_task()
    add_task_screen.enter_task_name("Test Task")
    add_task_screen.select_folder()

@when("Select priority, date, reminder, comment, and subtask")
def step_add_todo_task_required_details(app_context):
    home_screen = app_context["home_screen"]
    add_task_screen = app_context["add_task_screen"]
    add_task_screen.select_priority()
    add_task_screen.select_date_and_time("06 February 2026")
    add_task_screen.enable_reminder_and_repeat()
    add_task_screen.enter_comment("Test automation comment")
    add_task_screen.add_sub_task("Sub task 1")
    add_task_screen.click_on_done()

@then("The task should should be added in the Work Folder")
def step_verify_added_task(app_context):
    home_screen = app_context["home_screen"]
    task_title = home_screen.get_created_task_title()
    assert task_title == "Test Task"

@given("I have a task")
def given_step_bypass_1(app_context):
    pass 

@when("I edit the task name to \"Test Task Edit\"")
def step_edit_created_task_name(app_context):
    home_screen = app_context["home_screen"]
    add_task_screen = app_context["add_task_screen"]
    home_screen.select_task_for_edit()
    add_task_screen.enter_task_name("Test Task Edit")

@when("I change the date to \"07 February 2026\", and update the comment and subtask")
def step_edit_created_task_required_details(app_context):
    home_screen = app_context["home_screen"]
    add_task_screen = app_context["add_task_screen"]
    add_task_screen.select_date_and_time("07 February 2026")
    add_task_screen.enter_comment("Test automation comment edited")
    add_task_screen.mark_as_completed_sub_task()
    add_task_screen.click_on_done()

@then("The task should be updated with assigned date")
def step_edit_created_task_required_details(app_context):
    home_screen = app_context["home_screen"]
    home_screen.select_folder("Work")
    task_title = home_screen.get_created_task_title()
    task_date = home_screen.get_created_task_date_and_time()
    assert "Test Task Edit" in task_title and "Feb 7" in task_date

@given("I have a task")
def given_step_bypass_2(app_context):
    pass 

@when("I mark the task as completed")
def step_mark_completed_created_task(app_context):
    home_screen = app_context["home_screen"]
    home_screen.mark_as_completed_task()

@then("The task should mark as completed and move to \"Done\" folder")
def step_verify_marked_completed(app_context):
    home_screen = app_context["home_screen"]
    home_screen.select_folder("Done")
    is_selected = home_screen.mark_as_completed_task_validation()
    assert is_selected

@given("I have Task Available in Done folder")
def given_step_bypass_3(app_context):
    pass 

@when("I delete the task")
def step_delete_created_task(app_context):
    home_screen = app_context["home_screen"]
    home_screen.delete_task()

@then("The task should deleted in the \"All Folders\" folder")
def step_verify_task(app_context):
    home_screen = app_context["home_screen"]
    home_screen.select_folder("All Folders")
    no_task_message = home_screen.get_nothing_todo_message()
    assert "Nothing to do…" in no_task_message