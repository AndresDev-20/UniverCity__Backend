from app.db.base_class import Base

# Importamos los modelos por separado
from app.models.user import User
from app.models.program import Program
from app.models.semesters import Semester
from app.models.grade import Grade
from app.models.association import teachers_programs