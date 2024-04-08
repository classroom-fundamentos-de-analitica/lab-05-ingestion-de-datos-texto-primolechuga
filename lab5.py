import pandas as pd
import os 
import pyarrow as pq

# Crear el DataFrame con columnas : phrase y sentiment

dfTest = pd.DataFrame(columns=['phrase', 'sentiment'])
dfTrain = pd.DataFrame(columns=['phrase', 'sentiment'])

for root1, dirs1, files1 in os.walk("./test"):
    for file1 in files1:
        if file1.endswith(".txt"):
            with open(os.path.join(root1, file1), 'r') as f:
                lines = f.readlines()
                for line in lines:
                    dfTest = dfTest._append({'phrase': line, 'sentiment': os.path.basename(root1)}, ignore_index=True)
#export a test_dataset.csv
dfTest.to_csv('test_dataset.csv')

for root2, dirs2, files2 in os.walk("./train"):
    for file2 in files2:
        if file2.endswith(".txt"):
            with open(os.path.join(root2, file2), 'r') as f:
                lines = f.readlines()
                for line in lines:
                    dfTrain = dfTrain._append({'phrase': line, 'sentiment': os.path.basename(root2)}, ignore_index=True)

#export a train_dataset.csv
dfTrain.to_csv('train_dataset.csv')