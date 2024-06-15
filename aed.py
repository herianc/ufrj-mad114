import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def histbox(dados, coluna, xlabel='', ylabel='Frequência', title='', color='steelblue', size=(12, 6), bins=10):

    # Media e quartis
    media = dados[coluna].mean()
    quartis = dados[coluna].quantile([0.25, 0.5, 0.75])

    fig, ax = plt.subplots(2, 1, figsize=size, sharex=True, gridspec_kw={
                           'height_ratios': (0.10, 0.90)})
    plt.subplots_adjust(wspace=0.0, hspace=0.02)

    # Histograma
    sns.histplot(dados, x=coluna, ax=ax[1], color=color, bins=bins)
    ax[0].set_title(title)
    ax[1].axvline(quartis[0.25], color='purple', linestyle='--',
                  linewidth=1, label=f'1º Quartil: {quartis[0.25]:.2f}')
    ax[1].axvline(media, color='red', linestyle='--',
                  linewidth=1, label=f'Média: {media:.2f}')
    ax[1].axvline(quartis[0.5], color='green', linestyle='--',
                  linewidth=1, label=f'Mediana: {quartis[0.5]:.2f}')
    ax[1].axvline(quartis[0.75], color='purple', linestyle='--',
                  linewidth=1, label=f'3º Quartil: {quartis[0.75]:.2f}')
    ax[1].set_xlabel(xlabel)
    ax[1].set_ylabel(ylabel)
    ax[1].legend()

    # Boxplot
    sns.boxplot(dados, x=coluna, ax=ax[0], color=color)
    ax[0].axvline(media, color='red', linestyle='--',
                  linewidth=1, label=f'Média: {media:.2f}')

    fig.show()


def tabela_frequencias(df: pd.DataFrame, coluna: str):
    '''Tabela com as frequências de uma variável qualitativa'''

    frequencias = {'Freq. Absoluta': df[coluna].value_counts(),
                   'Freq. Relativa': df[coluna].value_counts() / df[coluna].count(),
                   'Freq. Abs. Acumulada': df[coluna].value_counts().cumsum(),
                   'Freq. Rel. Acumulada': (df[coluna].value_counts() / df[coluna].count()).cumsum()}

    tabela = pd.DataFrame(frequencias)
    return tabela


def tabela_descritiva(df, coluna):
    '''Tabela com as estatísticas descritivas de uma variável quantitativa'''
    estatisticas = {'Variável': coluna,
                    'Tamanho': df[coluna].count(),
                    'Moda': df[coluna].mode(),
                    'Média': df[coluna].mean(),
                    'Mínimo': df[coluna].min(),
                    '1º Q': df[coluna].quantile(0.25),
                    'Mediana': df[coluna].quantile(0.5),
                    '3º Q': df[coluna].quantile(0.75),
                    'Máximo': df[coluna].max(),
                    'Variância': df[coluna].var(),
                    'Desvio Padrão': df[coluna].std()}

    tabela = pd.DataFrame(estatisticas)
    tabela.set_index('Variável', inplace=True)
    return tabela


def limites_discrepantes(df: pd.DataFrame, coluna: str):
    '''Limites inferior e superior de uma variável quantitativa'''
    q1, q3 = df[coluna].quantile([0.25, 0.75]).values

    DIQ = q3 - q1

    limite_superior = q3 + (1.5 * DIQ)
    limite_inferior = q1 - (1.5 * DIQ)

    return limite_inferior, limite_superior
