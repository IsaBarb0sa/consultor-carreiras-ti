import pytest

from motor import Consultor, recomendar
from carreiras import ATIVIDADES, ENTREGAS, FERRAMENTA_PARA_TRILHA


def escolha(dicionario, chave):
    return next(rotulo for rotulo, valor in dicionario.items() if valor == chave)


@pytest.mark.parametrize("trilha,matematica,ferramenta", [
    ("ciencia", "Alta", "Python e estatística"),
    ("seguranca", "Média", "Linux e segurança de redes"),
    ("frontend", "Baixa", "JavaScript, HTML e CSS"),
    ("produto", "Média", "Figma, métricas e Agile"),
    ("engenharia", "Média", "Python e SQL"),
    ("backend", "Média", "Java ou C#"),
    ("devops", "Baixa", "Docker, Git e CI/CD"),
    ("cloud", "Média", "AWS, Azure ou GCP"),
    ("mobile", "Baixa", "Kotlin, Swift ou Flutter"),
    ("qa", "Média", "Selenium, Pytest ou testes"),
])
def test_personas(trilha, matematica, ferramenta):
    resultado = recomendar(matematica, escolha(ATIVIDADES, trilha), ferramenta, escolha(ENTREGAS, trilha))
    assert resultado["chave"] == trilha
    assert resultado["pontos"] >= 12
    assert len(resultado["motivos"]) >= 3


def test_iniciante_ainda_recebe_recomendacao():
    resultado = recomendar("Média", escolha(ATIVIDADES, "mobile"), "Nenhuma / iniciante", escolha(ENTREGAS, "mobile"))
    assert resultado["chave"] == "mobile"
    assert resultado["pontos"] == 9


def test_ha_pelo_menos_25_regras():
    from experta import Rule
    regras = [valor for valor in vars(Consultor).values() if isinstance(valor, Rule)]
    assert len(regras) >= 25


def test_respostas_invalidas():
    with pytest.raises(ValueError):
        recomendar("X", escolha(ATIVIDADES, "qa"), "Nenhuma / iniciante", escolha(ENTREGAS, "qa"))
