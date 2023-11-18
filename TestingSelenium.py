import subprocess
import os
from datetime import datetime

LOGS_FOLDER = "logs"
if not os.path.exists(LOGS_FOLDER):
    os.makedirs(LOGS_FOLDER)

current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILE = os.path.join(LOGS_FOLDER, f"selenium_log_{current_datetime}.txt")

REQUIREMENTS_FILE = "requirements.txt"

subprocess.run(["pip", "install", "-r", REQUIREMENTS_FILE])

command = "selenium-side-runner Simple_Stock.side"
with open(LOG_FILE, "w") as log_file:
    result = subprocess.run(command, stdout=log_file, stderr=subprocess.STDOUT, shell=True)

if result.returncode == 0:
    print(f"Ejecución exitosa. Verifica el archivo de log: {LOG_FILE}")
else:
    print(f"Error durante la ejecución. Consulta el archivo de log: {LOG_FILE}")