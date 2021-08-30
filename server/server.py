from flask import Flask, request, jsonify

from IO.dht11 import Dht11
from IO.relay import Relay

app = Flask(__name__)


@app.route('/temperature-humidity', methods=['GET'])
def get_temperature_humidity():
    temperature_humidity = Dht11().get_temperature_humidity().to_json()
    return jsonify({'temperature-humidity': temperature_humidity})


@app.route('/light-relay-state', methods=['POST'])
def post_light_relay_state():
    request_data = request.get_json()
    device_state = request_data['state']
    relay_device = Relay().change_light_relay_state(device_state).to_json()
    return jsonify({'relay-devices': relay_device})


@app.route('/exhaust-relay-state', methods=['POST'])
def post_exhaust_relay_state():
    request_data = request.get_json()
    device_state = request_data['state']
    relay_device = Relay().change_exhaust_relay_state(device_state).to_json()
    return jsonify({'relay-devices': relay_device})


@app.route('/humidifier-relay-state', methods=['POST'])
def post_humidifier_relay_state():
    request_data = request.get_json()
    device_state = request_data['state']
    relay_device = Relay().change_humidifier_relay_state(device_state).to_json()
    return jsonify({'relay-devices': relay_device})


@app.route('/pump-relay-state', methods=['POST'])
def post_pump_relay_state():
    request_data = request.get_json()
    device_state = request_data['state']
    relay_device = Relay().change_pump_relay_state(device_state).to_json()
    return jsonify({'relay-device': relay_device})


if __name__ == '__main__':
    app.run(host='192.168.86.184')