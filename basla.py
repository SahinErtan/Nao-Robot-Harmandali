import time
import sys
from naoqi import ALProxy

import baslangicFigur
import ucleme
import duzfigur
import esme
import bitiris
import atik
import finalHareketi



def main(robotIP, port):
    robotIP = "127.0.0.1"  # "192.168.11.3"

    port = 9559  # 9559 # Insert NAO port



    try:
        aup = ALProxy("ALAudioPlayer", robotIP, port)
        file = aup.post.playFile("Harmandal.wav")
        aup.stop(file)
        motion = ALProxy("ALMotion", robotIP, port)
        motion.wakeUp()
        motion.moveTo(0.4, 0.4, 1.00)

        time.sleep(2)
        bs = time.time()

        abs = time.time()
        baslangicFigur.main("127.0.0.1", 9559)

        # time.sleep(3)

        duzfigur.main("127.0.0.1", 9559)
        # bitiris.bitiris_normal()
        # bitiris.bitiris_yerde()
        print("duz figur sure = ", time.time() - abs)
        fs = time.time()
        print("Tum sure=", fs - bs)

        # time.sleep(2)

        abs = time.time()
        # ucleme.main("127.0.0.1", 9559)
        esme.esme()
        esme.ters_esme()
        bitiris.bitiris_kollu()
        print("esme sure = ", time.time() - abs)
        fs = time.time()
        print("Tum sure=", fs - bs)

        # time.sleep(3)
        motion.moveTo(0.4, 0.4, 1.00)

        abs = time.time()
        ucleme.main("127.0.0.1", 9559)
        atik.atik()
        bitiris.bitiris_yerde()
        print("atik sure = ", time.time() - abs)
        fs = time.time()
        print("Tum sure=", fs - bs)

        # time.sleep(3)
        motion.moveTo(0.4, 0.4, 1.00)

        abs = time.time()
        ucleme.main("127.0.0.1", 9559)
        finalHareketi.final()
        print("final sure = ", time.time() - abs)

        fs = time.time()

        print("Tum sure=", fs - bs)




        time.sleep(30)
        aup.stop(file)

    except BaseException, err:
        print"basla Hata"
        print err
        aup.stop(file)




if __name__ == "__main__":

    robotIP = "127.0.0.1"  # "192.168.11.3"

    port = 9559  # 9559 # Insert NAO port

    if len(sys.argv) <= 1:
        print"(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    time.sleep(2)
    main(robotIP, port)

