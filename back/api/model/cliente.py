from sqlalchemy import Column, String, Integer, DateTime, Float, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Cliente(Base):
    __tablename__ = 'clientes'
    
    id = Column("pk_cartas", Integer, primary_key=True)
    age = Column("Age", Integer)
    employment_type = Column("Employment Type", Integer)
    graduate_or_not = Column("GraduateOr0t", Integer)
    annual_income = Column("AnnualIncome", Float)
    family_members = Column("FamilyMembers", Integer)
    chronic_diseases = Column("ChronicDiseases", Integer)
    frequent_flyer = Column("FrequentFlyer", Integer)
    ever_travelled_abroad = Column("EverTravelledAbroad", Integer)
    travel_insurance = Column("TravelInsurance", Integer)

    UniqueConstraint(age, employment_type, graduate_or_not, annual_income, family_members, chronic_diseases, frequent_flyer, ever_travelled_abroad, travel_insurance)

    def __init__(self, age: int, employment_type: int, graduate_or_not: int,
                 annual_income: float, family_members: int, chronic_diseases: int,
                 frequent_flyer: int, ever_travelled_abroad: int, travel_insurance: int):
        """
        Cria um Cliente

        Arguments:
            age: Idade do cliente.
            employment_type: Tipo de emprego do cliente.
            graduate_or_not: Se o cliente é graduado ou não (1 para Sim, 0 para Não).
            annual_income: Renda anual do cliente.
            family_members: Número de membros na família do cliente.
            chronic_diseases: Se o cliente tem doenças crônicas (1 para Sim, 0 para Não).
            frequent_flyer: Se o cliente é um viajante frequente (1 para Sim, 0 para Não).
            ever_travelled_abroad: Se o cliente já viajou para o exterior (1 para Sim, 0 para Não).
            travel_insurance: Se o cliente possui seguro de viagem (1 para Sim, 0 para Não).
        """
        self.age = age
        self.employment_type = employment_type
        self.graduate_or_not = graduate_or_not
        self.annual_income = annual_income
        self.family_members = family_members
        self.chronic_diseases = chronic_diseases
        self.frequent_flyer = frequent_flyer
        self.ever_travelled_abroad = ever_travelled_abroad
        self.travel_insurance = travel_insurance