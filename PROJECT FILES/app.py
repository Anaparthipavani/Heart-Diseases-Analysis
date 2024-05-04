from flask import Flask, render_template

app = Flask(_name_) #intializing Flask

@app.route('/')
def index():
     return render_template('index.html')


if _name_ == '__main__':
    app.run(debug=True)