# openmv_ros

ROS driver to OpenMV camera, implementing the ROSSerial protocol. Working on the OpenMV7.

# Generate Messages

Not done yet, generate the standard ROS message then follow the message structure as shown in [openmv_ros/message_example](openmv_ros/message_example). This should not be hard to create the generator. 

Main differences from the ROS message: 
 - Python3 
 - Use a wrapper arround ustruct (microPython struct).
 - Less dependencies
 - No numpy support
 - Has a `__str__` method as it does not extend the genpy message class, can be solved.

# Install

Put all the messages inside your device plus microros.py, then make your main.py program.

# Run

Will be starting the standard ROSSerial node like:

```
roslaunch rosserial_server serial.launch baud:=115200 port:=/dev/ttyACM0
```

# Contributing

Branch, send a PR, thanks!

# Status

WIP:
    * Making the rospy interface, Publishers and Subscribers + default messages I need (TopicInfo, Tag, Tags, ROI)

Later work: 
    * ROS message generation
    * Service implementation
    * Make the generic message to inherit from

# Credits

* Alexis Paques (@AlexisTM)
