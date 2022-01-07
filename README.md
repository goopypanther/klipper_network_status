Klipper Network Status Plugin
=============================

Allow gcode macros to access system IP/hostname/wifi SSID/etc.

To install, clone repo into your rpi home folder and run `install.sh` or add the following to your moonraker configuration:

```
[update_manager client klipper_network_status]
type: git_repo
path: /home/pi/klipper_network_status
origin: https://github.com/JeremyRuhland/klipper_network_status
install_script: install.sh
```

Then, add `[network_status]` somewhere in your klipper configuration to enable the plugin.
