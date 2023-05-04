# Ad-click-prediction
Ad click prediction with 3 parameters age, gender and salary

This is the plot for salary vs age for the csv file


![Figure_1](https://user-images.githubusercontent.com/114865522/235683724-0a345d83-1ae4-405d-9d2f-d7dff80fd400.png)

ALGORITHM:
1. Import the required libraries: pandas and LogisticRegression from sklearn.linear_model
2. Load the dataset from the CSV file using pandas read_csv method
3. Replace the categorical values 'male' and 'female' in the 'gender' column with numerical values using pandas replace method
4. Extract the feature columns 'age', 'gender', and 'salary' and the label column 'label' from the dataset and assign them to X and y variables respectively
5. Create a logistic regression model using LogisticRegression() method and fit the model to the data using fit() method on the model object with X and y as inputs
6. Collect user data for 'age', 'gender', and 'salary' using input() method
7. Preprocess the user data by encoding 'gender' value as 1 if 'male' and 0 if 'female'
8. Set column names for X using X.columns method
9. Make a prediction using the loaded model by calling predict() method on the model object with the user data as input
10. Display the prediction result to the user using if-else statement
11. Print the feature weights and intercept values used by the model using coef_ and intercept_ methods on the model object
12. Set the column names for X and re-fit the model with the feature names using fit() method on the model object with X and y as inputs.

The given code is an example of a classification problem using logistic regression. The code fits a logistic regression model to the training data and uses it to predict the label.
