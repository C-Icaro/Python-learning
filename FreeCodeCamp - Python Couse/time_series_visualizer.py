import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Importando CSV
df = pd.read_csv('FreeCodeCamp - Python Couse/fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Limpa os dados
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def desenhar_grafico_linha():
    # Desenha o grafico de linha
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    ax.set_title('Visualizações Diárias da Página do Fórum freeCodeCamp 5/2016-12/2019')
    ax.set_xlabel('Data')
    ax.set_ylabel('Visualizações da Página')
    
    # Salva a figura
    fig.savefig('grafico_linha.png')
    return fig

def desenhar_grafico_barras():
    # Cria gráfico de barras mensais
    df_bar = df.copy()
    df_bar['ano'] = df_bar.index.year
    df_bar['mes'] = df_bar.index.month
    df_bar = df_bar.groupby(['ano', 'mes'])['value'].mean().unstack()
    
    # Desenha o gráfico de barras
    fig = df_bar.plot(kind='bar', figsize=(12, 6)).figure
    plt.xlabel('Anos')
    plt.ylabel('Visualizações Médias da Página')
    plt.legend(title='Meses', labels=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
    
    # Salva a figura
    fig.savefig('grafico_barras.png')
    return fig

def desenhar_grafico_caixa():
    # Cria o gráfico de caixa
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['ano'] = [d.year for d in df_box.date]
    df_box['mes'] = [d.strftime('%b') for d in df_box.date]

    # Desenha o gráfico o de caixa usando Seaborn
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))
    
    # Desenha o grafico de caixa por ano usando boxplot do matplotlib em vez do seaborn
    anos = df_box['ano'].unique()
    dados_anos = [df_box[df_box['ano'] == ano]['value'].values for ano in sorted(anos)]
    axes[0].boxplot(dados_anos, labels=sorted(anos))
    axes[0].set_title('Gráfico de Caixa por Ano (Tendência)')
    axes[0].set_xlabel('Ano')
    axes[0].set_ylabel('Visualizações da Página')
    
    ordem_meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    dados_meses = [df_box[df_box['mes'] == mes]['value'].values for mes in ordem_meses]
    axes[1].boxplot(dados_meses, labels=ordem_meses)
    axes[1].set_title('Gráfico de Caixa por Mês (Sazonalidade)')
    axes[1].set_xlabel('Mês')
    axes[1].set_ylabel('Visualizações da Página')
    
    # Salva a figura
    fig.savefig('grafico_caixa.png')
    return fig

# Executar as funções automaticamente (Teste do freecode camp)
if __name__ == "__main__":
    print("Gerando gráfico de linha...")
    desenhar_grafico_linha()
    print("Gráfico de linha salvo como 'grafico_linha.png'")
    
    print("Gerando gráfico de barras...")
    desenhar_grafico_barras()
    print("Gráfico de barras salvo como 'grafico_barras.png'")
    
    print("Gerando gráficos de caixa...")
    desenhar_grafico_caixa()
    print("Gráficos de caixa salvos como 'grafico_caixa.png'")
    
    print("Todas as visualizações foram concluídas!")