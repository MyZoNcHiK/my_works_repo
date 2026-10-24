class Task:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Завдання: {self.name}")


class Executor:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def show_info(self):
        print(f"Виконавець: {self.first_name} {self.last_name}")


class Project:
    def __init__(self, name, tasks_data):
        self.name = name
        self.tasks = []

        for task_name, first_name, last_name in tasks_data:
            task = Task(task_name)
            executor = Executor(first_name, last_name)
            self.tasks.append((task, executor))

    def show_info(self):
        print(f"Проект: {self.name}")

        for i, (task, executor) in enumerate(self.tasks, start=1):
            print(f"\n{i}.")
            task.show_info()
            executor.show_info()

    def add_task(self, task_name, first_name, last_name):
        task = Task(task_name)
        executor = Executor(first_name, last_name)
        self.tasks.append((task, executor))

    def show_tasks_count(self):
        print(f"Кількість завдань: {len(self.tasks)}")


project1 = Project(
    "Створення вебсайту",[
        ("Створення дизайну", "Іван", "Петренко"),
        ("Розробка сайту", "Олена", "Коваленко")
    ]
)

project1.show_info()
project1.show_tasks_count()

project1.add_task("Тестування сайту", "Андрій", "Мельник")

print()
project1.show_info()
project1.show_tasks_count()

