import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

try:
    # Configurações de estilo para os gráficos
    plt.style.use('seaborn-v0_8')
    sns.set_theme()

    # Criando diretório para os gráficos se não existir
    if not os.path.exists('graficos'):
        os.makedirs('graficos')

    # Lendo o arquivo CSV
    print("Lendo o arquivo CSV...")
    df = pd.read_csv('cancelamentos_sample.csv')

    # Função para criar e salvar gráficos
    def salvar_grafico(plt, nome_arquivo):
        try:
            plt.tight_layout()
            plt.savefig(os.path.join('graficos', f'{nome_arquivo}.png'))
            plt.close()
            print(f"Gráfico salvo: {nome_arquivo}.png")
        except Exception as e:
            print(f"Erro ao salvar gráfico {nome_arquivo}: {str(e)}")

    # Análise básica dos dados
    print("\nInformações do Dataset:")
    print(df.info())

    print("\nPrimeiras 5 linhas do Dataset:")
    print(df.head())

    print("\nEstatísticas descritivas:")
    print(df.describe())

    # Análise de valores ausentes
    print("\nValores ausentes por coluna:")
    print(df.isnull().sum())

    # Análise de correlação (apenas para colunas numéricas)
    print("\nGerando mapa de correlação para variáveis numéricas...")
    colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns
    plt.figure(figsize=(12, 8))
    sns.heatmap(df[colunas_numericas].corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Correlação entre Variáveis Numéricas')
    salvar_grafico(plt, 'correlacao')

    # Distribuição das variáveis numéricas
    print("\nGerando gráficos de distribuição para variáveis numéricas...")
    for coluna in colunas_numericas:
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x=coluna, kde=True)
        plt.title(f'Distribuição de {coluna}')
        salvar_grafico(plt, f'distribuicao_{coluna}')

    # Análise de cancelamentos por diferentes categorias
    print("\nGerando gráficos de cancelamento por categorias...")
    colunas_categoricas = df.select_dtypes(include=['object']).columns
    for coluna in colunas_categoricas:
        plt.figure(figsize=(12, 6))
        cancelamento_por_categoria = df.groupby(coluna)['cancelou'].mean()
        cancelamento_por_categoria.plot(kind='bar')
        plt.title(f'Taxa de Cancelamento por {coluna}')
        plt.xlabel(coluna)
        plt.ylabel('Taxa de Cancelamento')
        plt.xticks(rotation=45)
        salvar_grafico(plt, f'cancelamento_{coluna}')

        # Adicionar contagem por categoria
        plt.figure(figsize=(12, 6))
        df[coluna].value_counts().plot(kind='bar')
        plt.title(f'Distribuição de {coluna}')
        plt.xlabel(coluna)
        plt.ylabel('Quantidade')
        plt.xticks(rotation=45)
        salvar_grafico(plt, f'distribuicao_categoria_{coluna}')

    print("\nAnálise concluída com sucesso! Os gráficos foram salvos no diretório 'graficos'.")

except Exception as e:
    print(f"\nErro durante a execução: {str(e)}")
    sys.exit(1) 