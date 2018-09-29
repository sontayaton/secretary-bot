import ConfigParser
import io
from linemodules.msgforwarder import msgforwarder

msgforwarder.forwardMsgToUser("tonson","Tonson")
# Load the configuration file
configuration_file = "config/config.ini"

with open(configuration_file) as f:
    app_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(app_config))








# Print some contents
print("\nPrint some contents")
print(config.get('other', 'xxx'))  # Just get the value
#print(config.getboolean('other', 'use_anonymous'))  # You know the datatype?