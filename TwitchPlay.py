from IRC import IRC
from CMDParser import CMDParser
import sys, time, os, datetime
from pykeyboard import PyKeyboard

class TwitchPlay:
    def start(self, mode):
        os.popen("vba 大聯盟棒球賽.gba")
        irc = IRC("irc.twitch.tv", "ji01", "oauth:kx5f1v4wi8ni4fkmayta7ov9mzzy")
        irc.connect()

        try:
            parser = CMDParser(mode)
        except CMDParser.NoModeError:
            print("available modes: " + CMDParser.print_mode())
            exit(1)

        print("Gamemode: " + mode)
        print("ready")

        all_commands = ["left", "right", "up", "down", "select", "start", "A", "B", "L", "R"]
        commands = all_commands
        while True:
            try:
                if mode == "democracy":
                    print("start voting for 5 second(s)")
                    time.sleep(5)

                messages = irc.get_msg(irc.recv())
                text = ""
                for message in messages :
                    print(message)
                    text += message.text

                result = parser.parse(text, commands)
                if mode == "democracy" and len(result) > 1:
                    print("voting again for " + str(result))
                    commands = result
                    print(result)
                else :
                    commands = all_commands
                    if (len(result) > 0):
                        print("commands :" + str(result))
                    for cmd in result :
                        self.sendkey(cmd)

            except KeyboardInterrupt:
                print ("Ctrl-C caught, disconnecting")
                irc.disconnect()
                sys.exit()

    def sendkey(self, cmd):
        keys = {"left":0x25, "right":0x27, "up":0x26, "down":0x28, "A":"z", "B":"x", "L":"a", "R":"s", "start":0x0d, "select":0x08}
        kb = PyKeyboard()
        kb.tap_key(keys[cmd])

