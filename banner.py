import pyfiglet
import sys
import socket
from datetime import datetime
ascii_banner = pyfiglet.figlet_format("imran")
print(ascii_banner)

if len(sys.argv) == 2:
    target = socket.gethostname
