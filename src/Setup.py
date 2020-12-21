import subprocess
import sys
import requests

def installNode():
    requests.get("https://deb.nodesource.com/setup_10.x")
    subprocess.check_call([sys.executable, "apt", "install", "nodejs"])    

def downloadFile(url, filePath):
    r = requests.get(url, allow_redirects=True)
    open(filePath, 'wb').write(r.content)

def pipInstall(packages):
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])