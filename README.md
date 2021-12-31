# BerryBot [WIP]

This bot allows you to send SMS messages using a Telegram bot and a RaspberryPi.

## Why?

I am leaving abroad and from time to time I need to receive and send SMS messages from Brazil.


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

git clone https://github.com/rafaelzimmermann/BerryPhone.git
cd BerryPhone

mkvirtualenv berryphone
pip3 install -r requirements.txt

python berrybot.py

```


## HUAWEI E8372

Follow this [HOWTO](https://gist.github.com/ethaniel/d7f9c3192041c64c89d2c5b49527d0e2) written by @ethaniel.