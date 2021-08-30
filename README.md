# kraken-sensor
Raspberry PI application to read temperature, humidity and measure LUX. The application is also managing connected devices using a relay board module.

# Setup Environment

   - Install Python 3
   - Run `sh kraken-setup.sh`
   - Activate your newly Python env, because the dependencies were downloaded in there and also to avoid conflicts within your system libraries `source env/bin/activate`
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

   - Run `nohup python server.py` 
