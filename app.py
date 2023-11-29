from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/smt')
def home():
    return render_template('pr.html')


@app.route('/more', methods=['POST'])
def more():
    data = [str(x) for x in request.form.values()][0]
    return render_template('pr.html', result=f"some responses: {data}")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
