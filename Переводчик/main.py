from tkinter import *
from googletrans import Translator

def translate_text():
    loading_label.config(text="Переводит...")
    root.update()
    try:
        text = text_input.get('1.0', END).strip()
        translator = Translator()
        if is_russian(text):
            translated_text = translator.translate(text, dest='en').text
        else:
            translated_text = translator.translate(text, dest='ru').text

        text_output.delete('1.0', END)
        text_output.insert('1.0', translated_text)
        loading_label.config(text="Перевод завершен")
    except Exception as e:
        print("Ошибка перевода:", e)

def is_russian(text):
    return any(ord('а') <= ord(char) <= ord('я') or ord('А') <= ord(char) <= ord('Я') for char in text)

root = Tk()
root.geometry('350x450')
root.title('Переводчик')
root.resizable(width=False, height=False)
root.configure(bg='#2C3E50')

label_input = Label(root, fg='#ECF0F1', bg='#2C3E50', font=('Arial', 15), text='Введите текст:')
label_input.grid(row=0, column=0, padx=10, pady=10, sticky="w")

text_input = Text(root, width=35, height=5, font=('Arial', 12))
text_input.grid(row=1, column=0, padx=10, pady=10)

translate_button = Button(root, width=10, bg='#1ABC9C', fg='white', font=('Arial', 10, 'bold'), text='Перевести', command=translate_text)
translate_button.grid(row=2, column=0, pady=10)

label_output = Label(root, fg='#ECF0F1', bg='#2C3E50', font=('Arial', 15), text='Результат перевода:')
label_output.grid(row=3, column=0, padx=10, pady=10, sticky="w")

text_output = Text(root, width=35, height=5, font=('Arial', 12))
text_output.grid(row=4, column=0, padx=10, pady=10)


loading_label = Label(root, fg='#ECF0F1', bg='#2C3E50', font=('Arial', 15))
loading_label.grid(row=5, column=0, pady=10)

root.mainloop()
