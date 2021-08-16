#%%
import pandas as pd 
import matplotlib
import seaborn as sns 
import matplotlib.pyplot as plt 
import plotly.express as px
fruit_df = pd.read_excel('Fruit customer research.xlsx')
fruit_df
fruit_df.isna().sum()
del fruit_df['Unnamed: 11']
del fruit_df['Unnamed: 12']
del fruit_df['Unnamed: 13']
fruit_df['Age range'].unique()
def null_values_gh(Data):
    plt.figure(figsize=(12,6))
    plt.title('Null _Values')
    sns.heatmap(Data.isna(),cmap="YlGnBu")
# null_values_gh(fruit_df)   
def Counter(data,col_name):
    dt_count=data[col_name].value_counts()
    return dt_count
def gh_count(var,title):
    plt.title('{}'.format(title))
    sns.barplot(x=var,y=var.index)    
def px_gh(v):
   return px.bar(x=v.index,y=v)
def pie_gh(v):
   plt.figure(figsize=(12,6))
   plt.pie(v,labels=v.index,autopct='%1.1f%%', startangle=180);

Age_range_ct = Counter(fruit_df,'Age range')    
Age_range=gh_count(Age_range_ct,'Age Range')
Frequence_ct = Counter(fruit_df,'Frequence')
frequence =px_gh(Frequence_ct)
Type_ct = Counter(fruit_df,'Type')    
Type = px_gh(Type_ct)
Online_channel_ct = Counter(fruit_df,'Online channel').head(10)
Online_channel=pie_gh(Online_channel_ct)
