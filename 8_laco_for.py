import streamlit as st 

st.title("Contagem de numeros pares")

st.header("Clique abaixo para iniciar a contagem")

if st.button("Iniciar"):
    for i in range(100, 122, 2):
        st.write(i)
else:
    st.warning("Clique no botão para iniciar")