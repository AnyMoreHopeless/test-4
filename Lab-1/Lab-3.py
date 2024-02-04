class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        return f'PaperBook - {self.name} by {self.author}'

    def __repr__(self):
        return f'PaperBook(name={self.name}, author={self.author}, pages={self.pages})'


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = value

    def __str__(self):
        return f'AudioBook - {self.name} by {self.author}'

    def __repr__(self):
        return f'AudioBook(name={self.name}, author={self.author}, duration={self.duration})'