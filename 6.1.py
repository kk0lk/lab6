"""

Задача №1

За допомогою бібліотеки tkinter створити тест на будь-яку тему
на 6 або більше питань, використовуючи різні типи віджетів
(перемикачі, прапорці, спадне меню, поле введення, шкала тощо).

Виконала: Гриб Наталія Григорівна, 31І група

"""

from tkinter import*
from tkinter import messagebox

class ComputerScienceTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Інформатика - Тест")
        self.root.geometry("400x300")

        self.questions = [
            "1. Що таке HTML?",
            "2. Яка мова програмування використовується для написання веб-скриптів?",
            "3. Що таке GUI?",
            "4. Що означає абревіатура 'URL'?",
            "5. Яка операційна система є відкритою та безкоштовною?",
            "6. Яка структура данних використовується для зберігання об'єднаних значень в Python?"
        ]

        self.answers = [
            ["Гіпертекстова мова розмітки", "Глобальна мова технічного вираження", "Гаряча тастируюча мова літературного типу"],
            ["Java", "Python", "C++"],
            ["Графічний інтерфейс користувача", "Глобальний інтернет-універсум", "Гнучкий інтерактивний інтерфейс"],
            ["Uniform Resource Locator", "Universal Resource Locator", "Uniform Retrieval Locator"],
            ["Windows", "Linux", "Mac OS"],
            ["Список", "Кортеж", "Словник"]
        ]

        self.correct_answers = [0, 1, 0, 0, 1, 1]

        self.current_question = 0
        self.user_answers = []

        self.create_widgets()

    def create_widgets(self):
        self.question_label = Label(self.root, text=self.questions[self.current_question], wraplength=350, justify=LEFT)
        self.question_label.pack(pady=10)

        self.answer_var = StringVar()
        for i, answer in enumerate(self.answers[self.current_question]):
            Radiobutton(self.root, text=answer, variable=self.answer_var, value=i).pack(anchor=W)

        self.next_button = Button(self.root, text="Наступне", command=self.next_question)
        self.next_button.pack(pady=10)

    def next_question(self):
        user_answer = self.answer_var.get()
        if user_answer == "":
            messagebox.showwarning("Увага", "Будь ласка, оберіть відповідь.")
        else:
            self.user_answers.append(int(user_answer))
            self.answer_var.set("")  # Скидає вибір радіокнопок
            self.current_question += 1

            if self.current_question < len(self.questions):
                self.update_question()
            else:
                self.show_results()

    def update_question(self):
        self.question_label.config(text=self.questions[self.current_question])

        # Очищення попередніх радіокнопок
        for widget in self.root.winfo_children():
            if isinstance(widget, Radiobutton):
                widget.destroy()

        # Створення нових радіокнопок для нового питання
        for i, answer in enumerate(self.answers[self.current_question]):
            Radiobutton(self.root, text=answer, variable=self.answer_var, value=i).pack(anchor=W)

    def show_results(self):
        score = sum([1 for i in range(len(self.correct_answers)) if self.user_answers[i] == self.correct_answers[i]])
        messagebox.showinfo("Результат", f"Ваш результат: {score} / {len(self.questions)}")

if __name__ == "__main__":
    root = Tk()
    app = ComputerScienceTest(root)
    root.mainloop()

