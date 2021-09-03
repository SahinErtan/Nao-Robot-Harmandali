import sys
import time
from naoqi import ALProxy

def main(robotIP, port):
    names = list()
    times = list()
    keys = list()
    robotIP = "127.0.0.1"  # "192.168.11.3"

    port = 9559  # 9559 # Insert NAO port

    ETime=0.1   #0.16

    names.append("LAnklePitch")
    times.append([ETime])
    keys.append([[0.00272999, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([ETime])
    keys.append([[-0.00367502, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([ETime])
    keys.append([[-0.0397162, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([ETime])
    keys.append([[-0.0145191, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([ETime])
    keys.append([[0, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([ETime])
    keys.append([[0.00829946, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([ETime])
    keys.append([[0.0441114, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([ETime])
    keys.append([[-0.00727537, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([ETime])
    keys.append([[-0.000921135, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([ETime])
    keys.append([[1.3177, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([ETime])
    keys.append([[0.623187, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([ETime])
    keys.append([[0.00176798, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([ETime])
    keys.append([[0.00140243, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([ETime])
    keys.append([[9.52571e-05, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([ETime])
    keys.append([[0.0396621, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([ETime])
    keys.append([[0.014533, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([ETime])
    keys.append([[0, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([ETime])
    keys.append([[-0.00244095, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([ETime])
    keys.append([[-0.0533432, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([ETime])
    keys.append([[-0.00727537, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([ETime])
    keys.append([[-0.000568401, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([ETime])
    keys.append([[1.3264, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([ETime])
    keys.append([[-0.625114, [3, -0.0533333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([ETime])
    keys.append([[0.00176942, [3, -0.0533333, 0], [3, 0, 0]]])

    try:
      motion = ALProxy("ALMotion", robotIP, port)
      motion.wakeUp()
      motion.angleInterpolationBezier(names, times, keys)
      print("BaslangicFigurCalisti")
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

    main(robotIP="127.0.0.1", port=9559)