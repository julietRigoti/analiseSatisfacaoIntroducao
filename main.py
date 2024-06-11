import streamlit as st #implementação da maquina preditiva
import nltk  #natural languege tool kit 

### Para contruir esse projeto é necessario 3 Fases
#     1°Fase: Criação do Sistema 
#     2°Fase: Criação do MP/NLP 
#     3°Fase: Utilização do sistema           ###

# 1°Fase: Criação do Sistema

st.write("Analise de Satisfação do Cliente")
user_input = st.text_input("Por favor, avalie o atendimento:")

# 2°Fase: Criação do MP/NLP 
