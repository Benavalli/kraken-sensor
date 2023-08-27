import json

from flask import Flask, request, jsonify, render_template, Response
from IO.dht11 import Dht11
from IO.relay import Relay
from IO.camera import Camera

app = Flask(__name__)


@app.route('/temperature-humidity', methods=['GET'])
def get_temperature_humidity():
    temperature_humidity = Dht11().get_temperature_humidity()
    return jsonify({'temperature-humidity': temperature_humidity.__dict__})

@app.route('/relays', methods=['GET'])
def get_relays():
    relay_list = Relay().get_device_list()
    return jsonify({'relay-devices': [ob.__dict__ for ob in relay_list]})

@app.route('/light-relay-state', methods=['POST'])
def post_light_relay_state():
    request_data = request.get_json()
    device_state = request_data['state']
    relay_device = Relay().change_light_relay_state(device_state)
    return jsonify({'relay-devices': relay_device.__dict__})

@app.route('/exhaust-relay-state', methods=['POST'])
def post_exhaust_relay_state():
    request_data = request.get_json()
    device_state = request_data['state']
    relay_device = Relay().change_exhaust_relay_state(device_state)
    return jsonify({'relay-devices': relay_device.__dict__})

@app.route('/humidifier-relay-state', methods=['POST'])
def post_humidifier_relay_state():
    request_data = request.get_json()
    device_state = request_data['state']
    relay_device = Relay().change_humidifier_relay_state(device_state)
    return jsonify({'relay-devices': relay_device.__dict__})

@app.route('/pump-relay-state', methods=['POST'])
def post_pump_relay_state():
    request_data = request.get_json()
    device_state = request_data['state']
    relay_device = Relay().change_pump_relay_state(device_state)
    return jsonify({'relay-device': relay_device.__dict__})

@app.route('/fan-relay-state', methods=['POST'])
def post_fan_relay_state():
    request_data = request.get_json()
    device_state = request_data['state']
    relay_device = Relay().change_fan_relay_state(device_state)
    return jsonify({'relay-device': relay_device.__dict__})

@app.route('/inline-fan-relay-state', methods=['POST'])
def post_inline_fan_relay_state():
    request_data = request.get_json()
    device_state = request_data['state']
    relay_device = Relay().change_inline_fan_relay_state(device_state)
    return jsonify({'relay-device': relay_device.__dict__})

@app.route('/valve-relay-state', methods=['POST'])
def post_valve_relay_state():
    request_data = request.get_json()
    device_state = request_data['state']
    relay_device = Relay().change_valve_relay_state(device_state)
    return jsonify({'relay-device': relay_device.__dict__})

@app.route('/camera')
def camera_stream():
    """Video streaming home page."""
    return render_template('index.html')

def __gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(__gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
