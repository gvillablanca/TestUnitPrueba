#!/bin/bash

LOGS_FOLDER="logs"
mkdir -p "$LOGS_FOLDER"

CURRENT_DATETIME=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="$LOGS_FOLDER/selenium_log_${CURRENT_DATETIME}.txt"

REQUIREMENTS_FILE="requirements.txt"

pip install -r "$REQUIREMENTS_FILE"

selenium-side-runner Simple_Stock.side >> "$LOG_FILE" 2>&1

if [ $? -eq 0 ]; then
    echo "Ejecución exitosa. Verifica el archivo de log: $LOG_FILE"
else
    echo "Error durante la ejecución. Consulta el archivo de log: $LOG_FILE"
fi