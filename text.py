from flask import Flask, render_template

app_airplanes = Flask(__name__)




@app_airplanes.route('/')
@app_airplanes.route('/home')
def index():
    return render_template('index.html')


@app_airplanes.route('/')


if __name__ == "__main__":
    app_airplanes.run(debug=True)