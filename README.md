# kraken-sensor
Raspberry PI application to read temperature, humidity and measure LUX. 
Management of connected devices using a relay board module.
Routines to be added in Raspberry PI contrab.

# Setup Environment

   - Install Python 3
   - Run `sh kraken-setup.sh`
   - Activate your newly Python env, because the dependencies were downloaded in there and also to avoid conflicts within your system libraries `source env/bin/activate`
   - Export the Python path, which you have downloaded the project, e.g.  `export PYTHONPATH=/home/{user-name}/{clone-path}/kraken-sensor`
   - Make sure to adjust `config.properties` to match the `GPIO` PIN numbers which the devices are connected to your Raspberry PI

# Crontab

   - Edit your Crontab file `crontab -e`, to execute routines
 
```
PYTHONPATH=/home/{user-name}/{clone-path}/kraken-sensor
4 8 * * * python3 /home/{user-name}/{clone-path}/kraken-sensor/cron/cron_light_on.py
4 20 * * * python3 /home/{user-name}/{clone-path}/kraken-sensor/cron/cron_light_off.py
1 8-23,0-1 * * * python3 /home/{user-name}/{clone-path}/kraken-sensor/cron/cron_pump_on.py
*/41 8-23,0-1 * * * python3 /home/{user-name}/{clone-path}/kraken-sensor/cron/cron_pump_off.py
*/5 * * * * python3 /home/{user-name}/{clone-path}/kraken-sensor/cron/cron_temperature_humidity.py
30 8 * * * python3 /home/{user-name}/{clone-path}/kraken-sensor/cron/cron_water_level.py
@reboot python3 /home/{user-name}/{clone-path}/kraken-sensor/server/server.py > /home/pi/Kraken/server.log
```

# Server

   - Run `nohup python3 server.py` 
