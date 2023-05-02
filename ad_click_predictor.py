import pandas as pd
from sklearn.linear_model import LogisticRegression
#data5
# Load the dataset from the CSV file
data = pd.read_csv('ad_data5.csv')
data.columns = ['age', 'gender', 'salary', 'label']
# Replace gender with 0 and 1
data.loc[data['gender'] == 'male', 'gender'] = 1
data.loc[data['gender'] == 'female', 'gender'] = 0

# Extract the feature columns and the label column
x = data[['age', 'gender', 'salary']]
y = data['label']

# Create a logistic regression model and fit it to the data
model = LogisticRegression()
model.fit(x.values, y)

# Input data
age = int(input("Enter your age: "))
gender = input("Enter your gender (male/female): ")
salary = float(input("Enter your salary: "))

# Gender label
if gender == 'male':
    gender_encoded = 1
else:
    gender_encoded = 0

# Feature names
x.columns = ['age', 'gender', 'salary']

# Prediction using the loaded model
prediction = model.predict([[age, gender_encoded, salary]])

# Prediction result
# if prediction[0] == 0:
#     print("You are not likely to click the ad.")
if prediction == 0:
    print("You are not likely to click the ad.")
else:
    print("You are likely to click the ad.")

# Print the feature coefficients and intercept
print(model.coef_)
print(model.intercept_)

# Re-fit the model with feature names
model.fit(x.values, y)




#Not:60,m,30;
#Yes:18,f,11;
#yes:53,m,153;
#Not:55,m,60;
#Yes:25,f,80;
#Not:50,f,90;
#Not:39,f,40;
#Not:31,f,22;

# age=55, gender=male, salary=60, label=0
# age=25, gender=female, salary=80, label=1
# age=45, gender=male, salary=120, label=1
# age=30, gender=male, salary=40, label=1
# age=50, gender=female, salary=90, label=0