import RPi.GPIO as GPIO
import time

BUZZER_PIN = 18
SWITCH_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

buzzer_on = False
last_switch_state = GPIO.input(SWITCH_PIN)

pwm = GPIO.PWM(BUZZER_PIN, 2500)  # Set to a sharp beep frequency
pwm_started = False

# Chirp pattern timings (seconds)
BEEP_FREQ = 2500       # Hz
BEEP_DURATION = 0.12   # Beep length
BEEP_GAP = 0.12        # Gap between two beeps
CYCLE_PAUSE = 0.5      # Pause between chirp cycles

print("Press the switch to toggle the buzzer alarm on/off. Ctrl+C to exit.")

try:
    while True:
        current_switch_state = GPIO.input(SWITCH_PIN)
        if last_switch_state == 1 and current_switch_state == 0:
            buzzer_on = not buzzer_on
            if buzzer_on:
                print("Buzzer ON")
            else:
                print("Buzzer OFF")
                if pwm_started:
                    pwm.stop()
                    pwm_started = False
            time.sleep(0.2)  # Debounce
        last_switch_state = current_switch_state

        # Chirp pattern if buzzer is on
        if buzzer_on:
            pwm.ChangeFrequency(BEEP_FREQ)
            if not pwm_started:
                pwm.start(50)
                pwm_started = True
            # First beep
            pwm.ChangeFrequency(BEEP_FREQ)
            pwm.start(50)
            time.sleep(BEEP_DURATION)
            pwm.stop()
            time.sleep(BEEP_GAP)
            # Second beep
            pwm.start(50)
            time.sleep(BEEP_DURATION)
            pwm.stop()
            # Pause before next cycle
            time.sleep(CYCLE_PAUSE)
        else:
            time.sleep(0.05)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    if pwm_started:
        pwm.stop()
    GPIO.cleanup()
