from fastapi import HTTPException
from sqlalchemy import select, update, delete
from models import CityModel
from datetime import date
from sqlmodel import Session

def crud_expected_date(cep_origem: str, cep_destino: str, data_embarque: date, db: Session):
    query = "SELECT fnc_calcular_prazo($1, $2, $3)"
    try:
        return db.execute(query, cep_origem, cep_destino, data_embarque)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="falha ao chamar o banco")

def create_city(cep: str, cidade: str, uf: str, segunda: bool, terca: bool, quarta: bool, quinta: bool, sexta: bool, sabado: bool, domingo: bool, db: Session)
    cidade = CityModel(cep, cidade, uf, segunda, terca, quarta, quinta, sexta, sabado, domingo)
    try:
        db.add(cidade)
        db.commit()
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="falha ao chamar o banco")

def update_city(cep: str, cidade: str, uf: str, segunda: bool, terca: bool, quarta: bool, quinta: bool, sexta: bool, sabado: bool, domingo: bool, db: Session)
    update_query = update(CityModel).where(CityModel.cep == cep).values(city = cidade, uf = uf, monday = segunda, tuesday = terca, wednesday = quarta, thursday = quinta, saturday = sabado, sunday = domingo)
    try:
        db.execute(update_query)
        db.commit()
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="falha ao chamar o banco")

def get_city(cep: str, db: Session)
    select_query = select(CityModel).where(CityModel.cep == cep)
    try:
        return db.execute(select_query).one_or_none()._asdict()
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="falha ao chamar o banco")

def get_city(cep: str, db: Session)
    delete_query = delete(CityModel).where(CityModel.cep == cep)
    try:
        db.execute(delete_query).one_or_none()._asdict()
        db.commit()
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="falha ao chamar o banco")