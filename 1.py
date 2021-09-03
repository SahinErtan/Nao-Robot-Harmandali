"""
https://www.youtube.com/watch?v=9ha-Og68IeY&ab_channel=BornovaBelediyesi    Duz ve Agir Atlama

https://www.youtube.com/watch?v=mINL2iJB9DM&ab_channel=ZeybekSanat   (Tercih Edilen)
https://www.youtube.com/watch?v=yue7BCPQaG0&ab_channel=ZeybekSanat  (Tercih Edilen)

https://www.youtube.com/watch?v=C4vfq-uXeig&ab_channel=BornovaBelediyesi    Kadin Tavri
https://www.youtube.com/watch?v=4QBN7LtvlaM&ab_channel=BornovaBelediyesi    Kadin Tavri



--Gezinleme--

--Duz Kollu Figur--
ucleme
duzfigur
bitiris (herhangibiri)
(En az 2 tekrar)

Esme
Ters Esme


"""



import sys
import time
from naoqi import ALProxy

def main(robotIP, port):
    names = list()
    times = list()
    keys = list()
    robotIP = "127.0.0.1"  # "192.168.11.3"

    port = 9559  # 9559 # Insert NAO port
    try:
        ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
    except Exception, e:
        print("Could not create a proxy to ALTextToSpeech")


    ttsProxy.say("Hey check out my guitar skills!")

    try:
        motion = ALProxy("ALMotion", robotIP, port)
    except BaseException, err:
        print"hatataa"
        print err


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

    main(robotIP, port)

