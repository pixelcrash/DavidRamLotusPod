#!/bin/bash

# Use curl to check for internet connectivity

sudo pkill -f "python3 app.py"

if curl -s --head http://www.google.com/ &> /dev/null; then
  echo "Internet connection detected."
  sudo rm -rf /home/pi/DavidRamLotusPod/*
  sudo rm -rf /home/pi/DavidRamLotusPod
  git clone https://github.com/pixelcrash/DavidRamLotusPod.git
 # sudo rm -rf /home/pi/flask/*
  sudo cp -rf /home/pi/DavidRamLotusPod/* /home/pi/flask
  # Place your commands here that should run when there is an Internet connection
  
else
  echo "No Internet connection."
  # Place your commands here that should run when there is no Internet connection
fi

sudo reboot -h now
