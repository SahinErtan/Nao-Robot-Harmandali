import sys
import time
from naoqi import ALProxy

def first(robotIP, port):
    names = list()
    times = list()
    keys = list()
    robotIP = "127.0.0.1"  # "192.168.11.3"

    port = 9559  # 9559 # Insert NAO port

    ETime=1.7

    names.append("LElbowRoll")
    times.append([ETime])
    keys.append([[-0.0477997, [3, -0.32, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([ETime])
    keys.append([[-0.0197165, [3, -0.32, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([ETime])
    keys.append([[0, [3, -0.32, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([ETime])
    keys.append([[1.3185, [3, -0.32, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([ETime])
    keys.append([[0.617298, [3, -0.32, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([ETime])
    keys.append([[0, [3, -0.32, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([ETime])
    keys.append([[0.048025, [3, -0.32, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([ETime])
    keys.append([[0.0197301, [3, -0.32, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([ETime])
    keys.append([[0, [3, -0.32, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([ETime])
    keys.append([[1.32917, [3, -0.32, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([ETime])
    keys.append([[-0.618866, [3, -0.32, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([ETime])
    keys.append([[0, [3, -0.32, 0], [3, 0, 0]]])

    try:
      motion = ALProxy("ALMotion", robotIP, port)
      motion.angleInterpolationBezier(names, times, keys)
      print("uclemeKollarFirstCalisti")
    except BaseException, err:
      print err




def second(robotIP, port):
    names = list()
    times = list()
    keys = list()
    robotIP = "127.0.0.1"  # "192.168.11.3"

    port = 9559  # 9559 # Insert NAO port

    ETime=1.7

    names.append("LElbowRoll")
    times.append([ETime])
    keys.append([[-0.0465211, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([ETime])
    keys.append([[-0.0236891, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([ETime])
    keys.append([[0, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([ETime])
    keys.append([[1.32422, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([ETime])
    keys.append([[0.617622, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([ETime])
    keys.append([[0, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([ETime])
    keys.append([[1.52951, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([ETime])
    keys.append([[0.0238748, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([ETime])
    keys.append([[0.19, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([ETime])
    keys.append([[0.283031, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([ETime])
    keys.append([[-0.16174, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([ETime])
    keys.append([[0, [3, -0.0533333, 0], [3, 0, 0]]])


    try:
      motion = ALProxy("ALMotion", robotIP, port)
      motion.angleInterpolationBezier(names, times, keys)
      print("uclemeKollarSecondCalisti")
    except BaseException, err:
      print err




def third(robotIP, port):
    names = list()
    times = list()
    keys = list()
    robotIP = "127.0.0.1"  # "192.168.11.3"

    port = 9559  # 9559 # Insert NAO port

    ETime=1.7

    names.append("LElbowRoll")
    times.append([ETime])
    keys.append([[-0.0444707, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([ETime])
    keys.append([[-0.0237066, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([ETime])
    keys.append([[0, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([ETime])
    keys.append([[1.32227, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([ETime])
    keys.append([[0.620564, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([ETime])
    keys.append([[0, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([ETime])
    keys.append([[0.232124, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([ETime])
    keys.append([[-1.04454, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([ETime])
    keys.append([[0.69, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([ETime])
    keys.append([[-1.35148, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([ETime])
    keys.append([[-1.16351, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([ETime])
    keys.append([[0, [3, -0.0533333, 0], [3, 0, 0]]])


    try:
      motion = ALProxy("ALMotion", robotIP, port)
      motion.angleInterpolationBezier(names, times, keys)
      print("uclemeKollarThirdCalisti")
    except BaseException, err:
      print err



def four(robotIP, port):
    names = list()
    times = list()
    keys = list()
    robotIP = "127.0.0.1"  # "192.168.11.3"

    port = 9559  # 9559 # Insert NAO port

    ETime=1.0

    names.append("LElbowRoll")
    times.append([ETime])
    keys.append([[-0.040162, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([ETime])
    keys.append([[-0.243791, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([ETime])
    keys.append([[0.61, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([ETime])
    keys.append([[-1.34762, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([ETime])
    keys.append([[1.19647, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([ETime])
    keys.append([[1.05032, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([ETime])
    keys.append([[0.232124, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([ETime])
    keys.append([[-1.04454, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([ETime])
    keys.append([[0.69, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([ETime])
    keys.append([[-1.35148, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([ETime])
    keys.append([[-1.16351, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([ETime])
    keys.append([[0, [3, -0.173333, 0], [3, 0, 0]]])

    try:
      motion = ALProxy("ALMotion", robotIP, port)
      motion.angleInterpolationBezier(names, times, keys)
      print("uclemeKollarFourCalisti")
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

    first(robotIP="127.0.0.1", port=9559)
    time.sleep(3)
    four(robotIP="127.0.0.1", port=9559)
    time.sleep(3)
    four(robotIP="127.0.0.1", port=9559)