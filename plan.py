class LessonPlanner:
    def __init__(self):
        self.lessons = []

    def add_lesson(self):
        subject = input("Предмет: ").strip()
        time = input("Время: ").strip()
        note = input("Заметка (необязательно): ").strip()

        if not subject or not time:
            print("Ошибка: предмет и время обязательны")
            return

        lesson = {
            "subject": subject,
            "time": time,
            "note": note
        }

        self.lessons.append(lesson)
        print("Урок добавлен!\n")

    def show_lessons(self):
        if not self.lessons:
            print("Планер пуст\n")
            return

        print("\n📅 Список уроков:")
        for i, lesson in enumerate(self.lessons):
            print(f"{i + 1}. {lesson['time']} | {lesson['subject']} | {lesson['note']}")
        print()

    def delete_lesson(self):
        self.show_lessons()
        if not self.lessons:
            return

        try:
            index = int(input("Введите номер для удаления: ")) - 1
            if 0 <= index < len(self.lessons):
                removed = self.lessons.pop(index)
                print(f"Удалено: {removed['subject']}\n")
            else:
                print("Неверный номер\n")
        except ValueError:
            print("Введите число\n")

    def run(self):
        while True:
            print("=== Мини-планер ===")
            print("1. Добавить урок")
            print("2. Показать уроки")
            print("3. Удалить урок")
            print("4. Выход")

            choice = input("Выбор: ").strip()

            if choice == "1":
                self.add_lesson()
            elif choice == "2":
                self.show_lessons()
            elif choice == "3":
                self.delete_lesson()
            elif choice == "4":
                print("Выход...")
                break
            else:
                print("Неверный выбор\n")


if __name__ == "__main__":
    app = LessonPlanner()
    app.run()