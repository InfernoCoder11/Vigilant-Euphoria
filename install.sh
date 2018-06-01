printf "Running sudo apt-get update\n"
sudo apt-get update

printf "\nRunning sudo apt-get upgrade\n"
sudo apt-get upgrade

printf "\nInstalling pip\n"
sudo apt-get install python3-pip

printf "\nInstalling virtualenv\n"
sudo pip3 install virtualenv

printf "\nChanging Directory to home\n"
cd

printf "\nMaking Vigilant-Euphoria-Server directory\n"
mkdir Vigilant-Euphoria-Server

printf "\nChanging dir to Vigilant-Euphoria-Server\n"
cd Vigilant-Euphoria-Server

printf "\nCreating virtual environment\n"
virtualenv flask-env

printf "\nActivating virtual environment\n"
source flask-env/bin/activate

printf "\nInstalling flask\n"
pip install Flask
