# Part 2: Enhancement (Cleaning of external dataset)
####################################################
## Importing packages
import pandas as pd
import numpy as np

## Importing data
raw = pd.read_csv('data\output_noshow_raw.csv')
zips = pd.read_csv('data\ZIP_COUNTY_122021.csv')
covid_data = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv') # File contains 2.5 million rows

## Listing datatypes of raw data
raw.dtypes

"""
id                                   int64
patient_id_2                        object
practice_id                          int64
appointment_id                       int64
patient_id                           int64
appointment_date                    object
appointment_start_time              object
appointment_duration                 int64
appointment_type                    object
appointment_status                  object
appointment_date_time               object
appointment_last_modified_date      object
appointment_scheduled_date          object
appointment_yosi_noshow1            object
appointment_yosi_noshow2            object
custom_client                        int64
custom_client_site                   int64
client_site                         object
patient_dob                         object
patient_zipcode_x                   object
patient_gender                      object
patient_age                          int64
data_collect                        object
patient_age_groupper                object
appointment_date_qt                  int64
appointment_date_month               int64
appointment_date_year                int64
appintmentWithin3DayHoliday          int64
appintmentWithin5DayHoliday          int64
appintmentWithin7DayHoliday          int64
appointment_start_time_groupper     object
appointment_start_time_hour          int64
zipcode                             object
weather_conditions                  object
weather_icon                        object
geocode_zip                        float64
geocode_city                        object
geocode_county                      object
geocode_state                       object
geocode_latitude                   float64
geocode_longitude                  float64
geocode_lengthlife                  object
geocode_healthybehaviors            object
geocode_clinicalcare                object
geocode_socioeconomic               object
geocode_physicalenv                 object
dtype: object
"""

## Cleaning zipcode from raw data
raw['zipcode'] = raw['patient_zipcode_x'].str.split('-').str[0]
raw['zipcode'] = raw['zipcode'].astype(str)

## Listing datatypes of zipcode data
zips.dtypes

"""
zip                     int64
county                  int64
usps_zip_pref_city     object
usps_zip_pref_state    object
dtype: object
"""

## Converting variables to string
zips['county'] = zips['county'].astype(str)
zips['zip'] = zips['zip'].astype(str)

## Creating new column for drop
zips = zips.rename(columns={'zip': 'zipcode_pt'})
zips = zips.rename(columns={'county': 'county_fips_pt'})
zips = zips.rename(columns={'usps_zip_pref_city': 'city_pt'})
zips = zips.rename(columns={'usps_zip_pref_state': 'state_pt'})

## Developing a dataframe for merging
df_main = zips[['zipcode_pt', 'county_fips_pt', 'city_pt', 'state_pt']]

## Merging dataframes
df_main_merge = pd.merge(raw, df_main, how = 'left', left_on = ['zipcode'], right_on = ['zipcode_pt'])

## Listing datatypes of covid data
covid_data.dtypes

"""
date       object
county     object
state      object
fips      float64
cases       int64
deaths    float64
dtype: object
"""

## Converting variables to string
covid_data['fips'] = covid_data['fips'].astype(str)
covid_data['cases'] = covid_data['cases'].astype(str)
covid_data['deaths'] = covid_data['deaths'].astype(str)

covid_data['fips'] = covid_data['fips'].str.split('.').str[0]
covid_data['fips'] = covid_data['fips'].astype(str)

covid_data['deaths'] = covid_data['deaths'].str.split('.').str[0]
covid_data['deaths'] = covid_data['deaths'].astype(str)

## Developing a dataframe for merging
df_covid = covid_data[['date', 'fips', 'cases']]

## Merging dataframes
df_covid_merge = df_main_merge.merge(df_covid, how='inner', left_on=['appointment_date', 'county_fips_pt'], right_on=['date', 'fips'])

## Re listing dataypes of MERGE
df_covid_merge.dtypes

"""
id                                   int64
patient_id_2                        object
practice_id                          int64
appointment_id                       int64
patient_id                           int64
appointment_date                    object
appointment_start_time              object
appointment_duration                 int64
appointment_type                    object
appointment_status                  object
appointment_date_time               object
appointment_last_modified_date      object
appointment_scheduled_date          object
appointment_yosi_noshow1            object
appointment_yosi_noshow2            object
custom_client                        int64
custom_client_site                   int64
client_site                         object
patient_dob                         object
patient_zipcode_x                   object
patient_gender                      object
patient_age                          int64
data_collect                        object
patient_age_groupper                object
appointment_date_qt                  int64
appointment_date_month               int64
appointment_date_year                int64
appintmentWithin3DayHoliday          int64
appintmentWithin5DayHoliday          int64
appintmentWithin7DayHoliday          int64
appointment_start_time_groupper     object
appointment_start_time_hour          int64
zipcode                             object (Cleaned zipcode of the patient)
weather_conditions                  object
weather_icon                        object
geocode_zip                        float64
geocode_city                        object
geocode_county                      object
geocode_state                       object
geocode_stusab                      object
geocode_latitude                   float64
geocode_longitude                  float64
geocode_lengthlife                  object
geocode_healthybehaviors            object
geocode_clinicalcare                object
geocode_socioeconomic               object 
zipcode_pt                          object (Zipcode of the patient)
county_fips_pt                      object (County FIPS code of the patient)
city_pt                             object (City of the patient)
state_pt                            object (State of the patient)
date                                object (Date of the appointment)
fips                                object (County FIPS code)
cases                               object (Total cases in the county on the date of the appointment)
dtype: object
"""

## Merging information into master file
df_covid_merge.to_csv('data\master.csv', index=False)



############### Experimental ####################

## Merging dataframes
# df_main_merge = raw.join(df_main.set_index('zipcode_pt'), on='zipcode_pt', how='left')    [Line 94 Origin]
