# raspberry_pi_turtle_buzzer
Simple GPIO code for a raspberry pi 4 b to mimic the sound of a Lowes "turtle" alarm with visual LED indicator

## Example Audio
![Audio](./audio/sample_audio.m4a)

## Inspiration
![Example](./images/turtle.png)

## Implementation Example

![Example](./images/example.png)

## Features
- **Sound**: Variable frequency siren that sweeps between 1000Hz and 2500Hz
- **Visual**: LED blinks at approximately 5Hz (200ms intervals) while the alarm is active
- **Control**: Push button to toggle alarm on/off


# Raspberry Pi Pinout

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
|13 GPIO27-+-----[LED +]--[220Ω Resistor]--[LED -]  |
|         |                                   |      |
|         +-------------------o GND (any GND pin)    |
 -----------------------------------------------------

Components:
- [Buzzer +]: Connect to GPIO18 (pin 12)
- [Buzzer -]: Connect to GND (pin 6)
- [Switch]: One side to GPIO17 (pin 11), other side to any GND (e.g., pin 9)
- [LED +]: Connect to GPIO27 (pin 13) through a 220Ω current-limiting resistor
- [LED -]: Connect to any GND pin (e.g., pin 6, 9, 14, 20, 25, etc.)
```

# Deploy

Install Ansible and run the following command

```
ansible-playbook -i $YOUR_PI_IP, $ scripts/deploy.yml -e service_user=$YOUR_PI_USERNAME
```

* Note the comma at the end of the ip address. If not present it will not work
