import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, SimpleRNN, Input, concatenate
from tensorflow.keras.optimizers import Adam

df = pd.read_csv(r'C:\Users\kunal\Downloads\updatedcodetable\input_all_para23.csv')
# current_dir = os.getcwd()
# file_path =current_dir+'\Desktop\kunalAyush\input_all_para23.csv'
# df = pd.read_csv(file_path)
df.head()
df = df.drop('Day Number', axis=1)
df

df.fillna(0, inplace=True)
df.info()



X_percentages = df.iloc[:,0:14]
X_percentages.head()

X_percentages = X_percentages.drop('BENGA M', axis=1)
X_percentages = X_percentages.drop('benga high ash', axis=1)
X_percentages
# file_path=current_dir +'\Desktop\kunalAyush\input_features23.csv'
r=pd.read_csv(r'C:\Users\kunal\Downloads\updatedcodetable\input_features23.csv')
# r=pd.read_csv(file_path)
r
r = r.set_index(r.columns[0])
r.columns = range(len(r.columns))
r.index = range(len(r))



mk = pd.DataFrame(index=X_percentages.index, columns=r.columns)
mk

X_percentages = X_percentages.astype(float)  
r = r.astype(float)




for i, row_X in X_percentages.iterrows():
  
    for col_name in r.columns:
       
        col_r = r[col_name].values  

       
        mk.at[i, col_name] = np.sum(row_X.values * col_r)

        
mk


X_sequences = df.iloc[:,14:30]
X_sequences.head()

percentage_columns = mk
sequential_data =X_sequences

scaler_per = MinMaxScaler()
percentage_columns = scaler_per.fit_transform(percentage_columns)

scaler_seq = MinMaxScaler()
seq_columns = scaler_seq.fit_transform(sequential_data)
# file_path=current_dir+'\Desktop\kunalAyush\output23.csv'
Y = pd.read_csv(r'C:\Users\kunal\Downloads\updatedcodetable\output23.csv')
# Y=pd.read_csv(file_path)

print(Y.shape)



Y

Y = Y.drop('Days Number', axis=1)

y = np.array(Y)
X_percentage_train, X_percentage_test, X_seq_train, X_seq_test, y_train, y_test = train_test_split(
    percentage_columns, seq_columns, y, test_size=0.2, random_state=42
)

from keras.layers import Input, Dense, SimpleRNN, GRU,  concatenate, Reshape
from keras.models import Model
from keras.optimizers import Adam

percentage_input = Input(shape=(12,))
sequential_input = Input(shape=(15,))


x = Dense(128, activation='relu')(percentage_input)
x = Dense(64, activation='relu')(x)
x = Dense(1, activation='relu')(x)


input_percentage = Reshape((15, 1))(sequential_input)

x_reshaped = Reshape((1, 1))(x)

combined = concatenate([x_reshaped, input_percentage],axis=1)


yhat = SimpleRNN(128, activation='relu', return_sequences=False)(combined)
yhat = Dense(64, activation='relu')(yhat)
yhat=Dense(64, activation='relu')(yhat)
yhat = Dense(9, activation='linear')(yhat)  

model = Model(inputs=[percentage_input, sequential_input], outputs=yhat)
model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error', metrics=['accuracy'])
model.summary()


history = model.fit([X_percentage_train, X_seq_train], y_train, epochs=50, batch_size=32, validation_data=([X_percentage_test, X_seq_test], y_test), verbose=0)


import matplotlib.pyplot as plt


plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Validation'], loc='upper right')
plt.show()



plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'], loc='lower right')
plt.show()


import numpy as np
import pandas as pd


predictions_list = []


for i in range(len(X_percentage_train)):  
    data1 = np.array(X_percentage_train[i, :]).reshape(1,-1)  
    data2 = np.array(X_seq_train[i, :]).reshape(1,-1)        
   

    y_pred = model.predict([data1, data2])
  
    predictions_list.append(y_pred.flatten())
    


y_output = pd.DataFrame(predictions_list, columns=[f'{i }' for i in range(predictions_list[0].shape[0])])


y_output


y_train_2 = pd.DataFrame(y_train, columns=[
    '0', '1', '2', '3', '4', '5', '6', '7', '8'
])


