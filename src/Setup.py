import subprocess
import sys

def pipInstall(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])