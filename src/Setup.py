import subprocess
import sys

def installNode():
    subprocess.check_call([sys.executable, "curl", "-sL", "https://deb.nodesource.com/setup_10.x"])
    subprocess.check_call([sys.executable, "apt", "install", "nodejs"])    

def installPip():
    subprocess.check_call([sys.executable, "curl", "https://bootstrap.pypa.io/get-pip.py", "-o", "get-pip.py"])
    subprocess.check_call([sys.executable, "python", "get-pip.py"])    

def pipInstall(packages):
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])