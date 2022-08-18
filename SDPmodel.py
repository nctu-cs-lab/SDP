import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import xlwt

file_path = ''
DB_data = pd.read_csv(file_path)
y = DB_data.sum_defects

features = ['AMC', 'Ca', 'CAM', 'CBM', 'CBO', 'CC', 'Ce',
                  'DAM', 'DIT', 'IC', 'LCOM', 'LCOM3', 'LOC',
                  'MFA', 'MOA', 'NOC', 'NPM','RFC']
X = DB_data[features]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)
rf_model = RandomForestRegressor(random_state = 1)
rf_model.fit(train_X, train_y)

rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

rf_model_on_full_data = RandomForestRegressor()
rf_model_on_full_data.fit(X, y)

test_data_path = ''
test_data = pd.read_csv(test_data_path)
test_X = test_data[features]
test_preds = rf_model_on_full_data.predict(test_X)

output = pd.DataFrame({'sum-defects': test_preds})
for i in range():
    output = int(output.iloc[i])
    random.shuffle(output)
    sheet = book.add_sheet('DB'+str(i), cell_overwrite_ok=True)
    count = 0
    for j in output:
        sheet.write(count, 0, j)
        count += 1
book.save(r'../sheet.xls')

print(output)
