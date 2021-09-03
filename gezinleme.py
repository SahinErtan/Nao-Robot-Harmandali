"""
Ilk Hareket Cikildigi anda 9ve adim daire formatinda gezme
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


        posture.goToPosture("StandInit", 0.5)

        for tekrar in range(5):
            Leg = ["LLeg"]
            X = 0.08
            Y = 0.0
            Theta = 0.00
            footSteps = [[X, Y, Theta]]
            timeList = [0.2]
            clearExisting = False
            motion.setFootSteps(Leg, footSteps, timeList, clearExisting)
            motion.waitUntilMoveIsFinished()

            Leg = ["RLeg"]
            X = 0.08
            Y = 0.0
            Theta = 0.00
            footSteps = [[X, Y, Theta]]
            timeList = [0.2]
            clearExisting = False
            motion.setFootSteps(Leg, footSteps, timeList, clearExisting)
            motion.waitUntilMoveIsFinished()



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