'''Script to automate the dropper mechanism for competition - USC 2019 '''
import MAVLink

def set_servo(pin,pwm):
    MAV.doCommand(MAVLink.MAV_CMD.DO_SET_SERVO,pin,pwm,0,0,0,0,0)



servo_low = 9
servo_mid = 11
servo_hi = 10
open_pwm = 2000
close_pwm = 1300

print "dropping"
set_servo(servo_low,open_pwm)
Script.Sleep(500)
print "closing"
set_servo(servo_low,close_pwm)

Script.Sleep(1000)

print "moving down"
set_servo(servo_mid,open_pwm)
Script.Sleep(500)
print "closing"
set_servo(servo_mid,close_pwm)

Script.Sleep(1000)

print "moving down 2"
set_servo(servo_hi,open_pwm)
Script.Sleep(500)
print "closing"
set_servo(servo_hi,close_pwm)

print "done"




