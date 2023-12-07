## Minha API

Este projeto faz parte do material para entrega do MVP da pós graduação em Engenharia de Software.

Esse projeto possui um modelo que tem como objetivo prever se um cliente terá interesse em comprar um pacote de seguro de viagem.
Para isso, deve preencher os seguintes parâmetros:
Idade: Idade do cliente;
Tipo de emprego: Setor Governamental ou Setor Privado/Autônomo;
Graduação: Se o cliente já é graduado na universidade;
Renda anual: A renda anual do cliente;
Nº de membros da família: Número de membros da família do cliente;
Doença Crônica: Se o cliente sofre de alguma doença crônica/grave;
Viaja frequentemente: Considera se o cliente viajou mais de quatro vezes nos últimos dois anos. Se sim, então viaja frequentemente;
Já viajou para o exterior: Se o cliente já viajou para um país no exterior

---
## Como executar o backend


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.


## Como executar o teste
No diretório raiz, pelo terminal, executar o comando abaixo.

```
(env)$ pytest -v test_modelo.py
```