import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt

st.set_page_config(layout = 'wide', page_title= "Startup Analysis")

# imported cleaned data from jupyter notebook
df = pd.read_csv("Startup_cleaned.csv")
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

def load_overall_analysis():
    st.title("Overall Analysis")
    
    total = round(df['amount'].sum())
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    avg_funding = df.groupby('startup')['amount'].sum().mean()
    total_funded_startups = df['startup'].nunique()
    
    col1,col2,col3,col4 = st.columns(4)
    
    with col1:
        st.metric('Total', str(total) + " Cr")
    with col2:
        st.metric('Max Funding', str(max_funding) + " Cr")
    with col3:
        st.metric('Average Funding', str(round(avg_funding)) + " Cr")
    with col4:
        st.metric('Total Startups', total_funded_startups)
        
    st.header("MoM Graph")
    selected_option = st.selectbox("Select Type", ["Total", "Count"])
    
    if selected_option == 'Total':
        temp_df = df.groupby(['year','month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year','month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + "-" + temp_df['year'].astype('str')
    fig, ax = plt.subplots()
    ax.plot(temp_df['x_axis'],temp_df['amount'])
    st.pyplot(fig)


def load_investor_details(investor):
    st.title(investor)
    
    #load the recent 5 investments of investors
    last5_df  = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']] 
    st.subheader("Most Recent Investments")
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1:
        
        #biggest Investments (bar Graph):
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader("Biggest Investments")
        fig, ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)

    with col2:
        #Sectors investments
        vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader("Invested in Sectors..")
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series,labels=vertical_series.index, autopct= '%0.01f%%')
        st.pyplot(fig1)

    col1, col2 = st.columns(2)
    with col1:
        
        #Rounds investments
        round_series = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
        st.subheader("Invested in rounds..")
        fig3, ax3 = plt.subplots()
        ax3.pie(round_series,labels=round_series.index, autopct= '%0.01f%%')
        st.pyplot(fig3)
        
    with col2:
        #city investments
        city_series = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
        st.subheader("Invested in Cities..")
        fig4, ax4 = plt.subplots()
        ax4.pie(city_series,labels=city_series.index, autopct= '%0.01f%%')
        st.pyplot(fig4)

    
    df['year'] = df['date'].dt.year
    st.subheader("YoY Investements")
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    fig5, ax5 = plt.subplots()
    ax5.plot(year_series.index,year_series.values)
    st.pyplot(fig5)

st.sidebar.title("startup Funding Analysis")

option = st.sidebar.selectbox("Select One", ["Overall Analysis","Startup","Investor"])


# Over-all Analysis
if option == "Overall Analysis":
    load_overall_analysis()


# Startup Analysis
elif option == "Startup":
    startups = sorted(df['startup'].unique().tolist())
    st.sidebar.selectbox("Select Startup", startups)
    btn1 = st.sidebar.button("Find Startup Details")
    st.title("Startup Analysis")


# Investors Analysis
else:
    Investors = sorted(set(df['investors'].str.split(',').sum()))
    selected_investor = st.sidebar.selectbox("Select Investor", Investors)
    btn2 = st.sidebar.button("Find Investor Details")
    
    if btn2:
        load_investor_details(selected_investor)

    

