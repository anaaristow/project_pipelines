import pandas as pd


def extraction_url(url):
    table = pd.read_html(url, match='Rank')[0]
    columns = ['Nation','HDI']
    table = table.loc[:, columns].iloc[:, :2]
    table.columns = columns
    df = pd.DataFrame(table)
    return df
