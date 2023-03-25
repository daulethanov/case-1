from enum import Enum


class Street(Enum):
    bacinskaya = 'ул. Бакинская'
    bytovaya = 'ул.Бытовая'
    vostochnaya = 'ул.Восточная'
    gapeeva = 'ул.Гапеева'


class Dom(Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10


class ActJob(Enum):
    pending = 'В ожидании'
    start = 'В работе'
    finish = 'Выполнено'
