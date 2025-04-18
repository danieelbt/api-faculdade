from http import HTTPStatus

from fastapi import HTTPException

from projeto.data.fake_database import get_profissionais

lista_profissionais = get_profissionais()

class ProfissionaisService():
    @staticmethod
    def pesquisar_por_nome(nome: str):
        profissional = None
        for profissional_atual in lista_profissionais:
            if profissional_atual['nome'] == nome:
                profissional = profissional_atual
                return profissional
        if not profissional:
            raise HTTPException(
                detail='Não existem profissionais com esse nome',
                status_code=HTTPStatus.BAD_REQUEST
            )

    @staticmethod
    def pesquisar_por_especialidade(especialidade: str):
        profissionais = []
        for profissional in lista_profissionais:
            if profissional['especialidade'] == especialidade:
                profissionais.append(profissional)
        return profissionais

profissionais_service = ProfissionaisService()
