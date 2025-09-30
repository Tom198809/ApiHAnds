from model.creature import Creature

# Фиктивные данные, пока не произойдет замена на реальную базу данных и SQL
_creatures = [
    Creature(
        name="yeti",
        aka="Abominable Snowman",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan"
    ),
    Creature(
        name="Bigfoot",
        description="yeti's Cousin Eddie",
        country="US",
        area="*",
        aka="Sasquatch"
    ),
]

def get_all() -> list[Creature]:
    """Возврат всех существ"""
    return _creatures

def get_one(name: str) -> Creature | None:
    """Возврат одного существа"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

# Приведённые ниже варианты пока не функциональны,
# поэтому они просто делают вид, что работают,
# не изменяя реальный фиктивный список

def create(creature: Creature) -> Creature:
    """Добавление существа"""
    return creature

def modify(creature: Creature) -> Creature:
    """Частичное изменение записи существа"""
    return creature

def replace(creature: Creature) -> Creature:
    """Полная замена записи существа"""
    return creature

def delete(name: str):
    """Удаление записи существа; возврат значения None,
    если запись существовала"""
    return None  # пока не реализовано