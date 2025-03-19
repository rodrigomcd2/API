import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "App is running"
  
@app.route('/totalvendas')
def pegarvendas():
    df=pd.read_csv('12-18 - Criando API no Python.csv')
    total_vendas=df['Vendas'].sum()
    return jsonify({'total_vendas': total_vendas})
  
app.run(host='0.0.0.0')

df = pd.read_csv('12-18 - Criando API no Python.csv')
total_vendas = df['Vendas'].sum()
print(total_vendas)

