# kraken-sensor
Raspberry PI application to read temperature, humidity and measure LUX. 
Management of connected devices using a relay board module.
Routines to be added in Raspberry PI contrab.

# Setup Environment

   - Install Python 3
   - Run `sh kraken-setup.sh`
   - Activate your newly Python env, because the dependencies were downloaded in there and also to avoid conflicts within your system libraries `source env/bin/activate`
   - Export the Python path, which you have downloaded the project, e.g.  `export PYTHONPATH=/home/pi/Kraken/kraken-sensor`
   - Make sure to adjust `config.properties` to match the `GPIO` PIN numbers which the devices are connected to your Raspberry PI

# Crontab

   - Edit your Crontab file `crontab -e`, to execute routines
 
```
PYTHONPATH=/home/pi/Kraken/kraken-sensor
5 8 * * * python3 /home/pi/Kraken/kraken-sensor/cron/cron_light_on.py
5 1 * * * python3 /home/pi/Kraken/kraken-sensor/cron/cron_light_off.py
1 8-23,0-1 * * * python3 /home/pi/Kraken/kraken-sensor/cron/cron_pump_on.py
*/41 8-23,0-1 * * * python3 /home/pi/Kraken/kraken-sensor/cron/cron_pump_off.py
*/10 * * * * python3 /home/pi/Kraken/kraken-sensor/cron/cron_temperature_humidity.py
```

# Server

   - Run `nohup python3 server.py` 
