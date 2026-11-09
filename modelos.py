from sqlalchemy import String, CheckConstraint, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Sala(Base):

    __tablename__ = "salas"

    __table_args = (
        CheckConstraint("capacidad > 0", name="capacidad_positiva")
    )

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    capacidad: Mapped[int] = mapped_column(nullable=False)
    disponible: Mapped[bool] = mapped_column(nullable=False, default=True)


class Reserva(Base):

    __tablename__ = "reservas"

    __table_args__ = (
        
    )

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    estudiante: Mapped[str] = mapped_column(String(100), nullable=False)
    sala_id: Mapped[int] = mapped_column(ForeignKey("salas.id"), nullable=False)
    fecha: Mapped[str] = mapped_column(String(10), nullable=False)