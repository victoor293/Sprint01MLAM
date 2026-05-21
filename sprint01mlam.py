import pandas as pd


df = pd.read_csv("World Energy Consumption.csv")


freq_abs = df["year"].value_counts().sort_index()
freq_rel = (df["year"].value_counts(normalize=True).sort_index()) * 100
freq_acum = freq_abs.cumsum()


tabela = pd.DataFrame({
    "Absoluta": freq_abs,
    "Relativa (%)": freq_rel.round(2),
    "Acumulada": freq_acum
})

print(tabela)

# Insight 1:
# O aumento da quantidade de registros nos anos mais recentes indica crescimento da coleta e monitoramento de dados energéticos, algo essencial
# para plataformas inteligentes como o ChargeGrid Intelligence, que dependem de análise contínua para controlar a demanda dos eletropostos.

# Insight 2:
# A distribuição temporal dos dados permite identificar tendências históricas de consumo energético e expansão da eletrificação,
# contribuindo para prever horários de pico e aplicar políticas de tarifação dinâmica no sistema de recarga comercial.

#============================================================================================================================================

df2 = pd.read_csv("World Energy Consumption.csv")

freq_abs2 = df["year"].value_counts().sort_index()
freq_rel2 = (df["year"].value_counts(normalize=True).sort_index()) * 100
freq_acum2 = freq_abs.cumsum()

tabela2 = pd.DataFrame({
    "Frequência Absoluta": freq_abs,
    "Frequência Relativa (%)": freq_rel.round(2),
    "Frequência Acumulada": freq_acum
})

print(tabela2)

# Insight 1:
# Países com maiores valores de PIB tendem a apresentar maior infraestrutura energética e maior potencial de adoção de veículos elétricos,
# indicando mercados mais preparados para implantação de redes inteligentes de recarga.

# Insight 2:
# A concentração da maioria dos países em faixas menores de PIB mostra que
# soluções de gerenciamento automatizado, como o ChargeGrid Intelligence,
# precisam otimizar o consumo de energia e reduzir desperdícios para tornar a recarga comercial economicamente viável em diferentes cenários.