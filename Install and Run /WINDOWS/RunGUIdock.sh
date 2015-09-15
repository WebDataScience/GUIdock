#!/bin/bash
#Version Hong Hung 9/14/2015
#based on Docker start.sh

#Customize Image here
IMAGE="kristiyanto/guidock"

#Flag errors - from original 
trap '[ "$?" -eq 0 ] || read -p "Looks like something went wrong... Press any key to continue..."' EXIT

#Save current working directory
WD=`pwd`

#Change this if Docker files are stored elsewhere
cd "/c/Program Files/Docker Toolbox"

#Mostly from original docker script
VM=default
DOCKER_MACHINE=./docker-machine.exe
VBOXMANAGE=/$(reg query HKEY_LOCAL_MACHINE\\SOFTWARE\\Oracle\\VirtualBox //v InstallDir | grep InstallDir | awk '{print substr($0, index($0,$3))}' | sed 's/\\/\//g' | sed 's/://')VBoxManage.exe

MOBAXTERM="/c/Program Files (x86)/Mobatek/MobaXterm Personal Edition/MobaXterm.exe"
BATCH="$WD/startMoba.bat"
echo "Virtual Box Path is $VBOXMANAGE"

if [ ! -f $DOCKER_MACHINE ] || [ ! -f "${VBOXMANAGE}" ]; then
  echo "Either VirtualBox or Docker Machine are not installed. Please re-run the Toolbox Installer and try again."
  exit 1
fi

"${VBOXMANAGE}" showvminfo $VM &> /dev/null
VM_EXISTS_CODE=$?

set -e

if [ $VM_EXISTS_CODE -eq 1 ]; then
  echo "Creating Machine $VM..."
  $DOCKER_MACHINE rm -f $VM &> /dev/null || :
  rm -rf ~/.docker/machine/machines/$VM
  $DOCKER_MACHINE create -d virtualbox --virtualbox-memory 2048 $VM
else
  echo "Machine $VM already exists in VirtualBox."
fi

echo "Starting machine $VM..."
$DOCKER_MACHINE start $VM

echo "Setting environment variables for machine $VM..."
eval "$($DOCKER_MACHINE env --shell=bash $VM)"
clear

#This code is to find the Virtual Box IP for VM default
VBOXHOST=`"${VBOXMANAGE}" showvminfo default | grep 'VirtualBox Host-Only' | sed -n " s,[^']*'\([^']*\).*,\1,p " | sed "s/Ethernet Adapter/Network/"`
echo "$VBOXHOST"
MYCMD="netsh interface ip show addresses \""$VBOXHOST"\""
echo "Finding VBoxIP $MYCMD"
TMP=`$MYCMD | grep IP`
VBIP=`echo $TMP | awk '{print \$3}'`
echo "VBoxIP is $VBIP"
DOCKERIP=`docker-machine ip $VM`

#Run the bat script to run MobaXterm because of all the escaping necessary otherwise
$BATCH $DOCKERIP $VBIP $IMAGE&
clear
exit 0
