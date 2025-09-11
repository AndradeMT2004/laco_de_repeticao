import streamlit as st


st.title("Tabuada")

st.header("Multiplicação")

num = st.number_input("Digite o numero que você quer multiplicar: ",step=1)

if st.button("Iniciar"):

    for i in range(0, 11, 1):

        produto = i * num

        st.write(f"{i} x {num} = {produto}")

else:

    st.warning("Digite um numero")

