import streamlit as st
import time

st.title("Contagem regressiva")
st.write("escrever um algoritmo que solicita ao usuario um numero e faça a contagem a partir do numero informado ate o numero 1, aguardando um segundo para exibir cada numero")
num = st.number_input("Digite um numero",step=1, min_value=0)

if st.button("Iniciar"):
    for i in range(num, 0, -1):
        st.write(i)
        time.sleep(1)
    st.success("FIM")
else:
    st.warning("Digite um numero")