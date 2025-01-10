import uuid
from datetime import datetime


class Task:
    def __init__(self, title, description='', due_date=None):
        self.id = str(uuid.uuid4())  
        self.title = title
        self.description = description
        self.due_date = due_date if due_date else None
        self.completed = False
        self.created_at = datetime.now()

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{self.id}] {self.title} - {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []
        print("ToDo list created!")  

    def add_task(self, task: Task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added!")  

    def list_tasks(self):
        print("Listing tasks:")
        for task in self.tasks:
            print(task)  
        return [str(task) for task in self.tasks]

    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()
                print(f"Task '{task.title}' marked as completed!")  

    def clear_all_tasks(self):
        self.tasks.clear()
        print("All tasks cleared!")  


if __name__ == "__main__":
    # Crear una lista de tareas
    todo_list = ToDoList()

    # Añadir tareas
    task1 = Task("Buy groceries")
    todo_list.add_task(task1)

    task2 = Task("Finish homework")
    todo_list.add_task(task2)

    # Listar las tareas
    todo_list.list_tasks()

    # Marcar una tarea como completada
    todo_list.mark_task_completed(task1.id)

    # Listar las tareas nuevamente para ver el cambio
    todo_list.list_tasks()

    # Limpiar todas las tareas
    todo_list.clear_all_tasks()

    # Ver que la lista está vacía
    todo_list.list_tasks()
