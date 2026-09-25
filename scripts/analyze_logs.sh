#!/bin/bash

echo "=============================="
echo "Linux Log Analysis"
echo "=============================="

LOG_FILE="logs/application.log"

echo ""
echo "Total log lines:"
wc -l "$LOG_FILE"

echo ""
echo "ERROR count:"
grep -c "ERROR" "$LOG_FILE"

echo ""
echo "WARNING count:"
grep -c "WARNING" "$LOG_FILE"

echo ""
echo "INFO count:"
grep -c "INFO" "$LOG_FILE"

echo ""
echo "ERROR messages:"
grep "ERROR" "$LOG_FILE"

echo ""
echo "Log analysis completed."
