

import streamlit as st
import pandas as pd


df = pd.read_csv(r"C:\Users\USER\Desktop\Computer Practice\Excel Web Application\World-Happiness-Report-2022")
df.head()


st.title("World Happiness Index 2022")

st.sidebar.title("World Happiness Index 2022")

st.image("https://images.pexels.com/photos/5560532/pexels-photo-5560532.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", caption='World Happiness Dataset')


# Create a select box widget that can be used to filter the country and a slider to filter the ladder score in the sidebar as an example.

#Country Select Filter
country_list = ["All","Western Europe", "South Asia", "Southeast Asia", "East Asia", "North America and ANZ","Middle East and North Africa", "Latin America and Caribbean","Central and Eastern Europe","Commonwealth of Independent States","Sub-Saharan Africa"]
select = st.sidebar.selectbox('Filter the region here:', country_list, key='1')

if select =="All":
    filtered_df = df
else:
    filtered_df = df[df['Regional indicator']==select]
        
    
#Ladder Score Slider
score = st.sidebar.slider('Select min Happiness Score', min_value=5, max_value=10, value = 10) # Getting the input.


# Filtering the dataframe.
df = df[df['Happiness score'] <= score] 


#Line Chart
st.line_chart(data=None, width=0, height=0, use_container_width=True)
#Area Chart
st.area_chart(data=None, width=0, height=0, use_container_width=True)

#ScatterBar and Bar Chart
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

#Scatter Chart
fig = px.scatter(filtered_df, x="Explained by: GDP per capita", y="Explained by: Healthy life expectancy", size="Happiness score", color="Regional indicator", hover_name="Country", size_max=10)
st.write(fig)

#Bar Chart, you can write in this way too
st.write(px.bar(filtered_df, y='Happiness score', x='Country'))

#Seaborn Heatmap
#correlate data
corr = filtered_df.corr()

#using matplotlib to define the size
plt.figure(figsize=(8, 8))

#creating the heatmap with seaborn
fig1 = plt.figure()
ax = sns.heatmap(corr,
vmin=-1, vmax=1, center=0,
cmap=sns.diverging_palette(20, 220, n=200),
square=True
)
ax.set_xticklabels(
ax.get_xticklabels(),
rotation=45,
horizontalalignment='right'
);
st.pyplot(fig1)