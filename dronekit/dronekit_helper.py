from dronekit import LocationLocal, connect, VehicleMode, LocationGlobalRelative
from haversine import haversine, Unit
import time


def distance(p1, p2):
    """
    Calculates the distance between p1 and p2 in meters

    Parameters
    ----------
    p1 : (float, float)
        first point, tuple of form (latitude, longitude) in degrees
    p2 : (float, float)
        second point, same format as p1
    """
    return haversine(p1, p2, Unit.METERS)

class DronkitHelper:
    """
    Wrapper class for using dronekit in a more intuitive way.
    
    ...

    Attributes
    ----------
    vehicle : dronekit.vehicle
        the UAV that is controlled by the methods in this class
    
    Methods
    -------
    arm_and_takeoff(target_alt)
        Arm the vehicle (if possible) and take off to the target altitude
    fly_to(lat, lon, rel_alt=0, speed=5)
        Fly to a waypoint given by lat, lon and specified relative altitude and speed
    rtl(speed = 5)
        Return to launch and land at specified speed
    close()
        safe-close of the vehicle connection, checking for pending messages
    """

    def __init__(self, connection_string):
        """ connect to vehicle given by connection_string, blocks until connected """
        self.vehicle = connect(connection_string, wait_ready=True)

    def arm_and_takeoff(self, target_alt):
        """
        Arms vehicle and takes off to a target altitude

        Parameters
        ----------
        target_alt : float
            altitude to takeoff to
        """

        print("Pre-arm checks")
        # wait for self.vehicle to be armable/initialized
        while not self.vehicle.is_armable:
            print("Waiting for self.vehicle to initialize")
            time.sleep(1)
        
        print("Arming motors")
        # set self.vehicle to guided mode and arm
        self.vehicle.mode = VehicleMode("GUIDED")
        self.vehicle.armed = True

        # confirm armed
        while not self.vehicle.armed:
            print("Waiting for arming ...")
            time.sleep(1)

        print("Taking off")
        self.vehicle.simple_takeoff(target_alt)

        # Wait until the self.vehicle reaches the target altitude before returning
        while self.vehicle.location.global_relative_frame.alt <= target_alt*0.95:
            print("Altitude: {}".format(self.vehicle.location.global_relative_frame.alt))
            time.sleep(1)
        print("Reached target altitude")

    def fly_to(self, lat, lon, rel_alt=0, speed=5):
        """
        Flies to a waypoint at specified relative alititude or speed

        Parameters
        ----------
        lat : float
            latitude to fly to
        lon : float
            longitude to fly to
        rel_alt : float
            relative altitude (to the home altitude) to fly to the waypoint at(default 0)
        speed : float
            speed in m/s to fly to the waypoint at (default 5)
        """

        if self.vehicle.mode != VehicleMode("GUIDED"):
            print("CAN'T COMPLETE FLY TO, self.vehicle not in guided mode")
        
        self.vehicle.airspeed = speed
        goal = LocationGlobalRelative(lat, lon, rel_alt)

        self.vehicle.simple_goto(goal)

        dist_to_goal = distance((self.vehicle.location.global_frame.lat, 
                                 self.vehicle.location.global_frame.lon), (lat, lon))

        while dist_to_goal > 1:
            print("Distance to waypoint: {}".format(dist_to_goal))
            time.sleep(2)
            dist_to_goal = distance((self.vehicle.location.global_frame.lat, 
                                     self.vehicle.location.global_frame.lon), (lat, lon))

        print("Reached waypoint")

    def rtl(self, speed = 5):
        """ 
        Return to launch and land

        Parameters
        ----------
        speed : float
            speed to return home at (default 5)
        """

        self.vehicle.airspeed = speed

        self.vehicle.mode = VehicleMode("RTL")

        home = self.__get_home_location()
        
        while distance((self.vehicle.location.global_frame.lat, self.vehicle.location.global_frame.lon), 
                           home) > 1:
            print("Flying home: {}m to go".format(distance((self.vehicle.location.global_frame.lat, 
                                                            self.vehicle.location.global_frame.lon), home)))            
            time.sleep(2)
        
        print("landing")


    
    def close(self):
        """ Safe-close the connection to the vehicle, checking that all commands are flushed """
        
        self.vehicle.close()
    
    def __get_home_location(self):
        cmds = self.vehicle.commands
        cmds.download()
        cmds.wait_ready()

        return (self.vehicle.home_location.lat, self.vehicle.home_location.lon)
