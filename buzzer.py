import RPi.GPIO as GPIO
import time

BUZZER_PIN = 18
SWITCH_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

buzzer_on = False
last_switch_state = GPIO.input(SWITCH_PIN)

# Siren parameters
freq = 1000
direction = 1  # 1 = up, -1 = down
min_freq = 1000
max_freq = 2500
step = 50

pwm = GPIO.PWM(BUZZER_PIN, freq)
pwm_started = False

print("Press the switch to toggle the buzzer siren on/off. Ctrl+C to exit.")

try:
    while True:
        current_switch_state = GPIO.input(SWITCH_PIN)
        if last_switch_state == 1 and current_switch_state == 0:
            buzzer_on = not buzzer_on
            if buzzer_on:
                pwm.start(50)  # Start PWM at 50% duty
                pwm_started = True
                print("Buzzer ON")
            else:
                pwm.stop()
                pwm_started = False
                print("Buzzer OFF")
            time.sleep(0.2)  # Debounce delay
        last_switch_state = current_switch_state

        # Non-blocking siren logic
        if buzzer_on and pwm_started:
            pwm.ChangeFrequency(freq)
            freq += direction * step
            if freq >= max_freq or freq <= min_freq:
                direction *= -1  # Change sweep direction
            time.sleep(0.01)
        else:
            time.sleep(0.01)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    if pwm_started:
        pwm.stop()
    GPIO.cleanup()
