import os
import joblib
import argparse
import sys
import numpy as np
import pandas as pd
from sklearn import preprocessing


def newdataFilter(csv_file):
    dadosFRAME = pd.read_csv(csv_file, index_col=0)              # Lê o arquivo contendo os dados
    
    dadosFRAME = dadosFRAME.drop(columns=['cp'], axis=1)         # Coluna removida durante análise
    
    dadosFRAME = dadosFRAME.drop(columns=['slope'], axis=1)      # Coluna removida durante análise
    
    try:
        dadosFRAME = dadosFRAME.drop(columns=['sex'], axis=1)    # Coluna removida se os dados de origem forem a entrada
    except:
        pass
    
    for label in list(dadosFRAME):                               # Substitui NaNs pela moda da coluna
        auxMODE = dadosFRAME[label].mode()
        dadosFRAME[label].fillna(auxMODE[0],inplace=True)
        
    scaler = preprocessing.MinMaxScaler()
    
    dadosOUT = scaler.fit_transform(dadosFRAME.values)
        
    return dadosOUT

    
def predict_class(data_path):
    data = newdataFilter(data_path)

    model = joblib.load('./models/lgbm.sav')
    
    result = model.predict(data)
    
    result_df = pd.DataFrame(result, columns=['sex'])
    
    result_df[result_df['sex'] == 1] = 'F' 
    
    result_df[result_df['sex'] == 0] = 'M'
    
    result_df.to_csv('newsample_PREDICTIONS_BernardoCassimiroFonsecadeOliveira.csv', index=False)

    
parser = argparse.ArgumentParser(description='Submeta dados para o API')
parser.add_argument('csvfile', type=argparse.FileType('r'), help='Input csv file')

args = parser.parse_args()

predict_class(parser.parse_args().csvfile)
print("Predicao concluida")
sys.exit(1)