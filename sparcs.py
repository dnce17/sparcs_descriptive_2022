import pandas as pd
from helpers import *

pd.set_option('display.float_format', lambda x: '%.3f' % x)

# Load in the specific hospital county data
df_suffolk = pd.read_csv('https://health.data.ny.gov/resource/5dtw-tffi.csv?hospital_county=Suffolk&$limit=500000')
df_nassau = pd.read_csv('https://health.data.ny.gov/resource/5dtw-tffi.csv?hospital_county=Nassau&$limit=500000')
df_merged = pd.concat([df_suffolk, df_nassau])

print(len(df_suffolk), len(df_nassau), len(df_merged))

del(df_suffolk)
del(df_nassau)

# DATA CLEANUP
# Remove whitespace, dashes, make lower case, replace space with underscore
df_merged.columns = df_merged.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('_-', '')

# Remove commas from total_charges and total_costs
df_merged.total_charges = df_merged.total_charges.apply(lambda x : x.replace(',',''))
df_merged.total_costs = df_merged.total_costs.apply(lambda x : x.replace(',',''))

# Convert length_of_stay, total_charges, and total_costs to numeric
df_merged['length_of_stay'] = pd.to_numeric(df_merged['length_of_stay'], errors='coerce')
df_merged['total_charges'] = pd.to_numeric(df_merged['total_charges'], errors='coerce')
df_merged['total_costs'] = pd.to_numeric(df_merged['total_costs'], errors='coerce')

# Isolate the county after numeric conversion for easier use
df_nassau = df_merged[df_merged['hospital_county'] == 'Nassau']
df_suffolk = df_merged[df_merged['hospital_county'] == 'Suffolk']

# HANDLE MISSING DATA (Only length of stay has missing data after checking)
# Replace missing vals w/ column's median of the hospital county
df_nassau['length_of_stay'].fillna(df_nassau['length_of_stay'].median(), inplace=True)
df_suffolk['length_of_stay'].fillna(df_suffolk['length_of_stay'].median(), inplace=True)

# # Confirm there is no more missing values
print(df_nassau['length_of_stay'].isna().sum())
print(df_suffolk['length_of_stay'].isna().sum())
print(df_merged['total_charges'].isna().sum())
print(df_merged['total_costs'].isna().sum())

# BASIC DESCRIPTIVE STATISTICS: 
# Nassau's Stats
print(df_nassau.length_of_stay.describe())
print(df_nassau.total_charges.describe())
print(df_nassau.total_costs.describe())

# Suffolk's Stats
print(df_suffolk.length_of_stay.describe())
print(df_suffolk.total_charges.describe())
print(df_suffolk.total_costs.describe())

# EXPLORING CATEGORICAL VARIABLES: Nassau and Suffolk bar plots 
# Age Group
age_group_order = ['0 to 17', '18 to 29', '30 to 49', '50 to 69', '70 or Older']
df_nassau.age_group.value_counts()
create_bar('age_group', df_nassau, 'Age Groups', 'Total', 'Nassau Age Group Distribution', age_group_order)

df_suffolk.age_group.value_counts()
create_bar('age_group', df_suffolk, 'Age Groups', 'Total', 'Suffolk Age Group Distribution', age_group_order)

# Gender
df_nassau.gender.value_counts()
create_bar('gender', df_nassau, 'Gender', 'Total', 'Nassau Gender Distribution')

df_suffolk.gender.value_counts()
create_bar('gender', df_suffolk, 'Gender', 'Total', 'Suffolk Gender Distribution')

# Admission Type
# NOTE: The next section, VISUALIZATION, instructed to create a bar plot for admission_type
# too, but would be the same as the code below. Thus, it was only done here
admission_type_order = ['Newborn', 'Elective', 'Emergency', 'Trauma', 'Urgent', 'Not Available']
df_nassau.type_of_admission.value_counts()
create_bar('type_of_admission', df_nassau, 'Admission Type', 'Total', 'Nassau Admission Type Distribution', admission_type_order)

df_suffolk.type_of_admission.value_counts()
create_bar('type_of_admission', df_suffolk, 'Admission Type', 'Total', 'Suffolk Admission Type Distribution', admission_type_order)

# VISUALIZATIONS
# Histograms for length of stay
create_hist('length_of_stay', df_nassau, 'Length of Stay', 'Count', 'Nassau Length of Stay Distribution', 5)
create_hist('length_of_stay', df_suffolk, 'Length of Stay', 'Count', 'Suffolk Length of Stay Distribution', 5)

# Box plot for total charges
create_broken_axis_box(df_nassau.total_charges, 'Total Charge', 'Charge', 'Nassau Total Charge', 0)
create_broken_axis_box(df_suffolk.total_charges, 'Total Charge', 'Charge', 'Suffolk Total Charge', 0)

# SUMMARY REPORT USE
# How does the total cost vary by age group or type of admission?
create_bar('age_group', df_nassau, 'Age Groups', 'Total Cost', 'Nassau Age Group vs Cost', age_group_order, 'total_costs')
create_bar('age_group', df_suffolk, 'Age Groups', 'Total Cost', 'Suffolk Age Group vs Cost', age_group_order, 'total_costs')

# Used to identify potential trends in admission types alongside the chart for it above
print(df_nassau.type_of_admission.value_counts())
print(df_suffolk.type_of_admission.value_counts())