actual_output_train = pd.DataFrame(y_train_2)
predicted_output_train = pd.DataFrame(y_output)

y_train_2_list = [y_train_2[col].to_numpy() for col in y_train_2.columns]
y_output_list = [y_output[col].to_numpy() for col in y_output.columns]


result_list = []

for i in range(len(y_train_2_list)):
    result_list.append(((y_train_2_list[i] - y_output_list[i])*100 / y_train_2_list[i]).round(2))


result_df = pd.DataFrame({col: result_list[i] for i, col in enumerate(y_train_2.columns)})

frames=[]
for i in range(len(actual_output_train)):
    current_row_df = pd.DataFrame({'Actual': actual_output_train.iloc[i], 
                                    'Predicted': predicted_output_train.iloc[i], 
                                    'Error': result_df.iloc[i]}).transpose()
    frames.append(current_row_df)


train_error_file = pd.concat(frames, ignore_index=True)
new_columns = {'0': 'Ash', '1': 'VM','2':'Moisture', '3': '80','4':	'-25','5':'CSR'	,'6': 'CRI','7': 'M40','8':'M10'}
train_error_file.rename(columns=new_columns, inplace=True)
train_error_file = train_error_file.transpose()
column_mapping = {}
for i in range(280):
    day_number = (i // 3) + 1 
    if(i%3==0) :column_mapping[i]=f'day {day_number} Actual'
    elif(i%3==1) :column_mapping[i]=f'day {day_number} Predicted'
    else: column_mapping[i]=f' day {day_number} Error'

train_error_file.rename(columns=column_mapping, inplace=True)



train_error_file=train_error_file.transpose().round(2)
# file_path = 'train_error_file.csv'
# train_error_file.to_csv(file_path, index=True)



import numpy as np
import pandas as pd


predictions_list = []



for i in range(len(X_percentage_test)):  
    data1 = np.array(X_percentage_test[i, :]).reshape(1,-1)  
    data2 = np.array(X_seq_test[i, :]).reshape(1,-1)         
    

    y_pred = model.predict([data1, data2])
   
    predictions_list.append(y_pred.flatten())
    


y_output = pd.DataFrame(predictions_list, columns=[f'{i}' for i in range(predictions_list[0].shape[0])])


y_output



y_test_2 = pd.DataFrame(y_test, columns=[
    '0', '1', '2', '3', '4', '5', '6', '7', '8'
])


y_test_2


actual_output_train = pd.DataFrame(y_test_2)
predicted_output_train = pd.DataFrame(y_output)

y_train_2_list = [y_test_2[col].to_numpy() for col in y_test_2.columns]
y_output_list = [y_output[col].to_numpy() for col in y_output.columns]


result_list = []

for i in range(len(y_train_2_list)):
    result_list.append(((y_train_2_list[i] - y_output_list[i])*100 / y_train_2_list[i]).round(2))


result_df = pd.DataFrame({col: result_list[i] for i, col in enumerate(y_train_2.columns)})

frames=[]
for i in range(len(actual_output_train)):
    current_row_df = pd.DataFrame({'Actual': actual_output_train.iloc[i], 
                                    'Predicted': predicted_output_train.iloc[i], 
                                    'Error': result_df.iloc[i]}).transpose()
    frames.append(current_row_df)


train_error_file = pd.concat(frames, ignore_index=True)
new_columns = {'0': 'Ash', '1': 'VM','2':'Moisture', '3': '80','4':	'-25','5':'CSR'	,'6': 'CRI','7': 'M40','8':'M10'}
train_error_file.rename(columns=new_columns, inplace=True)
train_error_file = train_error_file.transpose()
column_mapping = {}
for i in range(280):
    day_number = (i // 3) + 1 
    if(i%3==0) :column_mapping[i]=f'day {day_number} Actual'
    elif(i%3==1) :column_mapping[i]=f'day {day_number} Predicted'
    else: column_mapping[i]=f' day {day_number} Error'

train_error_file.rename(columns=column_mapping, inplace=True)

train_error_file

test_error_file=train_error_file.transpose().round(2)

# file_path = 'test_error_file.csv'
# test_error_file.to_csv(file_path, index=True)