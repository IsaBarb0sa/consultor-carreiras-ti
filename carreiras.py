"""Vocabulário e matriz de decisão do sistema especialista."""

TRILHAS = {
    "backend": ("Desenvolvimento Back-end", "Constrói APIs, regras de negócio e sistemas conectados a bancos de dados."),
    "frontend": ("Desenvolvimento Front-end & UI/UX", "Cria interfaces acessíveis, agradáveis e fáceis de usar."),
    "ciencia": ("Ciência de Dados e Machine Learning", "Explora dados com estatística e cria modelos preditivos."),
    "engenharia": ("Engenharia de Dados", "Constrói pipelines e estruturas para armazenar e disponibilizar dados."),
    "seguranca": ("Cibersegurança", "Protege sistemas e investiga vulnerabilidades."),
    "devops": ("DevOps & SRE", "Automatiza entregas, monitora serviços e aumenta a confiabilidade."),
    "cloud": ("Computação em Nuvem", "Planeja infraestruturas escaláveis em provedores de nuvem."),
    "mobile": ("Desenvolvimento Mobile", "Desenvolve aplicativos para celulares e tablets."),
    "qa": ("Engenharia de Qualidade e Testes (QA)", "Previne defeitos e automatiza verificações de software."),
    "produto": ("Gestão de Produtos", "Prioriza necessidades de clientes e coordena a evolução de produtos."),
}

ATIVIDADES = {
    "Criar APIs e regras de negócio": "backend",
    "Desenhar telas e melhorar usabilidade": "frontend",
    "Investigar padrões e prever resultados": "ciencia",
    "Organizar bases e fluxos de dados": "engenharia",
    "Investigar falhas e proteger sistemas": "seguranca",
    "Automatizar entregas e monitorar serviços": "devops",
    "Projetar recursos de infraestrutura na nuvem": "cloud",
    "Criar aplicativos para celular": "mobile",
    "Encontrar bugs e automatizar testes": "qa",
    "Definir prioridades e conversar com usuários": "produto",
}

ENTREGAS = {
    "Serviços e APIs funcionando": "backend",
    "Uma experiência visual intuitiva": "frontend",
    "Previsões e descobertas baseadas em dados": "ciencia",
    "Dados organizados e disponíveis": "engenharia",
    "Proteção contra ataques": "seguranca",
    "Implantações estáveis e automatizadas": "devops",
    "Infraestrutura escalável": "cloud",
    "Aplicativo útil no celular": "mobile",
    "Software confiável e testado": "qa",
    "Produto que resolve problemas de negócio": "produto",
}

FERRAMENTAS = [
    "Python e estatística", "Python e SQL", "Java ou C#", "JavaScript, HTML e CSS",
    "Linux e segurança de redes", "Docker, Git e CI/CD", "AWS, Azure ou GCP",
    "Kotlin, Swift ou Flutter", "Selenium, Pytest ou testes", "Figma, métricas e Agile",
    "Nenhuma / iniciante",
]

FERRAMENTA_PARA_TRILHA = {
    "Python e estatística": "ciencia", "Python e SQL": "engenharia",
    "Java ou C#": "backend", "JavaScript, HTML e CSS": "frontend",
    "Linux e segurança de redes": "seguranca", "Docker, Git e CI/CD": "devops",
    "AWS, Azure ou GCP": "cloud", "Kotlin, Swift ou Flutter": "mobile",
    "Selenium, Pytest ou testes": "qa", "Figma, métricas e Agile": "produto",
}

# Desempate público e estável. Nenhuma opção é privilegiada por sorteio.
ORDEM = tuple(TRILHAS)
