import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# 1
df = pd.read_csv('FreeCodeCamp - Python Couse/medical_examination.csv')

# 2
df['overweight'] = ((df['weight'] / ((df['height']/100) ** 2)) > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    df_cat = df_cat.value_counts(['cardio', 'variable', 'value']).reset_index(name='total')

    # 7
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar')

    # 8
    fig = fig.fig

    # 9
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # Limpeza dos dados
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]
    # Matriz de correlação
    corr = df_heat.corr()
    # Máscara para triângulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # Figura
    fig, ax = plt.subplots(figsize=(12, 8))
    # Heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, vmax=0.3, vmin=-0.1, square=True, linewidths=0.5, cbar_kws={"shrink": 0.5})
    fig.savefig('heatmap.png')
    return fig


# Executar as funções automaticamente
if __name__ == "__main__":
    print("Gerando gráfico categórico...")
    draw_cat_plot()
    print("Gráfico categórico salvo como 'catplot.png'")
    
    print("Gerando mapa de calor...")
    draw_heat_map()
    print("Mapa de calor salvo como 'heatmap.png'")
    
    print("Visualizações concluídas!")
