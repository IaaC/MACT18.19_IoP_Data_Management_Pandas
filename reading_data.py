
# license: Creative Commons License
# Title: Data management with pandas www.iaac.net
# Created by: Diego Pajarito
#
# is licensed under a license Creative Commons Attribution 4.0 International License.
# http://creativecommons.org/licenses/by/4.0/
# This script uses pandas for data management for more information visit; pandas.pydata.org/
# This script uses geopandas for data management for more information visit; geopandas.org/

import pandas as pd
import matplotlib.pyplot as plt

# Read a csv file
tweets = pd.read_csv('data/tweets.csv')

# Basic plots
tweets.plot()                                       # plots all columns against index
tweets.plot(kind='scatter', x='lon', y='lat')       # scatter plot
tweets.plot(x='timestamp_ms', y='user_followers_count')       # scatter plot
tweets['timestamp_ms'].plot.hist(bins=400)          # histogram per timestamp
tweets['user_followers_count'].plot.hist(bins=1000) # histogram per user follower count
tweets.plot.bar(x='language')                       # bar chart with

# Groups and counts
pd.value_counts(tweets['source']).plot.bar()
pd.value_counts(tweets['language']).plot.bar()

# new columns based on values
tweets['geo'] = 'false'                             # create a new column
tweets.loc[tweets['lon'] > 0, 'geo'] = 'true'       # calculate for the new column based on existing values

geo_count = pd.value_counts(tweets['geo'])
geo_count.plot(kind='bar')

plot_geo = tweets['geo'].value_counts().plot(kind='bar')
plot_geo.set_xlabel('geo')
plot_geo.set_ylabel('tweets')
plt.show()




