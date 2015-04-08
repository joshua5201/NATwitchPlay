from IRC import IRC
import time
import unittest

class TestIRC(unittest.TestCase):

    def test_constructor(self):
        irc = IRC("testhost", "testuser")
        self.assertEqual("testhost", irc.host)
        self.assertEqual("testuser", irc.user)
        self.assertEqual("", irc.passwd)
        self.assertEqual(6667, irc.port)

    def test_connect_and_disconnect(self):
        irc = IRC("irc.twitch.tv", "jzzzzza5201", "oauth:ukw8ssssgzyq06lae2mupvr9x2gur55")
        irc.connect()
        msg = irc.recv()
        print(msg)
        irc.send("test string")
        irc.disconnect()
        with self.assertRaises(OSError):
            irc.send("raise error")
            
    def test_disconnect(self):
        irc = IRC("irc.twitch.tv", "joaaaa5201", "oauth:uasasaw8455gzyq06lae2mupvr9x2gur55")
        irc.connect()
        irc.disconnect()

    def test_send(self):
        irc = IRC("irc.twitch.tv", "joshsa201", "oauth:ukw8455gzyq06lae2mupvr9x2gaasasr55")
        irc.connect()
        irc.send("jaaizz a")

        irc.disconnect();

    def test_connect_failed(self):
        irc = IRC("iaaaaaaaaaaaaaa.aa", "a1")
        with self.assertRaises(OSError):
            irc.connect()
    
    def test_login_failed(self):
        irc = IRC("irc.twitch.tv", "jizz", "aa")
        with self.assertRaises(irc.LoginFailed):
            irc.connect()

    def test_recv_many_times(self):
        irc = IRC("irc.twitch.tv", "joshuas1", "oaasaah:ukw8455gzyq06lae2mupvr9x2gur55")
        irc.connect()
        irc.send("recv test")
        msg = irc.recv()
        print(msg)
        msg = irc.recv()
        print(msg)
        
    def test_get_msg(self):
        irc = IRC("irc.twitch.tv", "joshas201", "oauth:ukw8455gzyq06lae2muar55")
        irc.connect()
        print("please send messages in browser")
        time.sleep(10)
        text = irc.recv()
        messages = irc.get_msg(text)
        for message in messages :
            print(message)


if __name__ == '__main__':
    unittest.main()

