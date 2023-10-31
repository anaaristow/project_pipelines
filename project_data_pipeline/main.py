import pandas as pd
import os
import matplotlib.pyplot as plt 
import seaborn as sns
import src.extraction as ext
import src.transformation as tran
import src.visualization as visu

# extraction.py
url = "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index"
hdi = ext.extraction_url(url)

# transformation.py
df = pd.read_csv("data_set/world_marathon_majors.csv", encoding='ISO-8859-1', sep=';')
df_clean = tran.ajusting_data(df)
df_clean['minutes'] = df_clean['time_race'].apply(tran.minutes)
print(df_clean)
new_df = tran.converting(df_clean)
hdi = pd.read_csv(f"../project_data_pipeline/data_set/hdi_data_set")
total_winners = tran.grouping_winners(df)
combined = tran.combining_data(total_winners, hdi, "Country", "Nation")
combined.to_csv(f'../project_data_pipeline/data_set/combined_data_set')

# visualization.py
df = pd.read_csv("../project_data_pipeline/data_set/data_set_clean", encoding='utf-8', sep=',')
combined = pd.read_csv("../project_data_pipeline/data_set/combined_data_set")
visu.country_marathon(df)
visu.faster(df)
visu.impact_marathon(df)
visu.winners_per_country(df)
visu.winners_hdi(combined, 'Total Winners', 'HDI')
