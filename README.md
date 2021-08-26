# kraken-sensor
Raspberry PI application to read temperature, humidity and measure LUX. The application also control connected devices using relay board module.

# Setup Environment

   - Install Python 3
   - Run `sh kraken-setup.sh`
   - Activate your newely Python env, because the dependencies were downloaded in there and to avoid conflicts within your system libraries `source env/bin/activate`
   - Make sure to adjust `config.properties` to match the `GPIO` PIN numbers which the devices are connected into your Raspberry PI
