from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model/expense_model.pkl', 'rb'))  #read mode 

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        bmi = int(request.form['bmi'])
        children = int(request.form['children'])
        sex = int(request.form['Sex'])
        smoker = int(request.form['Smoker'])
        region = int(request.form['Region'])

        #get prediction
        input_cols = [[age, bmi, children, sex, smoker, region]]
        prediction = model.predict(input_cols)
        output = round(prediction[0], 2)
        return render_template("index.html", prediction_text="Your predicted annual healthcare expense is ${}".format(output))

if __name__ == "__main__":
    app.run(debug=True)