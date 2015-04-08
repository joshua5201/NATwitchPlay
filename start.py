from TwitchPlay import TwitchPlay
import sys

if len(sys.argv) != 2 :
    print("wrong number of arguments")
    print("usage: start.py [mode]")
    exit(1)
app = TwitchPlay()
app.start(sys.argv[1])
