#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""
Ucleme sonrasi yapilan 9lamanin geri kalani Bas-Cek-Salla
"""

import sys
import time
import motion
from naoqi import ALProxy
import almath


def main(robotIP, port):

    names = list()
    times = list()
    keys = list()
    robotIP = "127.0.0.1"  # "192.168.11.3"

    port = 9559  # 9559 # Insert NAO port

    try:
        motionProxy = ALProxy("ALMotion", robotIP, port)
        posture = ALProxy("ALRobotPosture", robotIP, port)
        motionProxy.wakeUp()
        import ucleme
        import uclemeKollar
        ucleme.main(robotIP,port)
        # import baslangicFigur
        # baslangicFigur.main(robotIP, port)

    except BaseException, err:
        print"hatataa"
        print err


    for tekrar in range(2):
        uclemeKollar.four(robotIP, port)

        # Sag Ayak Havada

        frame = motion.FRAME_WORLD
        axisMask = almath.AXIS_MASK_ALL  # full control
        useSensorValues = False

        # Lower the Torso and move to the side
        effector = "Torso"
        initTf = almath.Transform(motionProxy.getTransform(effector, frame, useSensorValues))
        deltaTf = almath.Transform(0.0, 0.045, -0.025)  # x, y, z
        targetTf = initTf * deltaTf
        path = list(targetTf.toVector())
        atimes = 1.0  # seconds
        motionProxy.transformInterpolations(effector, frame, path, axisMask, atimes)


        # RLeg motion
        effector = "RLeg"
        initTf = almath.Transform()

        try:
            initTf = almath.Transform(motionProxy.getTransform(effector, frame, useSensorValues))
        except Exception, errorMsg:
            print
            str(errorMsg)
            print
            "This example is not allowed on this robot."
            exit()

        # rotation Z
        deltaTf = almath.Transform(0.0, 0.0, 0.1) * almath.Transform().fromRotZ(0.0 * almath.TO_RAD)
        targetTf = initTf * deltaTf
        path = list(targetTf.toVector())
        atimes = 1.0  # seconds

        motionProxy.transformInterpolations(effector, frame, path, axisMask, atimes)
        time.sleep(2)



       # Sol Ayak Havada

        posture.goToPosture("StandInit", 1.0)
        uclemeKollar.four(robotIP, port)


        try:
            motionProxy.angleInterpolationBezier(names, times, keys)
        except BaseException, err:
            print
            err

        frame = motion.FRAME_WORLD
        axisMask = almath.AXIS_MASK_ALL  # full control
        useSensorValues = False

        # Lower the Torso and move to the side
        effector = "Torso"
        initTf = almath.Transform(motionProxy.getTransform(effector, frame, useSensorValues))
        deltaTf = almath.Transform(0.0, -0.045, -0.025)  # x, y, z
        targetTf = initTf * deltaTf
        path = list(targetTf.toVector())
        times = 1.0  # seconds
        motionProxy.transformInterpolations(effector, frame, path, axisMask, times)



        # LLeg motion
        effector = "LLeg"
        initTf = almath.Transform()

        try:
            initTf = almath.Transform(motionProxy.getTransform(effector, frame, useSensorValues))
        except Exception, errorMsg:
            print
            str(errorMsg)
            print
            "This example is not allowed on this robot."
            exit()

        # rotation Z
        deltaTf = almath.Transform(0.0, 0.0, 0.1) * almath.Transform().fromRotZ(0.0 * almath.TO_RAD)
        targetTf = initTf * deltaTf
        path = list(targetTf.toVector())
        times = 1.0  # seconds

        motionProxy.transformInterpolations(effector, frame, path, axisMask, times)
        time.sleep(2)


        deltaTf = almath.Transform(0.0, 0.0, 0.0) * almath.Transform().fromRotZ(0.0 * almath.TO_RAD)
        targetTf = initTf * deltaTf
        path = list(targetTf.toVector())
        motionProxy.transformInterpolations(effector, frame, path, axisMask, times)



        posture.goToPosture("StandInit", 1.0)
        uclemeKollar.four(robotIP, port)




    # Sag Ayak Havada


    frame = motion.FRAME_WORLD
    axisMask = almath.AXIS_MASK_ALL  # full control
    useSensorValues = False

    # Lower the Torso and move to the side
    effector = "Torso"
    initTf = almath.Transform(motionProxy.getTransform(effector, frame, useSensorValues))
    deltaTf = almath.Transform(0.0, 0.045, -0.025)  # x, y, z
    targetTf = initTf * deltaTf
    path = list(targetTf.toVector())
    atimes = 2.0  # seconds
    motionProxy.transformInterpolations(effector, frame, path, axisMask, atimes)



    # RLeg motion
    effector = "RLeg"
    initTf = almath.Transform()

    try:
        initTf = almath.Transform(motionProxy.getTransform(effector, frame, useSensorValues))
    except Exception, errorMsg:
        print
        str(errorMsg)
        print
        "This example is not allowed on this robot."
        exit()



    # rotation Z
    deltaTf = almath.Transform(0.0, 0.0, 0.1) * almath.Transform().fromRotZ(0.0 * almath.TO_RAD)
    targetTf = initTf * deltaTf
    path = list(targetTf.toVector())
    atimes = 2.0  # seconds

    motionProxy.transformInterpolations(effector, frame, path, axisMask, atimes)

    time.sleep(3)


    deltaTf = almath.Transform(0.0, 0.0, 0.0) * almath.Transform().fromRotZ(0.0 * almath.TO_RAD)
    targetTf = initTf * deltaTf
    path = list(targetTf.toVector())
    motionProxy.transformInterpolations(effector, frame, path, axisMask, atimes)


    """

    posture.goToPosture("StandInit", 0.5)
    uclemeKollar.four(robotIP, port)
    # Sol Ayak Havada


    try:
        motionProxy.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print
        err

    frame = motion.FRAME_WORLD
    axisMask = almath.AXIS_MASK_ALL  # full control
    useSensorValues = False

    # Lower the Torso and move to the side
    effector = "Torso"
    initTf = almath.Transform(motionProxy.getTransform(effector, frame, useSensorValues))
    deltaTf = almath.Transform(0.0, -0.045, -0.025)  # x, y, z
    targetTf = initTf * deltaTf
    path = list(targetTf.toVector())
    times = 1.0  # seconds
    motionProxy.transformInterpolations(effector, frame, path, axisMask, times)

    # LLeg motion
    effector = "LLeg"
    initTf = almath.Transform()

    try:
        initTf = almath.Transform(motionProxy.getTransform(effector, frame, useSensorValues))
    except Exception, errorMsg:
        print
        str(errorMsg)
        print
        "This example is not allowed on this robot."
        exit()

    # rotation Z
    deltaTf = almath.Transform(0.0, 0.0, 0.1) * almath.Transform().fromRotZ(0.0 * almath.TO_RAD)
    targetTf = initTf * deltaTf
    path = list(targetTf.toVector())
    times = 2.0  # seconds

    motionProxy.transformInterpolations(effector, frame, path, axisMask, times)
    time.sleep(3)

    deltaTf = almath.Transform(0.0, 0.0, 0.0) * almath.Transform().fromRotZ(0.0 * almath.TO_RAD)
    targetTf = initTf * deltaTf
    path = list(targetTf.toVector())
    motionProxy.transformInterpolations(effector, frame, path, axisMask, times)

    """




    # posture.goToPosture("StandInit", 0.5)
    # uclemeKollar.four(robotIP, port)




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
    print("Duz Figur sure= ",time.time()-bs)

