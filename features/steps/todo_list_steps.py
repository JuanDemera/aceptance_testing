from behave import given, when, then

todo_list = {}

def add_task(title):
    todo_list[title] = {'completed': False}

def mark_task_completed(title):
    if title in todo_list:
        todo_list[title]['completed'] = True
        return True
    return False

def update_task_title(old_title, new_title):
    if old_title in todo_list:
        todo_list[new_title] = todo_list.pop(old_title)
        return True
    return False

def clear_tasks():
    todo_list.clear()

def list_tasks():
    return list(todo_list.keys())

@given('I have a new to-do list')
def step_given_new_todo_list(context):
    todo_list.clear()

@given('I have a to-do list with tasks')
def step_given_todo_list_with_tasks(context):
    todo_list.clear()
    add_task("Buy groceries")
    add_task("Clean the house")

@given('I have a task "{title}" in the to-do list')
def step_given_task_in_todo_list(context, title):
    add_task(title)

@given('I have tasks in the to-do list')
def step_given_tasks_in_todo_list(context):
    add_task("Buy groceries")
    add_task("Clean the house")

@when('I add a task with title "{title}"')
def step_when_add_task(context, title):
    add_task(title)

@when('I list the tasks')
def step_when_list_tasks(context):
    context.task_list = list_tasks()

@when('I mark the task "{title}" as completed')
def step_when_mark_task_completed(context, title):
    context.result = mark_task_completed(title)

@when('I clear the to-do list')
def step_when_clear_todo_list(context):
    clear_tasks()

@when('I update the task "{old_title}" title to "{new_title}"')
def step_when_update_task_title(context, old_title, new_title):
    context.result = update_task_title(old_title, new_title)

@when('I try to mark a non-existent task as completed')
def step_when_mark_nonexistent_task(context):
    context.result = mark_task_completed("Non-existent task")

@then('the task "{title}" should be in the to-do list')
def step_then_task_in_todo_list(context, title):
    assert title in todo_list, f"Task '{title}' not found in the to-do list"

@then('the task "{title}" should be marked as completed')
def step_then_task_marked_completed(context, title):
    assert todo_list.get(title, {}).get('completed', False), f"Task '{title}' is not marked as completed"

@then('the to-do list should be empty')
def step_then_todo_list_empty(context):
    assert not todo_list, "The to-do list is not empty"

@then('I should see "{title}"')
def step_then_see_task(context, title):
    assert title in context.task_list, f"Task '{title}' not found in listed tasks"

@then('I should see an error message "Task not found"')
def step_then_error_message(context):
    assert not context.result, "Expected an error message but task was marked completed"
