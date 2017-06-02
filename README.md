# openmv_ros

ROS driver to OpenMV camera, implementing the ROSSerial protocol. Working on the OpenMV7.

# Generate Messages

Not done yet, generate the standard ROS message then follow the message structure as shown in [openmv_ros/message_example](openmv_ros/message_example). This should not be hard to create the generator. 

Main differences from the ROS message: 
 - Use a wrapper arround ustruct (microPython struct).
 - Less dependencies
 - No numpy support
 - Has a `__str__` method as it does not extend the genpy message class.

# Install

Put all the messages inside your device plus microros.py, then make your main.py program.

# Run

Will be starting the standard ROSSerial node like:

```
roslaunch rosserial_server serial.launch baud:=115200
```

# Status

WIP:
    * Making the rospy interface, Publishers and Subscribers.

Later work: 
    * Making the python ros message generation


# Credits

* Alexis Paques (@AlexisTM)
