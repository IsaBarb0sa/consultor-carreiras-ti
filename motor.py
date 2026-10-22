"""Motor de inferência por encadeamento para frente usando Experta."""

# Experta 1.9.4 depende de frozendict antigo, que usa aliases removidos do
# módulo collections em versões modernas do Python.
import collections
import collections.abc

for nome in ("Mapping", "MutableMapping", "Sequence"):
    if not hasattr(collections, nome):
        setattr(collections, nome, getattr(collections.abc, nome))

from experta import Fact, KnowledgeEngine, Rule

from carreiras import (
    ATIVIDADES, ENTREGAS, FERRAMENTA_PARA_TRILHA, ORDEM, TRILHAS,
)


class Preferencia(Fact):
    """Fato declarado durante a entrevista: dimensão e valor padronizado."""


class Consultor(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.pontos = {chave: 0 for chave in TRILHAS}
        self.motivos = {chave: [] for chave in TRILHAS}

    def pontuar(self, trilha, pontos, motivo):
        self.pontos[trilha] += pontos
        self.motivos[trilha].append(f"+{pontos}: {motivo}")

    # 10 regras de atividade (afinidade com o trabalho cotidiano).
    @Rule(Preferencia(tipo="atividade", valor="backend"))
    def atividade_backend(self): self.pontuar("backend", 5, "Gosta de criar APIs e lógica de negócio")

    @Rule(Preferencia(tipo="atividade", valor="frontend"))
    def atividade_frontend(self): self.pontuar("frontend", 5, "Gosta de criar interfaces")

    @Rule(Preferencia(tipo="atividade", valor="ciencia"))
    def atividade_ciencia(self): self.pontuar("ciencia", 5, "Gosta de investigar padrões e fazer previsões")

    @Rule(Preferencia(tipo="atividade", valor="engenharia"))
    def atividade_engenharia(self): self.pontuar("engenharia", 5, "Gosta de construir fluxos de dados")

    @Rule(Preferencia(tipo="atividade", valor="seguranca"))
    def atividade_seguranca(self): self.pontuar("seguranca", 5, "Gosta de investigar riscos e proteger sistemas")

    @Rule(Preferencia(tipo="atividade", valor="devops"))
    def atividade_devops(self): self.pontuar("devops", 5, "Gosta de automação e monitoramento")

    @Rule(Preferencia(tipo="atividade", valor="cloud"))
    def atividade_cloud(self): self.pontuar("cloud", 5, "Gosta de arquitetar infraestrutura em nuvem")

    @Rule(Preferencia(tipo="atividade", valor="mobile"))
    def atividade_mobile(self): self.pontuar("mobile", 5, "Gosta de desenvolver apps móveis")

    @Rule(Preferencia(tipo="atividade", valor="qa"))
    def atividade_qa(self): self.pontuar("qa", 5, "Gosta de encontrar bugs e testar")

    @Rule(Preferencia(tipo="atividade", valor="produto"))
    def atividade_produto(self): self.pontuar("produto", 5, "Gosta de ouvir usuários e priorizar soluções")

    # 10 regras de valor entregue (distinguem trabalho de resultado desejado).
    @Rule(Preferencia(tipo="entrega", valor="backend"))
    def entrega_backend(self): self.pontuar("backend", 4, "Valoriza serviços e APIs funcionando")

    @Rule(Preferencia(tipo="entrega", valor="frontend"))
    def entrega_frontend(self): self.pontuar("frontend", 4, "Valoriza experiência visual intuitiva")

    @Rule(Preferencia(tipo="entrega", valor="ciencia"))
    def entrega_ciencia(self): self.pontuar("ciencia", 4, "Valoriza previsões com dados")

    @Rule(Preferencia(tipo="entrega", valor="engenharia"))
    def entrega_engenharia(self): self.pontuar("engenharia", 4, "Valoriza disponibilizar dados confiáveis")

    @Rule(Preferencia(tipo="entrega", valor="seguranca"))
    def entrega_seguranca(self): self.pontuar("seguranca", 4, "Valoriza defesa contra ataques")

    @Rule(Preferencia(tipo="entrega", valor="devops"))
    def entrega_devops(self): self.pontuar("devops", 4, "Valoriza implantações estáveis")

    @Rule(Preferencia(tipo="entrega", valor="cloud"))
    def entrega_cloud(self): self.pontuar("cloud", 4, "Valoriza infraestrutura escalável")

    @Rule(Preferencia(tipo="entrega", valor="mobile"))
    def entrega_mobile(self): self.pontuar("mobile", 4, "Valoriza aplicativos móveis úteis")

    @Rule(Preferencia(tipo="entrega", valor="qa"))
    def entrega_qa(self): self.pontuar("qa", 4, "Valoriza software confiável")

    @Rule(Preferencia(tipo="entrega", valor="produto"))
    def entrega_produto(self): self.pontuar("produto", 4, "Valoriza impacto de negócio")

    # 10 regras de conhecimento atual: não excluem iniciantes.
    @Rule(Preferencia(tipo="ferramenta", valor="backend"))
    def ferramenta_backend(self): self.pontuar("backend", 3, "Tem afinidade com Java ou C#")

    @Rule(Preferencia(tipo="ferramenta", valor="frontend"))
    def ferramenta_frontend(self): self.pontuar("frontend", 3, "Tem afinidade com JavaScript e CSS")

    @Rule(Preferencia(tipo="ferramenta", valor="ciencia"))
    def ferramenta_ciencia(self): self.pontuar("ciencia", 3, "Tem afinidade com Python e estatística")

    @Rule(Preferencia(tipo="ferramenta", valor="engenharia"))
    def ferramenta_engenharia(self): self.pontuar("engenharia", 3, "Tem afinidade com Python e SQL")

    @Rule(Preferencia(tipo="ferramenta", valor="seguranca"))
    def ferramenta_seguranca(self): self.pontuar("seguranca", 3, "Tem afinidade com Linux e redes")

    @Rule(Preferencia(tipo="ferramenta", valor="devops"))
    def ferramenta_devops(self): self.pontuar("devops", 3, "Tem afinidade com Docker e CI/CD")

    @Rule(Preferencia(tipo="ferramenta", valor="cloud"))
    def ferramenta_cloud(self): self.pontuar("cloud", 3, "Tem afinidade com provedores de nuvem")

    @Rule(Preferencia(tipo="ferramenta", valor="mobile"))
    def ferramenta_mobile(self): self.pontuar("mobile", 3, "Tem afinidade com ferramentas mobile")

    @Rule(Preferencia(tipo="ferramenta", valor="qa"))
    def ferramenta_qa(self): self.pontuar("qa", 3, "Tem afinidade com ferramentas de teste")

    @Rule(Preferencia(tipo="ferramenta", valor="produto"))
    def ferramenta_produto(self): self.pontuar("produto", 3, "Tem afinidade com Figma e métricas")

    # Regras cruzadas adicionais: matemática distingue ciência de engenharia.
    @Rule(Preferencia(tipo="matematica", valor="Alta"), Preferencia(tipo="atividade", valor="ciencia"))
    def matematica_ciencia(self): self.pontuar("ciencia", 2, "Alta afinidade matemática reforça modelagem preditiva")

    @Rule(Preferencia(tipo="matematica", valor="Baixa"), Preferencia(tipo="atividade", valor="engenharia"))
    def matematica_engenharia(self): self.pontuar("engenharia", 2, "Prefere pipelines a modelagem estatística")

    @Rule(Preferencia(tipo="atividade", valor="seguranca"), Preferencia(tipo="entrega", valor="seguranca"))
    def coerencia_seguranca(self): self.pontuar("seguranca", 2, "Interesse e objetivo convergem em proteção")

    @Rule(Preferencia(tipo="atividade", valor="devops"), Preferencia(tipo="entrega", valor="devops"))
    def coerencia_devops(self): self.pontuar("devops", 2, "Interesse e objetivo convergem em confiabilidade")


def recomendar(matematica: str, atividade: str, ferramenta: str, entrega: str) -> dict:
    """Produz recomendação determinística e justificativas das regras ativadas."""
    if matematica not in ("Baixa", "Média", "Alta"):
        raise ValueError("Afinidade matemática inválida")
    if atividade not in ATIVIDADES or entrega not in ENTREGAS:
        raise ValueError("Atividade ou entrega inválida")
    if ferramenta not in (*FERRAMENTA_PARA_TRILHA, "Nenhuma / iniciante"):
        raise ValueError("Ferramenta inválida")
    motor = Consultor()
    motor.reset()
    motor.declare(Preferencia(tipo="matematica", valor=matematica))
    motor.declare(Preferencia(tipo="atividade", valor=ATIVIDADES[atividade]))
    motor.declare(Preferencia(tipo="entrega", valor=ENTREGAS[entrega]))
    if ferramenta in FERRAMENTA_PARA_TRILHA:
        motor.declare(Preferencia(tipo="ferramenta", valor=FERRAMENTA_PARA_TRILHA[ferramenta]))
    motor.run()
    ranking = sorted(ORDEM, key=lambda chave: (-motor.pontos[chave], ORDEM.index(chave)))
    vencedora = ranking[0]
    return {
        "chave": vencedora,
        "nome": TRILHAS[vencedora][0],
        "descricao": TRILHAS[vencedora][1],
        "pontos": motor.pontos[vencedora],
        "motivos": motor.motivos[vencedora],
        "ranking": [(TRILHAS[chave][0], motor.pontos[chave]) for chave in ranking],
        "empate": len(ranking) > 1 and motor.pontos[ranking[0]] == motor.pontos[ranking[1]],
    }
