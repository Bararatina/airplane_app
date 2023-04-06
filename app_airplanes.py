from flask import Flask, render_template, request

app_airplanes = Flask(__name__)


class Airplane:
    max_speed = None
    year = None
    type_of_airplane = None
    flight_altitude = None

    def __init__(self, max_speed, year, type_of_airplane, flight_altitude):
        self.max_speed = max_speed
        self.year = year
        self.type_of_airplane = type_of_airplane
        self.flight_altitude = flight_altitude

    def create_airplane(self):
        return 'Type of airplane:', self.type_of_airplane, 'Year:', self.year, 'Flight altitude:', self.flight_altitude, 'Max speed:', self.max_speed
# как перенести на новую строчку, селф мешает


@app_airplanes.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        type_of_airplane = request.form['type_of_airplane']
        year = request.form['year']
        flight_altitude = request.form['flight_altitude']
        max_speed = request.form['max_speed']

        airplane = Airplane(max_speed, year, type_of_airplane, flight_altitude)
        return airplane
    else:
        return render_template('airplanes.html')


if __name__ == "__main__":
    app_airplanes.run(debug=True)
