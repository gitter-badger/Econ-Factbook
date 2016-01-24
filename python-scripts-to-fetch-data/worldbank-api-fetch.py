# http://wbdata.readthedocs.org/en/latest/
# http://wbdata.readthedocs.org/en/latest/fetcher.html

import wbdata
import datetime
import pandas as pd

'''
This wbdata is an interactive console to work with World Bank's API.
You can run wbdata.get_source() to see all sources of information and the
respective numbers to run in the below code to fetch the data.
Also, using Pandas package may facilitate the task to convert the lists and dictionaries
retrieved from the API.

Total Population -> source=16
'''

#wbdata.get_source()
wbdata.get_indicator(source=16)

# Define time range to search for data
data_date = (datetime.datetime(1960, 1, 1), datetime.datetime(2014, 1, 1))

# Store the data as the variable df
df = pd.DataFrame(wbdata.get_data("SP.POP.TOTL", pandas = True, data_date=data_date))

# Write it to a CSV - Exemple in /data-pipeline
df.to_csv ("YOURPATH/population_total_1960-2014.csv", sep = ',')
