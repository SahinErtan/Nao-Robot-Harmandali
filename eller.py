import sys
import time
from naoqi import ALProxy

def main(robotIP, port):
    names = list()
    times = list()
    keys = list()
    robotIP = "127.0.0.1"  # "192.168.11.3"

    port = 9559  # 9559 # Insert NAO port

    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([0.08])
    keys.append([-0.0349066])

    names.append("LElbowYaw")
    times.append([0.08])
    keys.append([-0.236131])

    names.append("LHand")
    times.append([0.08, 0.64])
    keys.append([0.606787, 0.2])

    names.append("LShoulderPitch")
    times.append([0.08])
    keys.append([-1.34362])

    names.append("LShoulderRoll")
    times.append([0.08])
    keys.append([1.19309])

    names.append("LWristYaw")
    times.append([0.08])
    keys.append([1.04417])

    names.append("RElbowRoll")
    times.append([0.08])
    keys.append([0.242431])

    names.append("RElbowYaw")
    times.append([0.08])
    keys.append([-1.03605])

    names.append("RHand")
    times.append([0.08, 0.64])
    keys.append([0.688909, 0.2])

    names.append("RShoulderPitch")
    times.append([0.08])
    keys.append([-1.34857])

    names.append("RShoulderRoll")
    times.append([0.08])
    keys.append([-1.15555])

    names.append("RWristYaw")
    times.append([0.08])
    keys.append([0])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        # motion = ALProxy("ALMotion", IP, 9559)
        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
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
