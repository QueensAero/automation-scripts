import MAVLink

def set_servo(pin,pwm):
    MAV.doCommand(MAVLink.MAV_CMD.DO_SET_SERVO,pin,pwm,0,0,0,0,0)


servo_low = 9
servo_mid = 10
servo_hi = 11
open_pwm = 2000
close_pwm = 1300

print "dropping"
set_servo(servo_low,open_pwm)
Script.Sleep(500)
set_servo(servo_low,close_pwm)

Script.Sleep(1000)

print "moving down"
set_servo(servo_mid,open_pwm)
Script.Sleep(500)
set_servo(servo_mid,close_pwm)

Script.Sleep(1000)


set_servo(servo_hi,open_pwm)
Script.Sleep(500)
set_servo(servo_hi,close_pwm)

print "done"




