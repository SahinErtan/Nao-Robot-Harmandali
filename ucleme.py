"""


Sol ayak ileri - sag ayak suruyerek solun yanina ve ayni anda sag el goguse kaldirilir
Sag ayak geri giderken sag el yana acilir -sol ayak surunerek cekilir
Sol ayak ileri giderken sol el yana acilir - sag ayak yanina cekilir

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
        motion = ALProxy("ALMotion", robotIP, port)
        posture = ALProxy("ALRobotPosture", robotIP, port)

        import uclemeKollar



        leftArmEnable = True
        rightArmEnable = True
        motion.setMoveArmsEnabled(leftArmEnable, rightArmEnable)

        step_time = 0.1

        Leg = ["LLeg"]
        X = 0.04
        Y = 0.0
        Theta = 0.00
        footSteps = [[X, Y, Theta]]
        timeList = [step_time]
        clearExisting = False
        motion.setFootSteps(Leg, footSteps, timeList, clearExisting)

        uclemeKollar.first(robotIP, port)
        motion.waitUntilMoveIsFinished()

        # time.sleep(3)

        Leg = ["RLeg"]
        X = 0.08
        Y = 0.0
        Theta = 0.00
        footSteps = [[X, Y, Theta]]
        timeList = [step_time]
        clearExisting = False
        motion.setFootSteps(Leg, footSteps, timeList, clearExisting)

        uclemeKollar.second(robotIP, port)
        motion.waitUntilMoveIsFinished()

        # time.sleep(3)

        Leg = ["RLeg"]
        X = -0.04
        Y = 0.0
        Theta = 0.00
        footSteps = [[X, Y, Theta]]
        timeList = [step_time]
        clearExisting = False
        motion.setFootSteps(Leg, footSteps, timeList, clearExisting)

        uclemeKollar.third(robotIP, port)
        motion.waitUntilMoveIsFinished()

        # time.sleep(3)

        Leg = ["LLeg"]
        X = -0.08
        Y = 0.0
        Theta = 0.00
        footSteps = [[X, Y, Theta]]
        timeList = [step_time]
        clearExisting = False
        motion.setFootSteps(Leg, footSteps, timeList, clearExisting)

        uclemeKollar.third(robotIP, port)
        motion.waitUntilMoveIsFinished()

        # time.sleep(3)

        Leg = ["LLeg"]
        X = 0.04
        Y = 0.0
        Theta = 0.00
        footSteps = [[X, Y, Theta]]
        timeList = [step_time]
        clearExisting = False
        motion.setFootSteps(Leg, footSteps, timeList, clearExisting)

        uclemeKollar.third(robotIP, port)
        motion.waitUntilMoveIsFinished()

        # time.sleep(3)

        Leg = ["RLeg"]
        X = -0.02
        Y = -0.02
        Theta = 0.00
        footSteps = [[X, Y, Theta]]
        timeList = [step_time]
        clearExisting = False
        motion.setFootSteps(Leg, footSteps, timeList, clearExisting)
        time.sleep(step_time*4)

        uclemeKollar.four(robotIP, port)
        motion.waitUntilMoveIsFinished()
        # uclemeKollar.four(robotIP, port)



    except BaseException, err:
        print"UCLEME HATA"
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

    bs = time.time()
    main(robotIP, port)
    print("Ucleme sure= ", time.time() - bs)
