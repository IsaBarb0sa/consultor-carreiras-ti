# Consultor Inteligente de Carreiras em TI

Trabalho da disciplina **Inteligência Artificial** — Ciência da Computação, UNIPAC Barbacena.

Sistema especialista baseado em regras explícitas que entrevista o usuário e recomenda **uma entre dez trilhas de carreira em TI**, apresentando a pontuação e as regras que justificam a escolha.

## Tecnologias

- Python 3.10 ou superior
- Experta 1.9.4, com motor de inferência baseado em regras `@Rule`
- Streamlit, interface web
- Pytest, testes automatizados

## Como executar

Abra um terminal na pasta deste projeto:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

No Linux/macOS, substitua os dois últimos comandos por `.venv/bin/python -m pip install -r requirements.txt` e `.venv/bin/python -m streamlit run app.py`.

O navegador abrirá a entrevista. Preencha os quatro campos e clique em **Descobrir minha carreira**.

## Matriz de decisão

Cada opção corresponde a uma trilha. O motor ativa regras independentes, permitindo perfis mistos:

| Resposta | Regra | Pontos |
| --- | --- | ---: |
| Atividade cotidiana preferida | Compatibilidade com a atividade | +5 |
| Tipo de entrega desejada | Compatibilidade com o resultado | +4 |
| Ferramenta de afinidade | Compatibilidade com conhecimento atual | +3 |
| Alta matemática + atividade de ciência de dados | Reforço de modelagem | +2 |
| Baixa matemática + atividade de engenharia de dados | Reforço de pipelines | +2 |
| Atividade + entrega de segurança | Convergência de defesa | +2 |
| Atividade + entrega de DevOps | Convergência de confiabilidade | +2 |

**Total: 34 regras `@Rule`** (30 de compatibilidade e 4 cruzadas). A recomendação é a trilha com maior soma. Em empate, usa-se uma ordem fixa definida em `carreiras.py`, e o usuário é informado. A afinidade matemática não elimina nenhuma carreira. A ferramenta "Nenhuma / iniciante" não gera pontuação, mas permite recomendar pela atividade e entrega.

### Associação das 10 trilhas

| Trilha | Atividade | Entrega | Ferramenta |
| --- | --- | --- | --- |
| Back-end | Criar APIs | Serviços e APIs | Java/C# |
| Front-end & UI/UX | Desenhar telas | Experiência intuitiva | JavaScript/CSS |
| Ciência de Dados/ML | Investigar padrões | Previsões | Python/estatística |
| Engenharia de Dados | Fluxos de dados | Dados disponíveis | Python/SQL |
| Cibersegurança | Proteger sistemas | Defesa contra ataques | Linux/redes |
| DevOps & SRE | Automatizar entregas | Implantações estáveis | Docker/CI-CD |
| Cloud | Projetar infraestrutura | Escalabilidade | AWS/Azure/GCP |
| Mobile | Criar apps | Aplicativo móvel | Kotlin/Swift/Flutter |
| QA | Testar software | Software confiável | Selenium/Pytest |
| Product Management | Priorizar soluções | Impacto de negócio | Figma/métricas/Agile |

## Validação por personas

Execute:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

As quatro personas principais de validação são:

1. **Ana (analítica):** matemática alta, padrões, Python/estatística, previsões → Ciência de Dados.
2. **Bruno (segurança):** matemática média, proteger sistemas, Linux/redes, defesa → Cibersegurança.
3. **Carla (visual):** matemática baixa, desenhar telas, JavaScript/CSS, experiência intuitiva → Front-end.
4. **Diego (negócios):** matemática média, prioridades, Figma/métricas, impacto → Gestão de Produtos.

Os testes também exercitam as outras seis trilhas, o perfil iniciante, entradas inválidas e o número mínimo de regras.

## Organização

- `app.py`: perguntas, formulário e apresentação dos resultados.
- `carreiras.py`: opções e tabela de associação das carreiras.
- `motor.py`: fatos, 34 regras Experta, inferência e ranking.
- `tests/test_personas.py`: testes das personas.

> Trabalho didático: a pontuação representa regras ativadas, não uma probabilidade de sucesso profissional.

## Relatório do projeto

O relatório apresenta o desenvolvimento, o funcionamento,
as regras de inferência e os testes do sistema especialista.

📄 [Visualizar relatório completo](docs/Relatorio_Consultor_Carreiras_TI.pdf)
