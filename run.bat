@echo off
pytest -s -v -m "regression" --html=./Reports/report.html TestCases/ --browser chrome