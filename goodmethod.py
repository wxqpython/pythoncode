#!/usr/bin/env python3
import time
class Date(object):
    def __init__(self, year,mon,day):
        self.year = year
        self.mon = mon
        self.day = day
    @classmethod
    def now(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

class EuroDate(Date):
     def __str__(self):
       return 'year: %s mon:%s day:%s' % (self.year, self.mon,self.day)

e = EuroDate.now()
print(e)
