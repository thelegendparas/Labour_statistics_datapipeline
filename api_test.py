# Load the packages

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd
import requests
import json
import prettytable
import csv
import os
from dotenv import load_dotenv, dotenv_values
# Insert  API KEY

load_dotenv()

API_KEY = os.getenv("API_KEY")

Quarterly_gross_job_gains = os.getenv("QUARTERLY_GROSS_JOB_GAINS")
Quarterly_gross_job_loss = os.getenv("QUARTERLY_GROSS_JOB_LOSSES")

Employment_lvl = os.getenv("EMPLOYMENT_LVL")
Employment_population_ratio = os.getenv("EMPLOYMENT_POPULATION_RATIO")

Labour_force_participation = os.getenv("LABOR_FORCE_PARTICIPATION_RATE")
Total_avg_weekly_Hrs = os.getenv("TOTAL_AVG_WEEKLY_HRS")
Avg_weekly_earnings = os.getenv("AVG_WEEKLY_EARNINGS")

Avg_hourly_earnings_all_employees = os.getenv("AVG_HOURLY_EARNINGS_ALL_EMPLOYEES")

# Picking the relevant Hyperparameters and series ID
collection = []

collection.append(Quarterly_gross_job_gains)
collection.append(Quarterly_gross_job_loss)

start_year = 2011
end_year = 2022

start_year = str(start_year)
end_year = str(end_year)

# Payload Body

headers = {'Content-type': 'application/json'}

data = json.dumps({
    "seriesid": collection,
    "startyear":start_year,
    "endyear": end_year})

p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)

json_data = json.loads(p.text)

# Clean data

def Quater_year(year: list[int]):
    for i in range(1, len(year)):
        if year[i] != year[i - 1] and (year[i - 1] * 4) % 4 == 3:
            continue
        year[i] = year[i - 1] + 0.25

    return year


def Month_year(year: list[int]):
    for i in range(1, len(year)):
        if year[i] != year[i - 1] and (year[i - 1] * 10) % 10 == 0:
            continue
        year[i] = year[i - 1] + 0.1

    return year


def convert_str_int_list(year: list[str]):
    for i in range(len(year)):
        x = year[i]
        year[i] = int(x)
    return year


if json_data['status'] == "REQUEST_SUCCEEDED":
    # Extraction the year and period data
    year = []
    period = []
    series = json_data['Results']['series'][0]

    for item in series['data']:
        year.append(item['year'])
        period.append(item['period'])
    year.reverse()
    period.reverse()

    if period[0] == "M01":
        spaced_year = Month_year(convert_str_int_list(year))
    else:
        spaced_year = Quater_year(convert_str_int_list(year))

    values = []
    for series in json_data['Results']['series']:
        seriesId = series['seriesID']
        series_data = []
        for item in series['data']:
            series_data.append(item['value'])
        series_data.reverse()
        values.append(series_data)

    # Inserting the value in dictionary
    data = {
        "timestamp": year,
        "period": period
    }
    for i in range(len(collection)):
        data.update({f'{os.getenv(collection[i])}': values[i]})

    df = pd.DataFrame(data)

    df.set_index("timestamp", inplace=True)

    for i in range(len(collection)):
        column = df.columns[1 + i]
        df[column] = pd.to_numeric(df[column], errors="coerce")  # Convert to float
        plt.plot(spaced_year, df[column], marker='o', label=column)

    # Get current axis and set smooth y-axis ticks
    ax = plt.gca()  # Get current axis
    ax.yaxis.set_major_locator(MaxNLocator(nbins=6))  # Controls number of y-axis ticks

    # Customize the plot
    plt.title("Time Series Data")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend(title="Series")
    plt.grid(True)

    # Show the plot
    plt.savefig(f"{os.getenv(collection[0])}.png")

    # Exporting the dataframe into excel
    df.to_csv("out.csv")
