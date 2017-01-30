# every bot has to write "I'm Poppy" to its STDOUT as a handshake with the
# engine otherwise the bot will be disqualified.
from time import sleep
import sys

print "I'm Poppy!"
sys.stdout.flush()

while True:
    a = raw_input()
    print "Notice me Senpai!", a
    sys.stdout.flush()
