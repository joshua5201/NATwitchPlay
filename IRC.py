import socket
import sys
import re
import time
import datetime

class IRC:

    class LoginFailed(Exception):
        def __init__(self, value):                                                                       
            self.value = value
        def __str__(self):
            return repr(self.value)

    def __init__(self, host, user, passwd = "", port=6667):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port

    def connect(self, timeout=10):
        passwd_msg = 'PASS ' + self.passwd + '\r\n'
        nick_msg = 'NICK ' + self.user   + '\r\n'
        channel_msg = 'JOIN #' + self.user   + '\r\n'


        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.conn.setblocking(0)
        self.conn.settimeout(timeout)
        self.conn.connect((self.host, self.port))
        self.conn.send(passwd_msg.encode('utf-8'))
        self.conn.send(nick_msg.encode('utf-8'))
        self.conn.send(channel_msg.encode('utf-8'))

        failed = re.compile(":Login unsuccessful", re.MULTILINE)
        if failed.search(self.recv()) != None :
            raise self.LoginFailed("user: " + self.user + " passwd: " + self.passwd)

    def disconnect(self):
        self.conn.close()

    def send(self, text):
        msg = 'PRIVMSG #' + self.user + ' ' + ':'+text + '\r\n'
        self.conn.send(msg.encode('utf-8'))

    def recv(self):
        msg = b''
        try:
            msg= self.conn.recv(8192)
        except socket.timeout:
            pass

        find_ping = re.compile("PING :tmi.twitch.tv", re.MULTILINE)
        if find_ping.search(msg.decode('utf-8')) != None:
            self.conn.send(b"PONG :tmi.twitch.tv")

        return msg.decode('utf-8')

    class Message:
        def __init__(self, sender, text, recvtime):
            self.sender = sender
            self.text = text
            self.recvtime = recvtime

        def __str__(self):
            return self.sender + " " + self.recvtime.strftime("%x %X")+ ": " + self.text

    def get_msg(self, text):
        messages = []
        msg_re = re.compile("^:.*!(.*)@.*PRIVMSG.*:(.*)$", re.MULTILINE)
        res = msg_re.findall(text)
        for msg in res :
            new_message = self.Message(msg[0], msg[1].replace('\r', ''), datetime.datetime.now())
            messages += [new_message]

        return messages
