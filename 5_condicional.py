import streamlit as st

st.title("Media do Aluno")

media = st.number_input("Digite a sua media")

if st.button("Calcular media"):
    if media >= 7:
        st.success("Aprovado")
    else:
        st.error("Reprovado!")
else:
    st.warning("Digite sua media")

# Success - Verde
# Warning - Amarelo
# Info - azul
# Erro - Vermelho