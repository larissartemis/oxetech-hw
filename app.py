import streamlit as st
import pandas as pd

st.title("Hello, World!")
st.write("Bem vindo ao seu primeiro app Streamlit :)")

st.header("título")
st.subheader("subtítulo")
st.text("texto")
st.markdown("texto com markdown: **negrito**, *itálico*")
st.markdown("##### cabeçalho com markdown")
st.markdown("- lista não numerada com markdown")
st.markdown("1. lista numerada com markdown")
st.markdown("`código`")

data = {
    'nome': ['ana', 'bruno', 'carlos'],
    'idade': [23, 34, 45],
    'cor favorita': ['amarelo', 'azul', 'cinza']
}
df = pd.DataFrame(data)
st.dataframe(df)
st.table(df)

if st.button('clique aqui'):
   st.write('clicado')

idade = st.slider('quantos anos você tem?', 0, 100, 25)
st.write(f'{idade} anos')

cor_selecionada = st.selectbox('Escolha uma cor:', ['Nenhuma'] + list(df['cor favorita']))
if cor_selecionada != 'Nenhuma':
    st.write(f'{cor_selecionada}')

col1, col2 = st.columns(2)

with col1:
     st.header('coluna')
     st.write('conteudo')

with col2:
     st.header('coluna')
     st.write('conteudo')

st.sidebar.header('menu lateral')
st.sidebar.write('escrevendo no menu lateral!')

