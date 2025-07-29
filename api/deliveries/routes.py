from fastapi import APIRouter
from datetime import date
from database import get_db
from sqlmodel import Session
from crud import get_expected_date

delivery_router = APIRouter()

@delivery_router.post("/dataprevista")
async def expected_date(cep_origem: str, cep_destino: str, data_embarque: date, db: Session = Depends(get_db())):
    return get_expected_date(cep_origem, cep_destino, data_embarque, db)

@delivery_router.post("/cep")
async def create_cidade(cep: str, cidade: str, uf: str, segunda: bool, terca: bool, quarta: bool, quinta: bool, sexta: bool, sabado: bool, domingo: bool, db: Session = Depends(get_db())):
    return null

@delivery_router.put("/cep/{cep}")
async def update_cidade(cep: str, cidade: str, uf: str, segunda: bool, terca: bool, quarta: bool, quinta: bool, sexta: bool, sabado: bool, domingo: bool, db: Session = Depends(get_db())):
    return null

@delivery_router.get("/cep/{cep}")
async def get_cidade(cep: str, db: Session = get_db()):
    return null

@delivery_router.delete("/cep/{cep}")
async def delete_cidade(cep: str, db: Session = get_db()):
    return null