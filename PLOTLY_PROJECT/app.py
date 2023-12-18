import streamlit as st 
import numpy as np
import pandas as pd 
import plotly.express as px  

# importing dataset
df = pd.read_csv('india.csv') 

# converting all the unique state into list and add at the 0 position 'Overall India'
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('Data Visualization of India')
selected_state = st.sidebar.selectbox('Select a state', list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))

plot = st.sidebar.button('Plot graph')

if plot:
    st.text('Size represent primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude',
                                width=1200, height=700, 
                                zoom=3, size_max=40, size=primary, color=secondary,
                                mapbox_style='carto-positron')
        st.plotly_chart(fig, use_container_width=True)
    else:
        # plot for state 
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6, size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700,hover_name='District')

        st.plotly_chart(fig, use_container_width=True)