from sqlalchemy.orm import Session
from sqlalchemy import select

from modelos import Sala, Reserva
from conexion import engine

def consultar_salas():
    with Session(engine) as session:
        salas = session.scalars(select(Sala)).all()

        if not salas:
            print("No hay salas registradas.")
            return []

        for salas in salas:
            print(f"ID: {salas.id}, Nombre: {salas.nombre}, Capacidad: {salas.capacidad}, Disponible: {salas.disponible}")

def consultar_reservas():
    with Session(engine) as session:
        reservas = session.scalars(select(Reserva)).all()

        if not reservas:
            print("No hay reservas agendadas.")
            return []
        for reserva in reservas:
            sala = session.get(Sala, reserva.sala_id)
            print(f"ID: {reserva.id}, Estudiante: {reserva.estudiante}, Sala: {sala.nombre}, Fecha: {reserva.fecha}")
        return reservas
