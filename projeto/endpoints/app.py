from fastapi import FastAPI

from projeto.data.enum import Especialidade
from projeto.data.fake_database import get_profissionais
from projeto.schemas import Message, Profissional, ProfissionaisList
from projeto.service.profissionais_service import profissionais_service

app = FastAPI()

lista_profissionais = get_profissionais()


@app.get('/', response_model=Message, include_in_schema=False)
def ola_mundo():
    return {'message': 'Olá, mundo!'}


@app.get(
    '/todos-profissionais',
    response_model=ProfissionaisList,
    summary='Pesquisa todos os profissionais',
)
def pesquisar_profissionais():
    return {'profissionais': lista_profissionais}


@app.get(
    '/profissionais/{nome}',
    response_model=Profissional,
    summary='Pesquisa o profissional por nome',
)
def pesquisar_por_nome(nome: str):
    return profissionais_service.pesquisar_por_nome(nome)


@app.get(
    '/profissionais',
    response_model=ProfissionaisList,
    summary='Pesquisa profissionais por especialidade',
)
def pesquisar_por_especialidade(especialidade: Especialidade):
    profissionais = profissionais_service.pesquisar_por_especialidade(especialidade)
    return {'profissionais': profissionais}
