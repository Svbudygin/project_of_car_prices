from flask import Flask, request, render_template, url_for

from utils.DFwork import description_func

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('Welcome.html')


@app.route('/hypothesis')
def hypothesis():
    return render_template('hypothesis.html')


@app.route('/data', methods=["GET", "POST"])
def data():

    if request.method == 'POST':
        query = request.form['our_params']
        res, lst = description_func(query)
        return render_template('data.html', result=res, lst=lst)
    else:
        return render_template('data.html')


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000)
    app.run()
