import pickle
from flask import Flask,request,app,jsonift,url_for,render_template
import numpy as np
import pandas as pd


app = Flask(__name__)

## loaad the model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
