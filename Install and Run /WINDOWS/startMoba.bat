REM This file starts up MobaXterm
REM Hong Hung 9-14-2015
@echo off

FOR /F "delims=" %%i in ('where /R "C:\Program Files (x86)" MobaXterm') do set Moba=%%i
echo Docker IP Address is: %1
echo VirtualBox IP Address is: %2 
echo Dockerfile or Image is: %3 
echo MobaXterm binary is %Moba%
start "" "%Moba%" -exitwhendone -exec "sshpass -p tcuser ssh docker@%1 'docker run -t -e DISPLAY=%2:0 %3'"
