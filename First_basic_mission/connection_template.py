from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import argparse


parser = argparse.ArgumentParser(description='commands')
parser.add_argument('--connect')
args = parser.parse_args()

connection_string = args.connect

vehicle = connect(connection_string, wait_ready=True)


# takeoff-function
def arm_and_takeoff(tgt_altitude):
    print("Arming drone")
    
    while not vehicle.is_armable:
        time.sleep(1)
        
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    
    while not vehicle.armed: time.sleep(1)
    
    print("Takeoff")
    vehicle.simple_takeoff(tgt_altitude)
    
    
    while True:
        altitude = vehicle.location.global_relative_frame.alt
        
        if altitude >= tgt_altitude -1:
            print("Altitude reached")
            break
            
        time.sleep(1)
        
        
time.sleep(10)

arm_and_takeoff(10)


vehicle.airspeed = 7

# Go to waypoint1
print ("go to waypoint1")
wp1 = LocationGlobalRelative(35.9872609, -95.8753037, 10)

vehicle.simple_goto(wp1)


time.sleep(30)

#Coming back
print("Coming back")
vehicle.mode = VehicleMode("RTL")

time.sleep(40)

#-- Close connection
print("Closing connection")
vehicle.close()

