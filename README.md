# Appium+pytest-bdd Mobile App Automation Framework

This repository contains an Appium-based automation framework for testing a Todo List Android application. It uses Python, pytest-bdd, and Appium for end-to-end mobile UI automation.


## Features Covered

BDD scenarios implemented in ManageTodotasks.feature:

Add a new Todo task

Add task name, folder, priority, date, reminder, comment, and subtask.

Edit created task

Update task name, date, comment, and subtask.

Mark task as completed

Move task to the "Done" folder.

Delete taskMove task to the "Done" folder.

Delete task and verify it is removed from "All Folders".


## Prerequisites

Visual Studio code

Python 3.9+

Appium 2.x

Android Emulator or Physical Device (configured via ADB)

Node.js & NPM (for Appium server)

venv (Python virtual environment module)

## Setup & Installation

#### Clone the repository:

~~~
git clone https://github.com/QA-ST/Appium_pytest_BDD
cd Appium_pytest_BDD
code .
~~~


#### Create a virtual environment (if not already included):

~~~
python -m venv venv
~~~

#### Activate the virtual environment:

##### Windows:

~~~
venv\Scripts\activate
~~~

##### macOS / Linux:

~~~
source venv/bin/activate
~~~

#### Install dependencies:

~~~
pip install -r requirements.txt
~~~

#### Launch Android Emulator or connect a physical device:

Verify if device connected or not with adb server.

~~~
adb devices
~~~


## Running Tests

### Make Sure the Android Emulator or Physical Device should running and virtual environment should activated

#### Enter command 

~~~
pytest  pytest --bdd-report="TestReport/bddreport.html" --alluredir=allure-results
~~~


### Appium server is automatically started and stopped by BaseClass and AppiumServer.

## View Report

Open bddreport.html in the browser or for viewing Allure report type command:

~~~
allure serve allure-results
~~~


#### Deactivating the Virtual Environment

After finishing, deactivate the venv using:

~~~
deactivate
~~~