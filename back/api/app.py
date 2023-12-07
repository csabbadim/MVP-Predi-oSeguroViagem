from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from sqlalchemy import and_

from model import Session, Cliente, Model
from logger import logger
from schemas import *
from flask_cors import CORS

# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cliente_tag = Tag(name="Cliente", description="Adição, visualização, remoção e predição de clientes")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de clientes
@app.get('/clientes', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})
def get_clientes():
    """Lista todos os clientes cadastrados na base
    Retorna uma lista de clientes cadastrados na base.
    
    Args:
        nome (str): nome do cliente
        
    Returns:
        list: lista de clientes cadastrados na base
    """
    session = Session()
    
    # Buscando todos os clientes
    clientes = session.query(Cliente).all()
    
    if not clientes:
        logger.warning("Não há clientes cadastrados na base :/")
        return {"message": "Não há clientes cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d clientes econtrados" % len(clientes))
        return apresenta_clientes(clientes), 200


# Rota de adição de clientes
@app.post('/cliente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: ClienteSchema):
    """Adiciona um novo cliente à base de dados
    Retorna uma representação dos clientes e diagnósticos associados.
    
    Args:
        age = idade do cliente
        employment_type= tipo de emprego, se é Government Sector ou Private Sector/Self Employed
        graduate_or_not= se já é formado ou não
        annual_income= salário por ano
        family_members= número de familiares
        chronic_diseases= se tem doenças crônicas
        frequent_flyer= se viaja frequentemente
        ever_travelled_abroad= se já viajou antes
        
    Returns:
        travel_insurance= prevê se precisa de um seguro de viagem ou não
    """
    
    # Carregando modelo
    ml_path = 'ml_model/classificador.pkl'
    modelo = Model.carrega_modelo(ml_path)

    cliente = Cliente(
        age = form.age,
        employment_type=form.employment_type,
        graduate_or_not=form.graduate_or_not,
        annual_income=form.annual_income,
        family_members=form.family_members,
        chronic_diseases=form.chronic_diseases,
        frequent_flyer=form.frequent_flyer,
        ever_travelled_abroad=form.ever_travelled_abroad,
        travel_insurance=Model.preditor(modelo, form)
    )
    logger.debug(f"Adicionando produto de nome: '{cliente.age}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se cliente já existe na base
        if (session.query(Cliente)
                   .filter(and_(
                       Cliente.age == form.age,
                       Cliente.employment_type == form.employment_type,
                       Cliente.graduate_or_not == form.graduate_or_not,
                       Cliente.annual_income == form.annual_income,
                       Cliente.family_members == form.family_members,
                       Cliente.chronic_diseases == form.chronic_diseases,
                       Cliente.frequent_flyer == form.frequent_flyer,
                       Cliente.ever_travelled_abroad == form.ever_travelled_abroad
                   ))
                   .first()):
            error_msg = "Cliente já existente na base :/"
            logger.warning(f"Erro ao adicionar cliente, {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando cliente
        session.add(cliente)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado cliente")
        return apresenta_cliente(cliente), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar cliente, {error_msg}")
        return {"message": error_msg}, 400    

# Rota de remoção de cliente por nome
@app.delete('/cliente', tags=[cliente_tag],
            responses={"200": ClienteViewSchema, "404": ErrorSchema})
def delete_cliente(query: ClienteDelSchema):
    """Remove um cliente cadastrado na base a partir de suas informações
    """

    age = unquote(unquote(str(query.age)))
    annual_income = unquote(unquote(str(query.annual_income)))
    chronic_diseases = unquote(unquote(str(query.chronic_diseases)))
    employment_type = unquote(unquote(str(query.employment_type)))
    ever_travelled_abroad = unquote(unquote(str(query.ever_travelled_abroad)))
    family_members = unquote(unquote(str(query.family_members)))
    frequent_flyer = unquote(unquote(str(query.frequent_flyer)))
    graduate_or_not = unquote(unquote(str(query.graduate_or_not)))
    travel_insurance = unquote(unquote(str(query.travel_insurance)))
    logger.debug(f"Deletando dados sobre cliente")
    
     # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Cliente).filter(Cliente.age == age, Cliente.annual_income == annual_income,
                                         Cliente.chronic_diseases == chronic_diseases, Cliente.employment_type == employment_type,
                                         Cliente.ever_travelled_abroad == ever_travelled_abroad, Cliente.family_members == family_members,
                                         Cliente.frequent_flyer == frequent_flyer, Cliente.graduate_or_not == graduate_or_not,
                                         Cliente.travel_insurance == travel_insurance,).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Cliente deletado")
        return {"mesage": "Cliente removido"}
    else:
        # se o cliente não foi encontrado
        error_msg = "Clente não encontrada na base :/"
        logger.warning(f"Erro ao deletar cliente, {error_msg}")
        return {"mesage": error_msg}, 404