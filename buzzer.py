import RPi.GPIO as GPIO
import time

BUZZER_PIN = 18
SWITCH_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

buzzer_on = False
last_switch_state = GPIO.input(SWITCH_PIN)

# Set up PWM (start at 1kHz, duty 50%)
pwm = GPIO.PWM(BUZZER_PIN, 1000)
pwm_started = False

def play_siren():
    # Sweep frequencies between 1000 Hz and 2500 Hz
    for freq in range(1000, 2500, 50):
        pwm.ChangeFrequency(freq)
        time.sleep(0.01)
    for freq in range(2500, 1000, -50):
        pwm.ChangeFrequency(freq)
        time.sleep(0.01)

print("Press the switch to toggle the buzzer siren on/off. Ctrl+C to exit.")

try:
    while True:
        current_switch_state = GPIO.input(SWITCH_PIN)
        if last_switch_state == 1 and current_switch_state == 0:
            buzzer_on = not buzzer_on
            if buzzer_on:
                pwm.start(50)  # Start PWM at 50% duty
                pwm_started = True
            else:
                pwm.stop()
                pwm_started = False
            print("Buzzer ON" if buzzer_on else "Buzzer OFF")
            time.sleep(0.2)
        last_switch_state = current_switch_state

        # Play siren if buzzer is on
        if buzzer_on and pwm_started:
            play_siren()
        else:
            time.sleep(0.01)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    if pwm_started:
        pwm.stop()
    GPIO.cleanup()
