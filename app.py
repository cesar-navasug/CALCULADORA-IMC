from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    if request.method == 'POST' and 'weight' in request.form and 'height' in request.form:
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = weight / (height ** 2)
    return render_template('index.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)
