# Este es el primer paso configurara las dependencias de como se va a 
#comportar la base de dartos de como se genere el proseso de datos y despues 
#se cierre
from typing import Generator
from app.db.session import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()