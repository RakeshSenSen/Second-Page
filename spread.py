import pandas as pd
import streamlit as st
import datetime

st.set_page_config(
     page_title="DATA TEAM",
     page_icon="🧊",
     layout="centered",
     initial_sidebar_state="expanded"
 )


from PIL import Image

col1,col2,col3=st.columns([4,5,3])
with col2:
     st.title('''DATA TEAM''')
with col1:
    pass
with  col3:
     i=Image.open('sen.png')
     st.set_option('deprecation.showPyplotGlobalUse', False)                          #image projection
     st.image(i,use_column_width=None)

idd='1jx3pR8tohqSRc_fPHLbgM8DcaNrAdQNa8tpxosdDezo'
df=pd.read_csv(f"https://docs.google.com/spreadsheets/d/{idd}/export?format=csv")
#st.write('''Hello''')
#st.dataframe(df)

df['Start date']=pd.to_datetime(df['Start date']).dt.date
df['Submitted date']=pd.to_datetime(df['Submitted date']).dt.date                 #Date column conversion to date time



search = st.sidebar.date_input("Enter Start Date",datetime.date(2021, 1, 1))
search0=pd.to_datetime(search)
search=df.loc[(df['Start date']==search0)]

search1=st.sidebar.date_input("Enter End Date",datetime.date(2022, 1, 30))
search10=pd.to_datetime(search1)
search1=df.loc[df['Start date']==search10]

df1=df[df['Start date'].between(search0,search10)]



#st.write("Data as per the Start Date and End Date")
btt=st.sidebar.button('DATA AS PER DATE')
if btt:
    st.write("Data as per the Start Date and End Date")
    st.write(df1)

try:
    tip1=st.sidebar.text_input("ENTER THE DEPARTMENT")
    tip=tip1.split(",")
    dtf=df1['Departments'].isin(tip)
    dtf=df1[dtf]
    

except Exception as e:
    print(e)
if tip1:
    st.write("Data as per the Departments")
    st.dataframe(dtf)

try:
    tic=st.sidebar.text_input("ENTER THE TICKET NUMBER")
    tif=tic.split(",")
    dtf1=df['Ticket number'].isin(tif)
    dtf1=df[dtf1]
except Exception as e:
    print(e)
if tic:
    st.write("Data as per the Ticket Number")
    st.dataframe(dtf1)

