# 🎓 UniverCity – Plataforma Virtual Educativa con FastAPI

**UniverCity** es una plataforma educativa universitaria construida con **FastAPI**, diseñada para gestionar carreras profesionales, semestres y calificaciones, con un robusto sistema de autenticación por roles.  
El sistema permite registrar usuarios (estudiantes, docentes y administradores), asociarlos a programas académicos, manejar semestres, registrar notas finales por semestre, y garantizar seguridad mediante JWT y control de permisos.

## 🚀 Tecnologías utilizadas

- **FastAPI** – Framework web moderno y rápido.
- **SQLAlchemy** – ORM para manejo de modelos y relaciones.
- **Alembic** – Migraciones automáticas de base de datos.
- **PostgreSQL** – Base de datos relacional.
- **Pydantic** – Validación y serialización de datos.
- **JWT (JSON Web Tokens)** – Autenticación y autorización.
- **Bcrypt** – Encriptación segura de contraseñas.

## 🗂️ Estructura del proyecto



```
raíz_del_proyecto/
│
├── .venv/                     # Entorno virtual
├── alembic/                   # Migraciones
│   ├── versions/              # Archivos de migración  
│   └── env.py                 # Configuración y modelos
├── app/
│   ├── main.py                # Punto de entrada de la app
│   ├── models/                # Modelos SQLAlchemy
│   │   ├── task.py
│   │   └── user.py
│   ├── api/
│   │   └── routers/
│   │       └── desp.py        # Rutas de endpoints
│   ├── db/
│   │   ├── base.py
│   │   ├── base_class.py
│   │   └── session.py
│   ├── crud/
│   │   ├── task.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── task.py
│   │   └── user.py
│   └── core/
│       └── config.py          # Configuración del proyecto
├── .gitignore
├── alembic.ini
└── requirements.txt
```


## 👤 Roles de usuario

- **Admin**: Puede crear y gestionar usuarios, programas, semestres y asignar relaciones.
- **Docente**: Consultar y evaluar notas de semestres asignados.
- **Estudiante**: Consultar su programa, semestres y calificaciones.

## ✅ Funcionalidades implementadas

- [x] Estructura profesional de proyecto con FastAPI.
- [x] Modelo `User` con validación de rol (`admin`, `teacher`, `student`).
- [x] Autenticación con JWT y protección de rutas según rol.
- [x] Encriptación de contraseñas con Bcrypt.
- [x] CRUD completo para usuarios.
- [x] Modelo `Programa` para carreras (ej: Ingeniería, Medicina, Inglés).
- [x] Modelo `Semestre` relacionado a un `Programa`.
- [x] Modelo `Nota` relacionada a un `Semestre`.
- [x] Conexión y migraciones con PostgreSQL y Alembic.
- [x] Asociación de estudiantes a programas.
- [x] Asociación de docentes a programas o semestres (estructura inicial).

## 📌 En desarrollo

- [ ] CRUD completo para `Programa`, `Semestre` y `Nota`.
- [ ] Vista agregada de calificaciones por estudiante.
- [ ] Reglas automáticas de aprobación y certificación final.
- [ ] Gestión avanzada para materias, proyectos y sesiones (plan futuro).
- [ ] CRUD extendido para asignación de docentes a semestres.

## 🔐 Seguridad

- Autenticación con JWT.
- Protección de rutas y control por rol.
- Validación de datos con Pydantic.
- Contraseñas encriptadas con Bcrypt.

## 🧪 Instalación y ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/AndresDev-20/UniverCity__Backend.git
cd univercity


2. Crea el entorno virtual e instálalo:

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Configura la conexión a PostgreSQL en `.env` o en `config.py`.

4. Ejecuta las migraciones:

```bash
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
Full Stack Developer | Apasionado por la tecnología educativa  
🔗 [LinkedIn](https://www.linkedin.com/in/yeison-andres-marroqu%C3%ADn-bernal-008138266/) | 🐙 [GitHub](https://github.com/AndresDev-20)
