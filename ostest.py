import os
import sys
import platform

print(f"{os.name=}")
print(f"{sys.platform=}")
print(f"{platform.mac_ver()=}")
print(f"{platform.system()=}")
print(f"{platform.architecture()=}")
