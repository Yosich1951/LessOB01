"""
Менеджер задач

Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
У задачи должны быть атрибуты: описание задачи, срок выполнения и
статус (выполнено/не выполнено).
Реализуй функцию для добавления задач,
отметки выполненных задач и
вывода списка текущих (не выполненных) задач.
"""


class Task:
    # Инициализация класса с заданными атрибутами
    def __init__(self, description, deadline, status=False):
        self.description = description  # Описание задачи
        self.deadline = deadline  # Срок выполнения
        self.status = status  # Статус выполнения (True - выполнено, False - не выполнено)


class TaskManager:
    def __init__(self):
        self.tasks = []  # Список для хранения задач

    # Функция для добавления задачи
    def add_task(self, description, deadline):
        task = Task(description, deadline)  # Создаем экземпляр задачи
        self.tasks.append(task)  # Добавляем задачу в список

    # Функция для отметки задачи как выполненной
    def mark_as_done(self, description):
        # Ищем задачу по описанию и отмечаем ее как выполненную
        for task in self.tasks:
            if task.description == description:
                task.status = True
                print(f"Задача '{description}' выполнена.")
                return
        print(f"Задача с описанием '{description}' не найдена.")

    # Функция для вывода списка текущих задач
    def show_current_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if not task.status:
                print(f"Описание: {task.description}, Срок: {task.deadline}")


# Создаем менеджер задач
task_manager = TaskManager()

# Добавление задач
task_manager.add_task("Купить молоко", "2023-04-05")
task_manager.add_task("Отправить письмо", "2023-04-10")

# Вывод текущих задач
task_manager.show_current_tasks()

# Отмечаем задачу "Купить молоко" как выполненную
task_manager.mark_as_done("Купить молоко")

# Повторный вывод текущих задач для проверки
task_manager.show_current_tasks()
