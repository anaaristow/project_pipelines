import pandas as pd


def ajusting_data(df):
    df = df.dropna(axis=1, how='all')
    df['date'] = df['time'].str.extract(r'(\d{2}/\d{2}/\d{4})')
    df['time_race'] = df['time'].str.extract(r'(\d{2}:\d{2})')
    return df

def minutes(time):
    time_str = str(time)
    parts = time_str.split(':')
    if len(parts) == 2:
        hours, minutes = map(int, parts)
        return hours * 60 + minutes
    else:
        return 0


def converting (data_frame):
    data_frame.to_csv('../project_data_pipeline/data_set/data_set_clean')
    return "converted in a data fram"

def grouping_winners(data_frame):
    # Creating a subset with the nationality and the total of winners
    total_winners = data_frame['country'].value_counts().reset_index()
    total_winners.columns = ['Country', 'Total Winners']
    # Getting the percentage
    total_winners['Percentage'] = ((total_winners['Total Winners'] / total_winners['Total Winners'].sum()) * 100).round(2).astype(str) + '%'
    return total_winners

def combining_data(data_set1, data_set2, column1, column2):
    # Combininf data_set1 with data_set2 on the column1 and column2
    combined = data_set1.merge(data_set2, left_on=f'{column1}', right_on=f'{column2}')
    combined = combined[['Country', 'Total Winners', 'Percentage', 'HDI']]
    return combined
