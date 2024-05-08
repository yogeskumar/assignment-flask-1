from datetime import date
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/index.html')
def home():
   return render_template('index.html', date = date.today() )
@app.route('/page2.html')
def page2():
   return render_template('page2.html', date = date.today() )
@app.route('/page3.html')
def page3():
   return render_template('page3.html', date = date.today() )
if __name__ == '__main__':
   app.run(debug = True)
