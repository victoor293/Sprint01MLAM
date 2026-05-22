# Anna Karla Rorato Albino - RM: 569604
# Arthur Araujo Massarioli - RM: 573308
# Beatriz da Siva Araújo - RM: 570619
# Daniel Alejandro Pupo Martínez - RM: 573075
# Victor Hugo Lavaqui - RM: 573838
# Wendel Pedro Rezende - RM: 573126

import pandas as pd


df = pd.read_csv("/content/World_Energy_Consumption.csv")


freq_abs = df["year"].value_counts().sort_index()
freq_rel = (df["year"].value_counts(normalize=True).sort_index()) * 100
freq_acum = freq_abs.cumsum()


tabela = pd.DataFrame({
    "Absoluta": freq_abs,
    "Relativa (%)": freq_rel.round(2),
    "Acumulada": freq_acum
})

print("=== Tabela 1: year (Discreta) ===")
print(tabela)

# Insight 1:
# O aumento da quantidade de registros nos anos mais recentes indica crescimento da coleta e monitoramento de dados energéticos, algo essencial
# para plataformas inteligentes como o ChargeGrid Intelligence, que dependem de análise contínua para controlar a demanda dos eletropostos.

# Insight 2:
# A distribuição temporal dos dados permite identificar tendências históricas de consumo energético e expansão da eletrificação,
# contribuindo para prever horários de pico e aplicar políticas de tarifação dinâmica no sistema de recarga comercial.

#============================================================================================================================================

gdp_valido = df["gdp"].dropna()

# Divide em 10 faixas (intervalos de classe) com pd.cut
tabela_continua = pd.cut(gdp_valido, bins=10).value_counts().sort_index()
freq_abs2 = tabela_continua
freq_rel2 = (tabela_continua / tabela_continua.sum() * 100).round(2)
freq_acum2 = freq_abs2.cumsum()

tabela_gdp = pd.DataFrame({
    "Absoluta": freq_abs2,
    "Relativa (%)": freq_rel2,
    "Acumulada": freq_acum2
})

print("\n=== Tabela 2: gdp (Contínua) ===")
print(tabela_gdp)

# Insight 1:
# Países com maiores valores de PIB tendem a apresentar maior infraestrutura energética e maior potencial de adoção de veículos elétricos,
# indicando mercados mais preparados para implantação de redes inteligentes de recarga.

# Insight 2:
# A concentração da maioria dos países em faixas menores de PIB mostra que
# soluções de gerenciamento automatizado, como o ChargeGrid Intelligence,
# precisam otimizar o consumo de energia e reduzir desperdícios para tornar a recarga comercial economicamente viável em diferentes cenários.
