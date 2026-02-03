Feature: Add and manage Todo tasks

  As a user, I want to be able to add, edit, mark as completed, and delete tasks, so that I can manage my to-do list efficiently.

  Scenario: Add a new Todo task successfully
    Given I launch the app
    When I add a new task with name "Test Task" and select folder as Work
    And Select priority, date, reminder, comment, and subtask
    Then The task should should be added in the Work Folder

  Scenario: Edit Created Task
    Given I have a task
    When I edit the task name to "Test Task Edit"
    And I change the date to "07 February 2026", and update the comment and subtask
    Then The task should be updated with assigned date

  Scenario: Mark Task as Completed
    Given I have a task
    When I mark the task as completed
    Then The task should mark as completed and move to "Done" folder

  Scenario: Deleted Created Task
    Given I have Task Available in Done folder
    When I delete the task
    Then The task should deleted in the "All Folders" folder
  