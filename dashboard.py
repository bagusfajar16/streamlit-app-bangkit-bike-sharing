import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Create function based on EDA Phase
def create_weather_impact (df) :
    weather_impact = df.groupby(by='weathersit').agg({
        'casual' : ['mean', 'min', 'max'],
        'registered' : ['mean', 'min', 'max'],
        'cnt' : ['mean', 'min', 'max']
    })
    return weather_impact

def create_working_day_impact (df) :
    working_day_impact = df.groupby(by='workingday').agg({
        'casual' : ['mean', 'min', 'max'],
        'registered' : ['mean', 'min', 'max'],
        'cnt' : ['mean', 'min', 'max']
    })
    return working_day_impact

def create_month_impact (df) :
    month_impact = df.groupby(by='mnth').agg({
        'casual': ['mean', 'min', 'max'],
        'registered': ['mean', 'min', 'max'],
        'cnt': ['mean', 'min', 'max']
    })
    return month_impact

def create_agg_result (df) :
    agg_result = hour_df.groupby(by='hr').agg({
        'casual': ['mean', 'min', 'max'],
        'registered': ['mean', 'min', 'max'],
        'cnt': ['mean', 'min', 'max']
    })
    return agg_result


#Create sidebar. This is only text
with st.sidebar:
    st.title("Bangkit Academy")
    st.text("Hi, there")
    st.text("I'm Putu Bagus Muhammad Fajar")
    st.text("This is my first streamlit app.")


#Visualize data from day.csv file
day_df = pd.read_csv("day_data.csv")
datetime_columns = ["dteday"]
day_df.sort_values(by="dteday", inplace=True)
day_df.reset_index(inplace=True)
 
for column in datetime_columns:
    day_df[column] = pd.to_datetime(day_df[column])

weather_impact_df = create_weather_impact (day_df)
working_day_impact_df = create_working_day_impact (day_df)
month_impact_df = create_month_impact (day_df)

st.header('Bike-Sharing Dashboard :sparkles:')

tab1, tab2, tab3, tab4 = st.tabs(["Weather Impact", "Working Day Impact", "Month Impact", "Hour Trend"])

with tab1:
    # Plotting first question
    st.subheader('Weather Impact for Bycycle Rental')
    plt.figure(figsize=(5, 14))
    ## Plot untuk Total Users (Cnt)
    plt.subplot(3, 1, 1)
    sns.barplot(x=weather_impact_df.index, y=weather_impact_df['cnt']['mean'], label='Total Users (Mean)')
    plt.title('Total Users (Cnt) Over Time')
    plt.xlabel('Weather Code')
    plt.ylabel('Number of Rental')
    plt.legend()
    ## Layout grafik
    plt.tight_layout()
    st.pyplot()

    with st.expander("See context (weather code)"):
        st.write(
            "- **Weather Code 1:** Clear, Few clouds, Partly cloudy, Partly cloudy\n"
            "- **Weather Code 2:** Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist\n"
            "- **Weather Code 3:** Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds\n"
            "- **Weather Code 4:** Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog"
        )

with tab2:
    # Plotting second question
    st.subheader('Working Day Impact for Bycycle Rental')
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
    ## Plot pertama (Casual Users)
    sns.barplot(x=working_day_impact_df['casual']['mean'], y=working_day_impact_df.index, ax=axes[0], label='Casual Users (Mean)', orient='h')
    axes[0].set_title('Casual Users Over Time')
    axes[0].set_xlabel('Number of Rentals')
    axes[0].set_ylabel('Working Day Index')
    axes[0].legend()
    # Plot kedua (Registered Users)
    sns.barplot(x=working_day_impact_df['registered']['mean'], y=working_day_impact_df.index, ax=axes[1], label='Registered Users (Mean)', orient='h')
    axes[1].set_title('Registered Users Over Time')
    axes[1].set_xlabel('Number of Rentals')
    axes[1].set_ylabel('Working Day Index')
    axes[1].invert_xaxis()
    axes[1].yaxis.set_label_position("right")
    axes[1].yaxis.tick_right()
    axes[1].legend()
    # Layout grafik
    plt.tight_layout()
    st.pyplot()

    with st.expander("See context (working day Index)"):
        st.write(
            "- **Working Day Index 0:** Holiday\n"
            "- **Working Day Index 1:** Working Day\n"
        )

with tab3:
    # Plotting third question
    st.subheader('Month Impact for Bycycle Rental')
    plt.figure(figsize=(5, 10))
    # Plot untuk Total Users (Cnt)
    plt.subplot(3, 1, 2)
    sns.barplot(x=month_impact_df.index, y=month_impact_df['cnt']['mean'], label='Total (Mean)')
    plt.title('Total Users (Cnt) Over Time')
    plt.xlabel('Month')
    plt.ylabel('Number of Rentals')
    plt.legend()
    # Layout grafik
    plt.tight_layout()
    st.pyplot()


# Visualize data from hour.csv
hour_df = pd.read_csv("hour_data.csv")
datetime_columns_hour = ["dteday"]
hour_df.sort_values(by="dteday", inplace=True)
hour_df.reset_index(inplace=True)
 
for hour_column in datetime_columns_hour:
    hour_df[column] = pd.to_datetime(hour_df[column])

agg_result_df = create_agg_result(hour_df)

with tab4:
    # Plotting for forth question
    st.subheader('Hour Grouping Tren for Bycycle Rental')
    plt.figure(figsize=(7, 14))
    plt.subplot(3, 1, 3)
    sns.lineplot(data=agg_result_df['cnt']['mean'], label='Total (Mean)')
    sns.lineplot(data=agg_result_df['cnt']['min'], label='Total (Min)')
    sns.lineplot(data=agg_result_df['cnt']['max'], label='Total (Max)')
    plt.title('Total Users (Cnt)')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Rentals')
    plt.legend()
    # Layout grafik
    plt.tight_layout()
    st.pyplot()