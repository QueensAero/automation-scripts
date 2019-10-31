""" Example program to introduce basic things that can be done using Dronekit. The imports
    sitl_helper and dronekit_helper are used as wrapper classes around the Dronekit and
    dronkit_sitl libraries, and provide some additional helper functions. """

from dronekit_helper import DronekitHelper
from sitl_helper import SITLHelper
import time

# start the simulator
print("Starting simulator (SITL)")
sitl_helper = SITLHelper(lat=44.226463, lon=-76.489577)

# connect to the Vehicle.
print("Connecting to vehicle on: %s" % sitl_helper.connection_string)
dk = DronekitHelper(sitl_helper.connection_string)

# get and print some vehicle attributes (state)
print(" Get some vehicle attribute values:")
print(" GPS: %s" % dk.vehicle.gps_0)
print(" Battery: %s" % dk.vehicle.battery)
print(" Last Heartbeat: %s" % dk.vehicle.last_heartbeat)
print(" Is Armable?: %s" % dk.vehicle.is_armable)
print(" System status: %s" % dk.vehicle.system_status.state)
print(" Mode: %s" % dk.vehicle.mode.name)    # settable

# wait for 20 seconds. During this time, you can attempt to connect to the simulator in
# mission planner, by selecting TCP, 127.0.0.1 (localhost) for the IP address and 5763
# as the remote port
time.sleep(1)

# arm the UAV a takeoff to an altitude of 10 metres
dk.arm_and_takeoff(10)

# fly to latitude, longitude given at a relative altitude of 14m and speed 3 m/s
# relative alititude means relative to the home location
dk.fly_to(44.226705, -76.489219, rel_alt=14, speed=3)

# return to launch, at a speed of 10 m/s
dk.rtl(speed=10)

time.sleep(25)

# close vehicle object before exiting script this is important becuase it 
# makes sure any commands are flushed (sent) before exiting the script
dk.close()

# shut down simulator
sitl_helper.stop()
print("Completed")