# openmv_ros

> Due to the chnage of idea management-wise at the time and the lack of hardware available to me, this is unmaintained.
> Refer to the fallback solution ;)

I changed company and do nto have the hardware anymore.

## Fallback solution

You can do the communication using the serial CDC driver of the OpenMV board.

On the OpenMV camera:
```python
import sensor, image, time, math, pyb

usb_vcp = pyb.USB_VCP()
usb_vcp.setinterrupt(-1)

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.VGA)
sensor.set_windowing((640, 60))
sensor.skip_frames(time = 125)
sensor.set_auto_gain(False, value=10)
sensor.set_auto_whitebal(False)
sensor.set_auto_exposure(False, value=125)
sensor.set_colorbar(False)

while True:
    clock.tick()
    img = sensor.snapshot()
    codes = img.find_barcodes()

    for code in codes:
        text = "".join([code.payload(), "\t", str(code.quality()), "\n"])
        usb_vcp.send(text, timeout=usb_timeout)

    if len(codes) == 0:
        usb_vcp.send("\n", timeout=usb_timeout)
```

Then you read the data from the computer:

```python
    def spinonce(self):
        """Spin to read."""
        lines = []
        received = False

        while self.serial.in_waiting:
            line = self.serial.readline()
            lines.append(line)
            received = True

        codes = []
        if received:
            for line in lines:
                code = self.parseline(line)
                if code is not None:
                    codes.append(code)

            self.msg.header.stamp = (rospy.Time.now() - self.delay)
            self.msg.barcodes = codes
            self.barcode_to_world(self.msg)
            self.topic.publish(self.msg)
``` 

# How it should look like is below

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
