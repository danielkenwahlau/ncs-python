"""  low-level TCP/IP ASCII command/log interface"""

import telnetlib


class TCP_IF(object):
    """connection via telnet/tcp-ip to receiver ascii interface """

    def __init__(self,ip_addr,port):
        ''' ip_addr and port as parameters to be generic '''
        # save ip_addr for later use (could be asked by other modules)
        self.ip_addr = ip_addr
        self.con = telnetlib.Telnet(self.ip_addr,port)


    def send_cmd(self,cmdstring,terminator="\n"):
        """ write a command [string] to receiver """
        self.con.write(cmdstring.encode('ascii') + terminator.encode('ascii'))

    
    def read_line(self,timeout=0):
        """ read a line (wait for eol), return its string. If timeout expires -> raise an exception """
        s = self.con.read_until(b"\n",timeout).decode('ascii')
        if len(s) == 0:
            # if logging is turned off, this occurs after complete msg was read
            #raise IOError # ToDo: make timeout error
            return ""
        else:
            return s


    def read_response(self,pattern,timeout=0):
        """ read one or more lines (continuously) that starts with pattern, skip all that does not match"""
        d = list()
        line = ""
        
        # remove all "old" lines without desired pattern
        while pattern not in line:
            line = self.read_line(timeout)
            # handle timeout when nothing could be read
            # return empty list
            if (line == ""):
                return list()

        # get every continuous line with pattern
        while pattern in line:
            line = line.strip()
            sublist = line.split(',')
            d.append(sublist[1:]) # remove e.g. CAP
            line = self.read_line(timeout)

        return d


    def __del__(self):
        self.con.close()
        

#endclass

