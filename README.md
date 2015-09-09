# Docker-Bioconductor-Cytoscape
Docker file for kristiyanto/networkbma.

The package contains: Cytoscape, R, with Bioconductor packages (igraph, Rserve, and networkBMA). 

A tutorial to get it run on Windows and Mac are available: 
https://www.youtube.com/watch?v=FXOU2EZ4szI (Mac)
https://www.youtube.com/watch?v=Y1Ye5mOMBW0 (Windows)


## OSX
# PREPARATION
# Install Docker
https://www.docker.com/toolbox

# Install Brew 
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Install X11 (XQuartz) 
brew install xquartz
# Install Socat
brew install socat
# TO RUN CONTAINER 
# Get the Socat running 
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"

# Get XQuartz Running
open -a Xquartz

# Get Docker Running
(Run Kitematic)

# Run the Image (IP is your Mac IP, use ifconfig command if not sure)
docker run -ti -e DISPLAY=192.168.99.1:0 kristiyanto/networkbma


## WINDOWS
# PREPARATION
# Install Docker
https://www.docker.com/toolbox

# Install MobaXterm 
http://mobaxterm.mobatek.net/

# TO RUN CONTAINER 
# Get Docker running
(run kitematic)

# Open MobaXterm with X11 Support
(tools -> X11 tab with DWM)

# Login into Docker VM
ssh -X docker@192.168.99.100

password is tcuser, ip is your docker VM IP. If not sure, run:
docker-machine ip default

# Run Docker
docker run -ti -e DISPLAY=192.168.99.1:1.0 kristiyanto/networkbma

IP is your Windows IP address. Use ipconfig if not sure.
Display port (:1.0) is your current display port. Look at your MobaXterm window tab name if not sure.





