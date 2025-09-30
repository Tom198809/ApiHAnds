from model.explorer import Explorer

# Фиктивные данные, в главе 10 они будут заменены на реальную базу данных и SQL
_explorers = [
    Explorer(
        name="Claude Hande",
        country="FR",
        description="Scarce during full moons"
    ),
    Explorer(
        name="Noah Weiser",
        country="DE",
        description="Myopic machete man"
    ),
]

def get_all() -> list[Explorer]:
    """Возврат всех исследователей"""
    return _explorers

def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

# Приведенные ниже варианты пока не функциональны,
# поэтому они просто делают вид, что работают,
# не изменяя реальный фиктивный список

def create(explorer: Explorer) -> Explorer:
    """Добавление исследователя"""
    return explorer

def modify(explorer: Explorer) -> Explorer:
    """Частичное изменение записи исследователя"""
    return explorer

def replace(explorer: Explorer) -> Explorer:
    """Полная замена записи исследователя"""
    return explorer

def delete(name: str) -> bool:
    """Удаление записи исследователя; возврат значения None,
    если запись существовала"""
    return None  # пока не реализовано