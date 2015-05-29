__author__ = 'mine_bit'

from plugins import popbrute_plugin


class popbrute():
    @classmethod
    def Strart(cls, server_in, userlist_in, wordlist_in):
        popbrute_plugin.Start(server_in, userlist_in, wordlist_in)
