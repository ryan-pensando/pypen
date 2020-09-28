# Copyright (c) 2020, Pensando Systems
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# Author: Ryan Tischer ryan@pensando.io



import time
import random
import socket
from datetime import datetime, timedelta


def return_time(now, t5):
    # return_time formats string for use with PSM API start and endtime

    fmonth = now.strftime("%m")
    day = now.strftime("%d")
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")

    tDash = '{y}-{fm}-{d}T{h}:{min}:{s}Z'.format(
        y=now.year, d=day, h=hour, min=minute, s=second, fm = fmonth)

    fmonth = t5.strftime("%m")
    hour = t5.strftime("%H")
    minute = t5.strftime("%M")
    second = t5.strftime("%S")

    tminusDash =  '{y}-{fm}-{d}T{h}:{min}:{s}Z'.format(
        y=now.year, d=day, h=hour, min=minute, s=second, fm = fmonth)

    return tDash, tminusDash


def sendLog(host, port, msg):
    message = msg.encode('utf-8')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(bytes(msg, "utf-8"), (host, port))
    # sock = socket()
    # sock.connect((host, port))
    # sock.sendall(message)
    sock.close()


def randomLine(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num + 2): continue
        line = aline
    return line


def calcDate(direction,ndays,dateFormat="n"):
    if dateFormat == "T":
        if direction == "past":
            return f"{datetime.now() - timedelta(days=ndays):%Y-%m-%dT%H:%M:%S}"
        else:
            return f"{datetime.now() + timedelta(days=ndays):%Y/%m/%d %H:%M:%S}"
    else:
        if direction == "past":
            return f"{datetime.now() - timedelta(days=ndays):%Y/%m/%d %H:%M:%S}"
        else:
            return f"{datetime.now() + timedelta(days=ndays):%Y/%m/%d %H:%M:%S}"

def strTimeProp(start, end, dateFormat, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, dateFormat))
    etime = time.mktime(time.strptime(end, dateFormat))

    ptime = stime + prop * (etime - stime)
    #print(time.strftime(format, time.localtime(ptime)))
    return time.strftime(dateFormat, time.localtime(ptime))


def randomDate(start, end, prop,dateFormat='%Y/%m/%d %H:%M:%S'):
    return strTimeProp(start, end, dateFormat, prop).strip()


def main():
    pass

if __name__ == "__main__":
    main()
