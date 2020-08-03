# Pi Fan Controller

Raspberry Pi fan controller.

## Description

This repository provides scripts that can be run on the Raspberry Pi that will
monitor the core temperature and start the fan when the temperature reaches
a certain threshold.

To use this code, you'll have to install a fan. The full instructions can be
found on our guide: [Control Your Raspberry Pi Fan (and Temperature) with Python](https://howchoo.com/g/ote2mjkzzta/control-raspberry-pi-fan-temperature-python).

## Installation
1. Clone this repo: `git clone https://github.com/msy021/pi-fan-controller.git`
1. Run the setup script: `./pi-fan-controller/script/install`

## If pip is not already installed run:
`sudo apt install python3-pip`

### Install requirements globally
`sudo pip3 install -r pi-fan-controller/requirements.txt`

## Uninstallation
If you need to uninstall:

1. Run the uninstall script: `./pi-fan-controller/script/uninstall`
