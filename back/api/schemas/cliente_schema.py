from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Cliente
import json
import numpy as np

class ClienteSchema(BaseModel):
    """ Define como um novo cliente a ser inserido deve ser representado
    """
    age: str = 18
    employment_type: str = "Setor Governamental"
    graduate_or_not: str = "Sim"
    annual_income: float = 10000
    family_members: int = 3
    chronic_diseases: str = "Sim"
    frequent_flyer: str = "Sim"
    ever_travelled_abroad: str = "Sim"
    
# Função auxiliar para mapear "sim" e "não" para 1 e 0
def map_sim_nao(value):
    return 1 if value.lower() == "sim" else 0

class ClienteViewSchema(BaseModel):
    """Define como um cliente será retornado
    """
    age: int = 18
    employment_type: str = "Setor Governamental"
    graduate_or_not: str = "Sim"
    annual_income: float = 15000
    family_members: int = 3
    chronic_diseases: str = "Sim"
    frequent_flyer: str = "Sim"
    ever_travelled_abroad: str = "Sim"

class ListaClientesSchema(BaseModel):
    """Define como uma lista de clientes será representada
    """
    clientes: List[ClienteSchema]
    
class ClienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    age: str
    employment_type: str
    graduate_or_not: str
    annual_income: float
    family_members: int
    chronic_diseases: str
    frequent_flyer: str
    ever_travelled_abroad: str
    travel_insurance: int
    
# Apresenta apenas os dados de um cliente    
def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    return {
        "age": cliente.age,
        "employment_type": cliente.employment_type,
        "graduate_or_not": cliente.graduate_or_not,
        "annual_income": cliente.annual_income,
        "family_members": cliente.family_members,
        "chronic_diseases": cliente.chronic_diseases,
        "frequent_flyer": cliente.frequent_flyer,
        "ever_travelled_abroad": cliente.ever_travelled_abroad,
        "travel_insurance": cliente.travel_insurance
    }
    
# Apresenta uma lista de clientes
def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
            "age": cliente.age,
            "employment_type": cliente.employment_type,
            "graduate_or_not": cliente.graduate_or_not,
            "annual_income": cliente.annual_income,
            "family_members": cliente.family_members,
            "chronic_diseases": cliente.chronic_diseases,
            "frequent_flyer": cliente.frequent_flyer,
            "ever_travelled_abroad": cliente.ever_travelled_abroad,
            "travel_insurance": cliente.travel_insurance
        })

    return {"clientes": result}