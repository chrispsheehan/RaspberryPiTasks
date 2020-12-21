import requests
import subprocess
import sys

def installNode():
    requests.get("https://deb.nodesource.com/setup_10.x")
    subprocess.check_call([sys.executable, "apt", "install", "nodejs"])    

def pipInstall(packages):
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])