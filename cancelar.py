from sqlalchemy.orm import Session

from conexion import engine
from modelos import Sala, Reserva



def cancelar_reserva(reserva_id):
    with Session(engine) as session:
        reserva = session.get(Reserva, reserva_id)
        if not reserva:
            raise ValueError(f"No existe una reserva con ID {reserva_id}.")
        
        sala = session.get(Sala, reserva.sala_id)
        sala.disponible = True
        
        session.delete(reserva)
        session.commit()
        print(f"La reserva con ID {reserva_id} ha sido cancelada exitosamente.")
        return reserva_id
