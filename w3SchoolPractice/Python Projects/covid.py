import pandas as pd

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv'
covid_data = pd.read_csv(url)

print(covid_data.columns)

if 'Country/Region' in covid_data.columns:
    group_col = 'Country/Region'
elif 'Country_Region' in covid_data.columns:
    group_col = 'Country_Region'
else:
    raise ValueError("The column for country/region is missing in the dataset.")

data = covid_data.groupby(group_col)[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()

result = data[data['Deaths'] > 0][[group_col, 'Deaths']]
print(result)
