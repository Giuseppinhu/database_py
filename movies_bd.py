import pandas as pd

file = 'C:/Users/Giuseppe/Desktop/movies.csv' 
dataframe = pd.read_csv(file)

print("\nOs cinco primeiros da lista de filmes:")
print(dataframe.head())

# Retira todas as linhas vazias
dataframe_limpo = dataframe.dropna()

print("\nRetirando os valores em branco do BD:")
print(dataframe_limpo.head())

dataframe_numerico = dataframe_limpo.select_dtypes(include=['number'])

# Estatísticas descritivas
print("\nTodas as estatístisca do banco de dados:")
print(f"Média:\n{dataframe_numerico.mean()}\n")
print(f"Mediana:\n{dataframe_numerico.median()}\n")
print(f"Desvio padrão:\n{dataframe_numerico.std()}\n")
print(f"Valor mínimo:\n{dataframe_numerico.min()}\n")
print(f"Valor máximo:\n{dataframe_numerico.max()}\n")

# Estátisticas dos filmes
print("\nResumo estatístico (describe):")
print(dataframe_numerico.describe())

input("\n\n\n\nPressione Enter para fechar a aplicação...")
