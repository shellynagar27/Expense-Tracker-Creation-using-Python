import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import altair as alt

API_URL="http://localhost:8000" # this should match with the fastapi sever 


def analytics_by_month_tab():
    response = requests.get(f"{API_URL}/analytics_by_month/")
    response=response.json()

    data={
        "Month":list(response.keys()),
        "Total Expenditure":[response[month]["total_expenditure"] for month in response],
        "Percentage":[response[month]["percentage"] for month in response]
    }

    df= pd.DataFrame({
        "Month":data["Month"],
        "Total Expenditure":data["Total Expenditure"],
        "Percentage":data["Percentage"]
    })

    # df_sorted=df.sort_values(by="Percentage",ascending=False)

    st.title("Expense breakdown by Month")
    bar_chart=alt.Chart(data=df).mark_bar(size=100).encode(
        x=alt.X('Month',axis=alt.Axis(labelAngle=0)),y='Total Expenditure',
        color=alt.value('#d62828')).properties(width=800)
    st.altair_chart(bar_chart)
    #st.bar_chart(data=df.set_index("Month")["Total Expenditure"],width=0,height=0,use_container_width=True, color="#d62828")

    df["Total Expenditure"]=df["Total Expenditure"].map("{:.2f}".format)
    df["Percentage"]=df["Percentage"].map("{:.2f}".format)
    st.table(df)


