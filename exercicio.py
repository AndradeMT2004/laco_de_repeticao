import streamlit as st
import time

st.title("Soma")
st.header("Laço de repetição")
st.write("Escrever um programa de computador que solicite do usuario 5 numeros inteiros e,ao final, apresente a soma de todos os numeros lidos")

soma = 0

for i in range(1,6):
    num = st.number_input(f"Digite o {i} numero: ", step=1, min_value=0)
    soma = soma + num
    time.sleep(1)
    if num != 0:
        continue
if st.button("Inicie a soma"):
    st.success(F"O resultado da soma é: {soma}")


else:
    st.info("Informe um numero")