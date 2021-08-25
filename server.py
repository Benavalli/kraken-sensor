from flask import Flask, request, jsonify

from IO.dht11 import Dht11
from IO.relay import Relay

app = Flask(__name__)


@app.route('/temperature-humidity', methods=['GET'])
def get_temperature_humidity():
    temperature_humidity = Dht11().get_temperature_humidity().to_json()
    return jsonify({'temperature-humidity': temperature_humidity})


@app.route('/lamp-relay-state', methods=['POST'])
def post_lamp_relay_state():
    device_state = request.values.get('state')
    relay_devices = Relay().change_light_relay_state(device_state)
    return jsonify({'relay-devices': relay_devices})


@app.route('/exhaust-relay-state', methods=['POST'])
def post_exhaust_relay_state():
    device_state = request.values.get('state')
    relay_devices = Relay().change_exhaust_relay_state(device_state)
    return jsonify({'relay-devices': relay_devices})


@app.route('/humidifier-relay-state', methods=['POST'])
def post_humidifier_relay_state():
    device_state = request.values.get('state')
    relay_devices = Relay().change_humidifier_relay_state(device_state)
    return jsonify({'relay-devices': relay_devices})


@app.route('/pump-relay-state', methods=['POST'])
def post_pump_relay_state():
    device_state = request.values.get('state')
    relay_devices = Relay().change_pump_relay_state(device_state)
    return jsonify({'relay-devices': relay_devices})


if __name__ == '__main__':
    app.run(host='192.168.86.184')
