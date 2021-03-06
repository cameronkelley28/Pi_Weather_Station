from flask import Flask, render_template
from sendEmail import *
from sense_hat import SenseHat

app = Flask(__name__)

@app.route('/')

def index():
    sense = SenseHat()
    sense.clear()

    acceleration = sense.get_accelerometer_raw()
    celcius      = round(sense.get_temperature(), 1)
    kwargs = dict(
        celcius     = celcius,
        fahrenheit  = round(1.8 * celcius + 32, 1),
        humidity    = round(sense.get_humidity(), 1),
        pressure    = round(sense.get_pressure(), 1),
        x = round(acceleration['x'], 2),
        y = round(acceleration['y'], 2),
        z = round(acceleration['z'], 2),
    )
    return render_template('weather.html', **kwargs)

while __name__ == '__main__':
    app.run(host='0.0.0.0')
