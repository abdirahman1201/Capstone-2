from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html', title='homepage')

@app.route('/about')
def about():
    return render_template('about.html', title='About')




if __name__ == "__main__":
    app.run(host='0.0.0.0')