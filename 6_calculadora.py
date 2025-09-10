import streamlit as st

st.title("Calculadora")

a = st.number_input("Digite o numero A: ", step=0)
b = st.number_input("Digite o numero B: ", step=0)

media = (a + b) / 2
soma = a + b
produto = a * b
menor_valor = min(a, b)
maior_valor = max(a, b)

if st.button("Calcular"):
    st.write(f"Media: ", media)
    st.write(f"Soma: ", soma)
    st.write(f"Menor valor: ", menor_valor)
    st.write(f"Maior valor", maior_valor)
else:
    st.warning("Digite o numero A e B")