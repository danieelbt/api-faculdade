from typing import List

from pydantic import BaseModel


class Profissional(BaseModel):
    nome: str
    especialidade: str

class ProfissionaisList(BaseModel):
    profissionais: List[Profissional]
