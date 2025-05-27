# 🎓 UniverCity – Plataforma Virtual Educativa con FastAPI

**UniverCity** es una plataforma educativa universitaria desarrollada con **FastAPI**, diseñada para gestionar carreras, semestres, notas y usuarios con distintos roles.  
El sistema permite registrar estudiantes, docentes y administradores, asociarlos a programas académicos, registrar notas por semestre y aplicar reglas de seguridad con JWT y control de permisos por rol.

---

## 🚀 Tecnologías utilizadas

- **FastAPI** – Framework web moderno y asíncrono.
- **SQLAlchemy** – ORM para modelado de datos relacional.
- **Alembic** – Gestión de migraciones de base de datos.
- **PostgreSQL** – Motor de base de datos.
- **Pydantic** – Validación y serialización de datos.
- **JWT (JSON Web Tokens)** – Autenticación basada en tokens.
- **Bcrypt** – Hashing seguro de contraseñas.

---


---

## 👤 Roles de usuario

- **Admin**: Crea y gestiona usuarios, programas, semestres, notas.
- **Docente**: Consulta y registra calificaciones de estudiantes asignados.
- **Estudiante**: Consulta su programa, semestres y calificaciones.

---

## ✅ Funcionalidades implementadas

- [x] Autenticación con JWT.
- [x] Encriptación segura de contraseñas (Bcrypt).
- [x] Validación de roles (`admin`, `teacher`, `student`).
- [x] CRUD completo para usuarios.
- [x] CRUD para `Programa` (carreras universitarias).
- [x] CRUD para `Semestre`, vinculado a programas.
- [x] CRUD para `Nota`, asociada a semestres y usuarios.
- [x] Asociación de estudiantes a programas.
- [x] Asociación de docentes a programas y semestres (estructura inicial).
- [x] Protección de rutas según rol.
- [x] Migraciones con Alembic y PostgreSQL.



## 🔐 Seguridad

- Autenticación con JWT.
- Protección de endpoints por roles.
- Validación estricta con Pydantic.
- Hashing de contraseñas con Bcrypt.
- Manejo de errores y respuestas personalizadas.

---

## 🧪 Instalación y ejecución local

### 1. Clonar el repositorio

```bash
git clone https://github.com/AndresDev-20/UniverCity__Backend.git
cd UniverCity__Backend


2. Crea el entorno virtual e instálalo:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

3. Configura la conexión a PostgreSQL en `.env` o en `config.py`.
```
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/univercity_db
SECRET_KEY=tu_clave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
4. Ejecuta las migraciones:

```bash
alembic revision --autogenerate -m "mensaje_de_migracion"
alembic upgrade head
```

5. Corre la aplicación:

```bash
uvicorn app.main:app --reload
```

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.  
¡Eres libre de usarlo, modificarlo y adaptarlo!

## ✍️ Autor

**Yeison Andrés Marroquín Bernal**  
Full Stack Developer
🔗 [LinkedIn](https://www.linkedin.com/in/yeison-andres-marroqu%C3%ADn-bernal-008138266/) | 🐙 [GitHub](https://github.com/AndresDev-20)
