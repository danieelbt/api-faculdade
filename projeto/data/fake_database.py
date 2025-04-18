import json

def get_profissionais():
    with open('projeto/data/profissionais.json', 'r', encoding='utf-8') as f:
        profissionais = json.load(f)
    return profissionais
