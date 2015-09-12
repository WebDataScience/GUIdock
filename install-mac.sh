echo "\n\n\n ***** This script will install additional program \n ***** to enable X11 Forwarding in Mac. "
echo " ***** Docker will need to be downloaded and installed from Docker Website  \n\n\n"

# Install Home Brew 
echo "Installing Homebrew"
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# With home brew installed, install xquartz
echo "Installing xquartz"
brew install xquartz

# With home brew installed, install socat
echo "Installing Socat"
brew install socat

echo "\n\n\n ***** Now please download and install Docker Toolbox from Docker Website ***** "
echo " ***** https://www.docker.com/toolbox ***** \n\n\n"
open "https://www.docker.com/toolbox" &