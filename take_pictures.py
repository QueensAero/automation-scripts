'''automates picture taking for USC 2019. Controls the camera gimbal to take pictures from
multiple angles. Works simulatenously with "camera_pictures.bas" running on a canon camera
with CHDK installed to take pictures at different zooms'''

import MAVLink

def set_servo(pin,pwm):
    MAV.doCommand(MAVLink.MAV_CMD.DO_SET_SERVO,pin,pwm,0,0,0,0,0)


servo_pitch = 9
servo_yaw = 11
servo_camera = 12
gimbal_min = 1100
gimbal_max= 1900
camera_hi = 2100
camera_lo = 1000
point_delay = 3000
trigger_delay = 3000
picture_delay = 16000


print "starting pictures"
print "pointing down"

set_servo(servo_pitch,int(gimbal_min + (gimbal_max-gimbal_min)*90/110))
set_servo(servo_yaw,int(gimbal_min + (gimbal_max-gimbal_min)/2))
Script.Sleep(point_delay)
print "taking pictures"
set_servo(servo_camera,camera_hi)
Script.Sleep(trigger_delay)
set_servo(servo_camera,camera_lo)
Script.Sleep(picture_delay)

print "down"
set_servo(servo_pitch,gimbal_max)
Script.Sleep(point_delay)
set_servo(servo_camera,camera_hi)
print "taking pictures"
Script.Sleep(trigger_delay)
set_servo(servo_camera,camera_lo)
Script.Sleep(picture_delay)

print "right"
set_servo(servo_pitch,int(gimbal_min + (gimbal_max-gimbal_min)*70/110))
set_servo(servo_yaw,gimbal_min)
Script.Sleep(point_delay)
set_servo(servo_camera,camera_hi)
print "taking pictures"
Script.Sleep(trigger_delay)
set_servo(servo_camera,camera_lo)
Script.Sleep(picture_delay)

print "left"
set_servo(servo_yaw,gimbal_max)
Script.Sleep(point_delay)
set_servo(servo_camera,camera_hi)
print "taking pictures"
Script.Sleep(trigger_delay)
set_servo(servo_camera,camera_lo)
Script.Sleep(picture_delay)

print "up"
set_servo(servo_pitch,int(gimbal_min + (gimbal_max-gimbal_min)*70/110))
set_servo(servo_yaw,int(gimbal_min + (gimbal_max-gimbal_min)/2))
Script.Sleep(point_delay)
set_servo(servo_camera,camera_hi)
print "taking pictures"
Script.Sleep(trigger_delay)
set_servo(servo_camera,camera_lo)
Script.Sleep(picture_delay)

print "resetting gimbal"
set_servo(servo_pitch,gimbal_min)


print "done"