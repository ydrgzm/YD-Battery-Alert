
# **YD Battery Alert**

A python script that runs as a background service. It alerts the user in two cases:

* Battery level > 90 and charger is connected
* Battery level < 30 and charger is not connected

# Setup
We are going to set up the app to run as a `startup service`, meaning that the service will start executing as soon as the computer is switched on. Follow the steps below for this:

1. Press Win + R to open Run.
2. Type `shell:startup` and hit Enter to open startup apps folder. 
3. Now create a shortcut of `run.bat` and place it in the startup apps folder.
4. Now Restart Your PC/Laptop.
5. Enjoy!


## Screenshots

![Low Battery Screenshot](https://github.com/ydrgzm/YD-Battery-Alert/blob/main/images/low_battery.png?raw=true)
