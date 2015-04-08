import re
from collections import Counter

class CMDParser:
    modes = {"normal", "violence", "democracy", "reverse"}

    def print_mode():
        res = ""
        for mode in CMDParser.modes:
            res += (mode + " ")

        return res

    class NoModeError(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)

    def __init__(self, mode):
        if mode not in self.modes:
            raise self.NoModeError(mode)

        self.mode = mode;

    def parse(self, text, commands):
        cmd_re = re.compile("|".join(commands))
        input_cmds = cmd_re.findall(text)
        if self.mode == "normal":
            return input_cmds
        elif self.mode == "reverse":
            return self.reverse(input_cmds)
        else :
            max_count = 0
            max_cmds = []
            input_count = Counter(input_cmds)
            for cmd in self.uniq(input_cmds):
                if input_count[cmd] > max_count:
                    max_cmds = [cmd]
                    max_count = input_count[cmd]
                elif input_count[cmd] == max_count:
                    max_cmds += [cmd]

            if self.mode == "democracy":
                return max_cmds
            
            res_cmds = []
            for max_cmd in max_cmds:
                res_cmds += [max_cmd] * max_count

            return res_cmds

    def reverse(self, cmds):
        reverse_dict = {"left":"right", "right":"left", "up":"down", "down":"up", "A":"B", "B":"A", "L":"R", "R":"L", "select":"start", "start":"select"}
        reverse_cmds = []
        for cmd in cmds:
            reverse_cmds += [reverse_dict[cmd]]

        return reverse_cmds

    def uniq(self, li):
        founded = set()
        uniq_list = []
        for entry in li :
            if entry not in founded:
                uniq_list += [entry]
                founded.add(entry)
        
        return uniq_list
