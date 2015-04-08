from CMDParser import CMDParser
import unittest

class TestCMDParser(unittest.TestCase):
    def test_normal_mode(self):
        normal = CMDParser("normal")
        test_string = "leftleftrightrightupAdownBselectstartLR"
        cmds = normal.parse(test_string)
        self.assertEqual(cmds, ["left", "left", "right", "right", "up", "A", "down", "B", "select", "start", "L", "R"])

    def test_violence_mode(self):
        violence = CMDParser("violence")
        test_string = "leftleftrightrightupdownselectAAA"
        cmds = violence.parse(test_string)
        self.assertEqual(cmds, ["A", "A", "A"])

        test_string = "leftleftleftleftuprightupdownselectAAA"
        cmds = violence.parse(test_string)
        self.assertEqual(cmds, ["left", "left", "left", "left"])

        test_string = "leftleftrightrightAB"
        cmds = violence.parse(test_string)
        self.assertEqual(cmds, ["left", "left", "right", "right"])

    def test_democracy_mode(self):
        democracy = CMDParser("democracy")
        test_string = "leftleftrightrightupdownselectAAAL"
        cmds = democracy.parse(test_string)
        self.assertEqual(cmds, ["A"])

        democracy = CMDParser("democracy")
        test_string = "leftleftleftrightrightupdownselectAAA"
        cmds = democracy.parse(test_string)
        self.assertEqual(cmds, ["left", "A"])

    def test_reverse_mode(self):
        reverse = CMDParser("reverse")
        test_string = "leftrightupdownselectAALL"
        cmds = reverse.parse(test_string)
        self.assertEqual(cmds, ["right", "left", "down", "up", "start", "B", "B", "R", "R"])

    def test_exceptions(self):
        with self.assertRaises(CMDParser.NoModeError) :
            foo = CMDParser("foo")

    def test_uniq(self):
        parser = CMDParser("normal")
        test_list = ["aa", "a", "a", "b", "a", "b", "a", "c", "c"]
        self.assertEqual(["aa", "a", "b", "c"], parser.uniq(test_list))

if __name__ == '__main__':
    unittest.main()

