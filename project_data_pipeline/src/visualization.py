import pandas as pd
import os
import matplotlib.pyplot as plt 
import seaborn as sns

def country_marathon(data_frame):
        colors = ["#440154", "#482777", "#3E4989", "#31688E", "#26838F", "#1F9D95", "#22B16C", "#43C555", "#7AD151", "#AAD946", "#D4EE00"]
        plt.figure(figsize=(14, 8))
        plt.pie((data_frame["marathon"].value_counts()).values, 
        labels = (data_frame["marathon"].value_counts()).index,
        autopct='%1.1f%%', startangle=140,colors=colors)
        plt.title('Major Marathons')
        plt.savefig(f'../project_data_pipeline/images/country_marathon.png')
        os.system(f"open images/country_marathon.png")

def faster(data_frame):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='year', y='minutes', hue='gender', 
    data=data_frame, palette='viridis', errorbar=None)
    plt.xticks(rotation=90)
    plt.xlabel('Year')
    plt.ylabel('Minutes')
    plt.title('Minutes to complete the race per year')
    plt.savefig(f'../project_data_pipeline/images/faster.png')
    os.system(f"open images/faster.png")

def impact_marathon(data_frame):
    fast = data_frame.groupby(["marathon", "gender"]).agg({"minutes":min}).reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(data=fast, x='marathon', y='minutes', hue='gender', palette='viridis')
    plt.xlabel('Marathon')
    plt.ylabel('Minutes')
    plt.title('Histogram of Marathon Times by Gender')
    plt.xticks(rotation=90)
    plt.savefig(f'../project_data_pipeline/images/impact_marathon.png')
    os.system(f"open images/impact_marathon.png")


def winners_per_country(data_frame):
    country = data_frame["country"].value_counts(dropna=False) 
    country_10 = country.index[:10].values
    data_frame["country_10"] = data_frame["country"].where(data_frame["country"].isin(country_10), 
                        "Other") 
    colors = ["#440154", "#482777", "#3E4989", "#31688E", "#26838F", "#1F9D95", "#22B16C", "#43C555", "#7AD151", "#AAD946", "#D4EE00", "#FFFF7E"]
    plt.figure(figsize=(14, 8))
    plt.pie((data_frame["country_10"].value_counts()).values, 
            labels = (data_frame["country_10"].value_counts()).index,
            autopct='%1.1f%%', startangle=140,
            colors=colors)
    plt.title('Winners vs Country')
    plt.savefig(f'../project_data_pipeline/images/winners_per_country.png')
    os.system(f"open images/winners_per_country.png")

def correlation(data_frame, column1, column2):
    corr = round( (data_frame[column1].corr(data_frame[column2])), 5)
    print(f'The correlation between {column1} and {column2} is: {corr}')
    correlation_matrix = data_frame[[column1, column2]].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(data=correlation_matrix, annot=True, cmap="viridis")
    plt.title(f'Correlation heatmap between {column1} and {column2}')
    plt.savefig(f'../project_data_pipeline/images/correlation_winners_HDI.png')
    os.system(f"open images/correlation_winners_HDI.png")

def winners_hdi(data_frame, column1, column2):
    plt.figure(figsize=(8, 6))
    plt.scatter(data_frame[column1][:15], data_frame[column2][:15], marker='o', color="#440154")
    for i, row in data_frame[:15].iterrows():
        plt.text(row[column1], row[column2], row['Country'], fontsize=8, ha='center', va='bottom')
    plt.scatter(data_frame[column1][15:], data_frame[column2][15:], marker='o', color="#440154")
    plt.xlabel('Total Winners')
    plt.ylabel('HDI')
    plt.title('Total Winners vs HDI')
    plt.savefig(f'../project_data_pipeline/images/scatter_winners_HDI.png')
    os.system(f"open images/scatter_winners_HDI.png")