# raspberry_pi_turtle_buzzer
Simple GPIO code for a raspberry pi 4 b to mimic the sound of a Lowes "turtle" alarm

<audio controls>
  <source src="./audio/sample_audio.m4a" type="audio/mp4">
  Your browser does not support the audio element.
</audio>

<img src="./images/example.png" alt="Example" width="50%">

# Pinout

```
Raspberry Pi 4 GPIO Header (Top View, Pins 1-20)
 -----------------------------------------------------
| 1  3V3    2  5V                                    |
| 3  GPIO2  4  5V                                    |
| 5  GPIO3  6  GND  o<---+-----[Buzzer -]            |
| 7  GPIO4  8  GPIO14     |                          |
| 9  GND    10 GPIO15     |                          |
|11 GPIO17 12 GPIO18------+-----[Buzzer +]           |
|   |        |                                       |
|   +-----[Switch]                                   |
|         |                                          |
|         +-------------------o GND (any GND pin)    |
 -----------------------------------------------------

Components:
- [Buzzer +]: Connect to GPIO18 (pin 12)
- [Buzzer -]: Connect to GND (pin 6)
- [Switch]: One side to GPIO17 (pin 11), other side to any GND (e.g., pin 9)
```

# Install

Install Ansible and run the following command

```
ansible-playbook -i $YOUR_PI_IP, $ scripts/deploy.yml -e service_user=$YOUR_PI_USERNAME
```

* Note the comma at the end of the ip address. If not present it will not work
