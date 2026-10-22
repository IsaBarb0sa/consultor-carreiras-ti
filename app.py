"""Interface web do consultor especialista de carreiras em TI."""

import streamlit as st

from carreiras import ATIVIDADES, ENTREGAS, FERRAMENTAS
from motor import recomendar

st.set_page_config(page_title="Consultor de Carreiras em TI", page_icon="🧭", layout="centered")

st.title("Consultor Inteligente de Carreiras em TI")
st.write("Responda quatro perguntas para descobrir uma trilha de TI alinhada aos seus interesses.")
st.caption("Sistema especialista acadêmico baseado em regras explícitas (Experta).")

with st.form("entrevista"):
    matematica = st.selectbox("1. Qual é sua afinidade com matemática e estatística?", ["Baixa", "Média", "Alta"], index=1)
    atividade = st.selectbox("2. Qual atividade você mais gostaria de fazer no dia a dia?", list(ATIVIDADES), index=None, placeholder="Selecione uma atividade")
    ferramenta = st.selectbox("3. Qual ferramenta ou área você mais conhece ou gosta?", FERRAMENTAS, index=None, placeholder="Selecione uma opção")
    entrega = st.selectbox("4. Qual resultado você gostaria de entregar?", list(ENTREGAS), index=None, placeholder="Selecione um resultado")
    enviar = st.form_submit_button("Descobrir minha carreira", type="primary", use_container_width=True)

if enviar:
    if not all((atividade, ferramenta, entrega)):
        st.warning("Responda todas as perguntas para receber uma recomendação.")
    else:
        resultado = recomendar(matematica, atividade, ferramenta, entrega)
        st.success(f"Trilha recomendada: {resultado['nome']}")
        st.write(resultado["descricao"])
        st.metric("Pontuação de compatibilidade (regras)", resultado["pontos"])
        if resultado["empate"]:
            st.info("Houve empate na pontuação. O sistema usou uma ordem fixa para desempatar; experimente rever suas respostas.")
        st.subheader("Por que essa recomendação?")
        for motivo in resultado["motivos"]:
            st.write(f"• {motivo}")
        st.subheader("Comparação das 10 trilhas")
        st.bar_chart({nome: pontos for nome, pontos in resultado["ranking"]}, horizontal=True)
        st.caption("As pontuações representam regras ativadas, não probabilidades ou testes psicológicos.")
