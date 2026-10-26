class Text:
    def __init__(self, content, language, **kwargs):
        super().__init__(**kwargs)
        self.content = content
        self.language = language

    def show_text(self):
        print(f"Зміст тексту: {self.content}")
        print(f"Мова: {self.language}")


class Font:
    def __init__(self, font_name, size, bold, italic, underline, **kwargs):
        super().__init__(**kwargs)
        self.font_name = font_name
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def show_font(self):
        print(f"Назва шрифту: {self.font_name}")
        print(f"Кегль: {self.size}")
        print(f"Напівгрубий: {'Так' if self.bold else 'Ні'}")
        print(f"Нахилений: {'Так' if self.italic else 'Ні'}")
        print(f"Підкреслений: {'Так' if self.underline else 'Ні'}")

class TextLabel(Text, Font):
    def __init__(self, content, language, font_name, size, bold, italic, underline, color):
        super().__init__(content=content, language=language, font_name=font_name, size=size, bold=bold, italic=italic, underline=underline)
        self.color = color

    def show_info(self):
        self.show_text()
        self.show_font()
        print(f"Колір: {self.color}")


label = TextLabel("Ласкаво просимо!", "Українська", "Arial", 16, True, False, True, "Синій")

label.show_info()

