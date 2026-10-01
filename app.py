import numpy as np
import pandas as pd
import streamlit as st

st.header('Jogando uma moeda')

number_of_trials = st.slider('Número de tentativas?', 1, 1000, 10)

if st.button('Executar'):
    results = np.random.randint(0, 2, size=number_of_trials)

    data = pd.DataFrame({
        'Tentativa': range(1, number_of_trials + 1),
        'Resultado (0 ou 1)': results
    })

    data['Média acumulada'] = data['Resultado (0 ou 1)'].expanding().mean()

    st.line_chart(data, x='Tentativa', y='Média acumulada')
    st.dataframe(data)
