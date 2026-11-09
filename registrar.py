from sqlalchemy.orm import Session
from sqlalchemy import select

from modelos import Sala, Reserva
from conexion import engine

def insertar_sala(nombre, capacidad):
    if not nombre.strip():
        raise ValueError("El nombre de la sala no puede estar vacio.")
    if capacidad <= 0:
        raise ValueError("La capacidad de la sala debe ser un numero positivo.")
    
    with Session(engine) as session:
        nueva_sala = Sala(nombre=nombre, capacidad=capacidad)
        session.add(nueva_sala)
        session.commit()
        print(f"La sala '{nombre}' con capacidad {capacidad} ha sido insertada exitosamente.")
        print(f"El ID de la nueva sala es: {nueva_sala.id}")
        return nueva_sala.id

def registrar_reserva(estudiante, sala_id, fecha):
    if not estudiante.strip():
        raise ValueError("El nombre del estudiante no puede estar vacio.")
    if not fecha:
        raise ValueError("La fecha de la reserva no puede estar vacia.")
    with Session(engine) as session:
        sala = session.get(Sala, sala_id)
        if not sala:
            raise ValueError(f"No existe una sala con ID {sala_id}.")
        if not sala.disponible:
            raise ValueError(f"La sala '{sala.nombre}' no esta disponible para la fecha {fecha}.")
        
        nueva_reserva = Reserva(estudiante=estudiante, sala_id=sala_id, fecha=fecha)
        sala.disponible = False
        session.add(nueva_reserva)
        session.commit()
        print(f"La reserva para el estudiante '{estudiante}' en la sala '{sala.nombre}' para la fecha {fecha} ha sido registrada exitosamente.")
        print(f"El ID de la nueva reserva es: {nueva_reserva.id}")
        return nueva_reserva.id

    