import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Load the data
file_path = ''
DB_data = pd.read_csv(file_path)
y = DB_data.sum_defects

features = ['CAM','Ce','NOC','RFC','WMC', 'LCOM', 'LCOM3', 'LOC']
X = DB_data[features]

# Select columns corresponding to features, and preview the data
X = DB_data[features]

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# Define a random forest model
rf_model = RandomForestRegressor(random_state = 1)
rf_model.fit(train_X, train_y)

rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)
print("Validation MAE for Random Forest Model: {:,.0f}".format(rf_val_mae))

rf_model_on_full_data = RandomForestRegressor()

# fit rf_model_on_full_data on all data from the training data
rf_model_on_full_data.fit(X, y)

# path to file you will use for predictions
test_data_path = '../Project-SDP model/Data/JIRA test set/JIRA-test set-no sum.csv'
test_data = pd.read_csv(test_data_path)
test_X = test_data[features]
test_preds = rf_model_on_full_data.predict(test_X)

# Run the code to save predictions in the format used for competition scoring
output = pd.DataFrame({'sum-defects': test_preds})
output.to_csv('submission.csv', index = False)

print(output)
