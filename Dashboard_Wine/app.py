from flask import Flask, render_template, request
import pickle
import pandas as pd 

app = Flask(__name__)

# home
@app.route('/')
def home():
    return render_template('home.html')

# input data untuk prediksi
@app.route('/predict', methods=['POST','GET'])
def predict():
    return render_template('predict.html')

# hasil prediksi
@app.route('/result', methods=['POST','GET'])
def result():
    if request.methods == 'POST':
        input = request.form

        df_predict = pd.DataFrame({
            'alcohol':[input['Alcohol']],
            'density':[input['Density']],
            'fixed acidity level':[input['fal']],
            'chlorides level':[input['cl']]
        })

        prediksi = model.predict_proba(df_predict)[0][1]

        if prediksi > 0.5:
            quality = 'Good'
        else:
            quality = 'Bad'

        return render_template('result.html', data=input, pred=quality)

if __name__ == '__main__':
    filename = 'Model Final.sav'
    model = pickle.load(open(filename,'rb'))
    app.run(debug=True)