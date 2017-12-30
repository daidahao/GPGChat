import time

class Message:
    def __init__(self):
        self.send = None
        self.text = None
        self.timestamp = None
        self.uuid = None
        self.seq = None

    def __str__(self):
        return self.text + '\n\n' \
               + self.__time_to_string__()

    def __time_to_string__(self):
        t_localtime = time.localtime(self.timestamp)
        localtime = time.localtime()
        if (t_localtime.tm_year == localtime.tm_year
            and t_localtime.tm_mon == localtime.tm_mon
            and t_localtime.tm_mday == localtime.tm_mday):
            return time.strftime("%H:%M:%S", t_localtime)
        return time.strftime("%Y-%m-%d %H:%M:%S", t_localtime)