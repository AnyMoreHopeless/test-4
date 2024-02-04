# Абстрактный класс для описания стола
class Table:
    def __init__(self, material: str, color: str, legs: int):
        # Материал стола
        self.material = material
        # Цвет стола
        self.color = color
        # Количество ножек стола
        self.legs = legs

    def change_color(self, new_color: str) -> None:
        # Метод для изменения цвета стола
        ...

    def add_legs(self, quantity: int) -> None:
        # Метод для добавления ножек столу
        ...

    # Пример использования метода change_color
    def method_1(self):
        """
        Изменяет цвет стола.

        Пример:
        >>> t = Table("wood", "brown", 4)
        >>> t.change_color("white")
        """
        ...


# Абстрактный класс для описания дерева
class Tree:
    def __init__(self, species: str, height: float, age: int):
        # Вид дерева
        self.species = species
        # Высота дерева
        self.height = height
        # Возраст дерева
        self.age = age

    def grow(self, new_height: float) -> None:
        # Метод для увеличения высоты дерева
        ...

    def shed_leaves(self, season: str) -> None:
        # Метод для опадания листьев
        ...

    # Пример использования метода grow
    def method_1(self):
        """
        Увеличивает высоту дерева.

        Пример:
        >>> t = Tree("oak", 5.2, 20)
        >>> t.grow(6.0)
        """
        ...


# Абстрактный класс для описания социальной сети
class SocialNetwork:
    def __init__(self, name: str, users: int, has_advertising: bool):
        # Название социальной сети
        self.name = name
        # Количество пользователей
        self.users = users
        # Наличие рекламы
        self.has_advertising = has_advertising

    def add_user(self, new_user: str) -> None:
        # Метод для добавления нового пользователя
        ...

    def remove_advertising(self) -> None:
        # Метод для удаления рекламы
        ...

    # Пример использования метода add_user
    def method_1(self):
        """
        Добавляет нового пользователя.

        Пример:
        >>> s = SocialNetwork("Facebook", 1000000, True)
        >>> s.add_user("John")
        """
        ...