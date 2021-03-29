from flask import Flask, render_template, request
import joblib
import pickle
import pandas as pd

app = Flask(__name__)

# halaman home
@app.route('/')
def home():
    return render_template('home.html')

# # halaman dataset
# @app.route('/database', methods=['POST','GET'])
# def dataset():
#     return render_template('dataset.html')

# # halaman visualisasi
# @app.route('/visualize', methods=['POST', 'GET'])
# def visual():
#     return render_template('plot.html')

# halaman input prediksi
@app.route('/predict', methods=['POST','GET'])
def predict():
    return render_template('predict.html')

# halaman hasil prediksi
@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        input = request.form

        df_predict = pd.DataFrame({
            'sex':[input['sex']],
            'age':[input['age']],
            'parch':[input['parch']],
            'fare':[input['fare']],
            'class':[input['class']],
            'embark_town':[input['embark_town']],
            'alone':[input['alone']]
        })

        prediksi = model.predict_proba(df_predict)[0][1]

        if prediksi > 0.5:
            label = 'Alive'
        else:
            label = 'Dead'

        return render_template('result.html', data=input, pred=label)

if __name__ == '__main__':
    filename = 'C:/Users/LENOVO/Documents/PURWADHIKA/DashTitanic/Titanic_Final5.sav'
    model = pickle.load(open(filename,'rb'))

    app.run(debug=True)
    

