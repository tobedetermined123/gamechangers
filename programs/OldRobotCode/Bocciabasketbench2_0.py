#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B,  positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,  positive_direction=Direction.COUNTERCLOCKWISE)
lift_motor = Motor(Port.A)
forklift_motor = Motor(Port.D) 

robot = DriveBase(left_motor, right_motor, wheel_diameter=94.2, axle_track=94)
robot.settings(straight_speed=200 , straight_acceleration=50, turn_rate=150, turn_acceleration=200)
ev3.screen.draw_text(50, 60, "bot go brrrrr")
ev3.speaker.beep()

gyro_sensor = GyroSensor(Port.S2, Direction.COUNTERCLOCKWISE)

def gyro_turn(angle, speed):
    gyro_sensor.reset_angle(0)
    if angle < 0:
        while gyro_sensor.angle() > angle:
            left_motor.run(speed=(-1 * speed))
            right_motor.run(speed=speed)
            wait(10)
    elif angle > 0:  
        while gyro_sensor.angle() < angle:
            left_motor.run(speed=speed)
            right_motor.run(speed=(-1 * speed))
            wait(10)  
    else:
        print("Error: no angle chosen")

    left_motor.brake()
    right_motor.brake() 

def gyro_straight(distance, robotSpeed):
    robot.reset() 
    gyro_sensor.reset_angle(0)

    PROPORTIONAL_GAIN = 1.1
    if distance < 0: # move backwards
        while robot.distance() > distance:
            reverseSpeed = -1 * robotSpeed        
            angle_correction = -1 * PROPORTIONAL_GAIN * gyro_sensor.angle()
            robot.drive(reverseSpeed, angle_correction) 
            wait(10)
    elif distance > 0: # move forwards             
        while robot.distance() < distance:
            angle_correction = -1 * PROPORTIONAL_GAIN * gyro_sensor.angle()
            robot.drive(robotSpeed, angle_correction) 
            wait(10)            
    robot.stop()




gyro_straight(50, 150)
gyro_turn(15, 100)
gyro_straight(610, 150)
gyro_turn(-7, 100)
wait(100)
gyro_straight(200, 150)
forklift_motor.run_angle(speed=25198, rotation_angle=1390)
forklift_motor.run_angle(speed=25198, rotation_angle=-1390)
gyro_straight(-70, 150)
gyro_turn(-37, 100)
gyro_straight(70, 150)
forklift_motor.run_angle(speed=25198, rotation_angle=10000)
gyro_straight(-100, 150)
gyro_turn(-90, 100)
gyro_straight(130, 150)
gyro_turn(40, 100)
gyro_straight(500, 250)
ev3.speaker.beep()


#RIP Hunter, Josh, and Zhongren, Who All Left The Group
