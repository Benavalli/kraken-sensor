# kraken-sensor
Raspberry PI application to measure temperature, humidity, water reservoir level and LUX. 
Management of connected devices using eletronic relay board modules.
Pre defined routines to be added in Raspberry PI contrab.

# Setup Environment

   - Verify if Pyhton >= 3 is installed
   - Clone the Kraken repo `git clone https://github.com/Benavalli/kraken-sensor`
   - Export the Python path, where you have downloaded the project, e.g.  `export PYTHONPATH=/home/{user-name}/{clone-path}/kraken-sensor`
   - Run `sh kraken-setup.sh`
   - Make sure to adjust `config.properties` to match the `GPIO` PIN numbers which the devices are connected to your Raspberry PI

# Crontab

   - Edit your Crontab file `crontab -e`, to execute routines
 
```
PYTHONPATH=/home/{user-name}/{clone-path}/kraken-sensor
4 8 * * * python /home/{user-name}/{clone-path}/kraken-sensor/cron/cron_light_on.py
4 20 * * * python /home/{user-name}/{clone-path}/kraken-sensor/cron/cron_light_off.py
1 8-23,0-1 * * * python /home/{user-name}/{clone-path}/kraken-sensor/cron/cron_fan_on.py
*/41 8-23,0-1 * * * python /home/{user-name}/{clone-path}/kraken-sensor/cron/cron_fan_off.py
*/5 * * * * python /home/{user-name}/{clone-path}/kraken-sensor/cron/cron_temperature_humidity.py
*/5 * * * * python /home/{user-name}/{clone-path}/kraken-sensor/cron/cron_camera.py
30 8 * * * python /home/{user-name}/{clone-path}/kraken-sensor/cron/cron_water_level.py
```

# API Server

   - Run `nohup python server.py` 
