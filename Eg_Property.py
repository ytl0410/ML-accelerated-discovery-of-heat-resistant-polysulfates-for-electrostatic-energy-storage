import argparse
import pandas as pd

# Create the parser
parser = argparse.ArgumentParser(description='Process some CSV files.')

# Add the arguments
parser.add_argument('input_file', type=str, help='The input CSV file')

# Parse the arguments
args = parser.parse_args()

# Read the input file into a DataFrame
df = pd.read_csv(args.input_file)

import tensorflow as tf
model_1 = tf.keras.models.load_model('Eg_model.h5')

import numpy as np
import pickle
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import Draw
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit import DataStructs

import seaborn as sns
from sklearn.model_selection import train_test_split


from rdkit.Chem import rdMolDescriptors as rdmd
from tqdm import tqdm
from functools import wraps

fn = data.Smiles.apply(Chem.MolFromSmiles).apply(lambda m: AllChem.GetMorganFingerprintAsBitVect(m, radius=3, nBits=1024))
X_fingerprint = np.array(fn.tolist())
X = X_fingerprint

prediction = model_1.predict(X)
score =  prediction.mean(axis=1)
df.to_csv('Prediction_results_Eg.csv',index=False)
