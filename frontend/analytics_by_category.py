import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import altair as alt

API_URL="http://localhost:8000" # this should match with the fastapi sever 


def analytics_by_category_tab():
    col1,col2 =st.columns(2)
    with col1:
        start_date = st.date_input("Start Date",datetime(2024,8,1))
        
    with col2:
        end_date = st.date_input("End Date",datetime(2024,8,5))
    
    if st.button("Get Analytics"):
        payload={
            "start_date":start_date.strftime("%Y-%m-%d"),
            "end_date":end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics_by_category/",json=payload)
        response=response.json()

        data={
            "Category":list(response.keys()),
            "Total":[response[category]["total"] for category in response],
            "Percentage":[response[category]["percentage"] for category in response]
        }

        df= pd.DataFrame({
            "Category":data["Category"],
            "Total":data["Total"],
            "Percentage":data["Percentage"]
        })

        df_sorted=df.sort_values(by="Percentage",ascending=False)
        

        st.title("Expense breakdown by Category")

        bar_chart=alt.Chart(data=df_sorted).mark_bar(size=100).encode(
        x=alt.X('Category',axis=alt.Axis(labelAngle=0)),
        y='Percentage',
        color=alt.value('#d62828')).properties(width=700)
        st.altair_chart(bar_chart)

        #st.bar_chart(data=df_sorted.set_index("Category")["Percentage"],width=0,height=0,use_container_width=True, color="#d62828")

        df_sorted["Total"]=df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"]=df_sorted["Percentage"].map("{:.2f}".format)
        st.table(df_sorted)
    

