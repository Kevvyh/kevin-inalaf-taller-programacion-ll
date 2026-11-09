# Taller Evaluado - Programación ll

## Objetivo
Aplicar el mapeo objeto-relacional (ORM) para definir entidades relacionadas, crear tablas, insertar, 
consultar y eliminar registros, y modificar el estado de una sala mediante transacciones. La interacción 
se realizará mediante un menú por consola.

## Situación Problematica
La biblioteca universitaria necesita administrar salas de estudio y sus reservas. 
Se solicita desarrollar una aplicación que registre salas, permita reservar una sala disponible, 
consulte las reservas y cancele una reserva liberando nuevamente la sala. La información debe 
persistir en la base de datos SQLite biblioteca.db.

## Instalacion de dependencias

1. Preparar y activar el entorno virtual
```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
```
2. Instalar y verificar versión de SQLAlchemy
```bash
python -m pip install "SQLAlchemy>=2.0,<3.0"
python -c "import sqlalchemy; print(sqlalchemy.__version__)
```

- Carrera: Ingeniería Civil en Informática
- Asignatura: Programación ll
- Docente: Pedro Gaete

- Alumno: Kevin Inalaf
