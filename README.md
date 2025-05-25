# 🎓 UniverCity – Plataforma Virtual Educativa con FastAPI

**UniverCity** es una plataforma virtual educativa construida con **FastAPI**, que permite a universidades ofrecer clases en línea, gestionar usuarios (administradores, docentes y estudiantes), tareas, lecciones, entregas y calificaciones.

El sistema implementa autenticación segura con JWT, control de acceso por roles, migraciones con Alembic y almacenamiento en base de datos PostgreSQL.

## 🚀 Tecnologías utilizadas

- **FastAPI** – Framework web moderno y rápido.
- **SQLAlchemy** – ORM para manejo de modelos y base de datos.
- **Alembic** – Migraciones automáticas de base de datos.
- **PostgreSQL** – Motor de base de datos relacional.
- **Pydantic** – Validación y serialización de datos.
- **JWT (JSON Web Tokens)** – Autenticación y autorización.
- **Bcrypt** – Encriptación de contraseñas.

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

- **Admin**: Gestión de usuarios, cursos y control general del sistema.
- **Teacher**: Crea cursos, lecciones y tareas. Califica a los estudiantes.
- **Student**: Se inscribe en cursos, entrega tareas y consulta calificaciones.

## ✅ Funcionalidades implementadas

- [x] Estructura profesional del proyecto.
- [x] Modelo `User` con campos: nombre, apellido, email, contraseña y rol.
- [x] Validación de roles mediante `Enum` (`admin`, `teacher`, `student`).
- [x] Encriptación segura de contraseñas con Bcrypt.
- [x] Autenticación mediante JWT.
- [x] CRUD completo de usuarios.
- [x] Conexión con base de datos PostgreSQL.
- [x] Migraciones con Alembic.

## 📌 En desarrollo

- [ ] Protección de rutas según el rol del usuario.
- [ ] Modelo y CRUD para cursos y lecciones.
- [ ] Modelo y CRUD para tareas y entregas.
- [ ] Sistema de calificaciones (escala del 1 al 10).
- [ ] Gestión de clases virtuales con URL de videollamadas.
- [ ] Panel de visualización de calificaciones por estudiante.

## 🔐 Seguridad

- Uso de JWT para autenticación segura.
- Encriptación de contraseñas con Bcrypt.
- Validación y control de permisos según rol en endpoints.

## 🧪 Instalación y ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/univercity.git
cd univercity
```

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
🔗 [LinkedIn](https://www.linkedin.com/) | 🐙 [GitHub](https://github.com/tuusuario)
