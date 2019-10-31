import dronekit_sitl

class SITLHelper:
    """
    Wrapper class for using simulation in the loop (SITL) in a more intuitive way.
    
    ...

    Attributes
    ----------
    sitl : dronekit_sitl.sitl
        the simulated vehicle
    connection_string : string
        the string that describes how to connect to this vehicle using dronekit
    
    Methods
    -------
    stop()
        Stop the simulation
    """
    def __init__(self, lat=44.226463, lon=-76.489577):
        """
        Initialize the Simulation in the loop simulator

        Parameters
        ----------
        lat : float
            latitude to start the vehicle at, defaults to the baseball diamond near Queen's (default=44.226463)
        lon : float
            longitude to start the vehicle at, defaults to the baseball diamond near Queen's (default=-46.489577)
        """
        self.sitl = dronekit_sitl.start_default(lat=lat, lon=lon)
        self.connection_string = self.sitl.connection_string()
    
    def stop(self):
        """ stop the simulation """
        self.sitl.stop()
