@echo off
set /p id="Enter Video Name: "
C:\Python27\python.exe C:\Python27\scripts\autosub_app.py --list-languages
set /p videolanguage="Enter Video Language: "
C:\Python27\python.exe C:\Python27\scripts\autosub_app.py -S %videolanguage% -D %videolanguage% %id%
PAUSE