


# Installation

```
sudo apt install python3-pip
pip3 install virtualenv
pip3 install virtualenvwrapper

# Config virtualenvwrapper
mkdir ~/envs
echo "export PATH="$PATH:$HOME/.local/bin"
echo "export WORKON_HOME=~/envs \n" > ~/.zshrc
echo "source $HOME/.local/bin/virtualenvwrapper.sh \n" > ~/.zshrc

sudo apt install gammu gammu-smsd libgammu-dev
sudo gammu-config

git clone https://github.com/gammu/python-gammu.git
cd python-gammu
GAMMU_PATH=/usr/bin/gammu python setup.py build

git clone https://github.com/rafaelzimmermann/BerryPhone.git
cd BerryPhone

mkvirtualenv berryphone
pip3 install -r requirements.txt

python berrybot.py

```