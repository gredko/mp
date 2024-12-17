import os
import subprocess

services = ['python manage.py runserver', 'redis-server']

for service in services:
    try:
        subprocess.run(service, check=True, shell=True)
        print(f"{service} restarted successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to restart {service}.")
