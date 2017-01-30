# every bot has to write "I'm Poppy" to its STDOUT as a handshake with the
# engine otherwise the bot will be disqualified.
from time import sleep
import sys

print "I'm Poppy!"
sys.stdout.flush()

for i in xrange(2):
    sleep(0.5)
    a = raw_input()
    sleep(0.5)
    print "Notice me Senpai!"
    sys.stdout.flush()
