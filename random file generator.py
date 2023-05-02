import pandas as pd
import numpy as np

# Generate random data for age, gender, and salary
age = np.random.randint(18, 65, size=1000)  #We are having random ages starting from 18 upto 64 1000 entries
gender = np.random.choice(['male', 'female'], size=1000)  #We are having random gender male or female  1000 entries
salary = np.random.randint(10, 200, size=1000)  #We are having random salary starting from 20000 upto 199999  1000 entries

# Create labels for each sample
labels = np.random.choice([0, 1], size=1000)  #This label represents 1 for clicking and 0 for not clicking ad it is gernerated randomly  1000 entries

# Combine the data into a DataFrame
df = pd.DataFrame({'age': age, 'gender': gender, 'salary': salary, 'label': labels}) #We are putting this into a dataframe using pandas library

# Save the data to a CSV file
df.to_csv('ad_data6.csv', index=False)  #we are saving it in a csv file and if index is set to false a seperate index coulmn wont be created
