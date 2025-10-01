from .init import curs
from model.explorer import Explorer

curs.execute(
    """CREATE TABLE IF NOT EXISTS explorer (
       name TEXT PRIMARY KEY,
       country TEXT,
       description TEXT
    )"""
)

def row_to_model(row: tuple) -> Explorer:
    return Explorer(name=row[0], country=row[1], description=row[2])

def model_to_dict(explorer: Explorer) -> dict:
    return explorer.dict() if explorer else None

def get_one(name: str) -> Explorer | None:
    qry = "SELECT * FROM explorer WHERE name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row) if row else None

def get_all() -> list[Explorer]:
    qry = "SELECT * FROM explorer"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(explorer: Explorer) -> Explorer:
    qry = """INSERT INTO explorer (name, country, description)
             VALUES (:name, :country, :description)"""
    params = model_to_dict(explorer)
    _ = curs.execute(qry, params)
    return get_one(explorer.name)

def modify(name_orig: str, explorer: Explorer) -> Explorer | None:
    qry = """UPDATE explorer
             SET country=:country,
                 name=:name,
                 description=:description
             WHERE name=:name_orig"""
    params = model_to_dict(explorer)
    params["name_orig"] = name_orig
    _ = curs.execute(qry, params)
    return get_one(explorer.name)

def delete(explorer: Explorer) -> bool:
    qry = "DELETE FROM explorer WHERE name=:name"
    params = {"name": explorer.name}
    res = curs.execute(qry, params)
    return curs.rowcount > 0