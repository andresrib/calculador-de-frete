from database import Base

class CityModel(Base):
    __tablename__ = 'cities'
    cep: Mapped[str] = mapped_column(primary_key=True)
    city: Mapped[str]
    uf: Mapped[str]
    sunday: Mapped[bool]
    monday: Mapped[bool]
    tuesday: Mapped[bool]
    wednesday: Mapped[bool]
    thursday: Mapped[bool]
    friday: Mapped[bool]
    saturday: Mapped[bool]

    def __init__(cep: str, cidade: str, uf: str, segunda: bool, terca: bool, quarta: bool, quinta: bool, sexta: bool, sabado: bool, domingo: bool):
        self.cep = cep
        self.city = cidade
        self.uf = uf
        self.sunday = domingo
        self.monday = segunda
        self.tuesday = terca
        self.wednesday = quarta
        self.thursday = quinta
        self.friday = sexta
        self.saturday = sabado