import streamlit as st #implementação da maquina preditiva
import nltk  #natural languege tool kit 
from nltk.sentiment.vader import SentimentIntensityAnalyzer #analisador de sentimento

### Para contruir esse projeto é necessario 3 Fases
#     1°Fase: Criação do Sistema 
#     2°Fase: Criação do MP/NLP 
#     3°Fase: Utilização do sistema           ###

# 1°Fase: Criação do Sistema

st.write("Analise de Satisfação do Cliente")
user_input = st.text_input("Por favor, avalie o atendimento:")

# 2°Fase: Criação do MP/NLP 
nltk.download('vader_lexicon') # o vader_lexicon é um dicionario em inglês de palavras que o nltk usa para analisar o sentimento
sats = SentimentIntensityAnalyzer() #analisador de sentimento
score = sats.polarity_scores(user_input) #polaridade da frase do usuario

if score == 0:
    st.write("Neutro")
elif score["neg"] != 0:
    st.write("Analise Negativa!")
elif score["pos"] != 0: 
    st.write("Analise Positiva!")

# 3°Fase: Utilização do sistema

### Para utilizar o sistema, deve ir ao terminal e colocar o comando 'streamlit run nomedoProjeto.py ###

