from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/mensaje')
def mensaje():
    return render_template('mensaje.html')

@app.route('/web1')
def web1():
    return render_template('web1.html')

@app.route('/web2')
def web2():
    return render_template('web2.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
