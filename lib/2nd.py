import os
import time
# Set color
G = '\033[1;32m' # Green

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.003)
delay_print
delay_print (""+G+"╔════════════════════════════════════════╗  ""\n")
delay_print (""+G+"║ Instagram: @ hackerxmr                 ║  ""\n")
delay_print (""+G+"║ Github: https://github.com/MrHacker-X/ ║  ""\n")
delay_print (""+G+"╚════════════════════════════════════════╝  ""\n")
