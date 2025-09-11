import streamlit as st

import time



st.title("Numeros Impares")



st.write("Escrever um algoritmo que mostra os numeros impares de 1 a 20")

st.write("Clique no botão para iniciar.")



if st.button("Iniciar"):  

    for i in range(1,21, 2):

        st.write(i)

        time.sleep(0.5)

    st.success("Fim")

else:

    st.warning("Inicie a contagem")