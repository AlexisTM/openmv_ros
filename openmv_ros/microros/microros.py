import struct

class rospy(object):
  _publishers = []
  _subscribers = []

  def __init__(self):
    self.usb = pyb.USB_VCP()
    self.usb.setinterrupt(-1)


  def spinOnce(self):   
    # Handle serial communication
    if self.usb.any():
        header = bytes(4)
        read_bytes = self.usb.readinto(header)

        if read_bytes < len(header):
            # flush if we did not have the correct data
            self.usb.readall()
            return

        if header[0] != 0xff:
            self.usb.readall()
            return

        if header[1] != 0xfe: # Indigo+
            self.usb.readall()
            return

        dataLength = int(header[2]) + int(header[3])
        
        if header[5] != checksum(buff):
            self.usb.readall()
            return

        data = bytes(dataLength)
        read_bytes = self.usb.readinto(data)

        if read_bytes < len(data):
            self.usb.readall()
            return

  def advertise(self, _publisher):
    pass

  def subscribe(self, _subscriber):
    pass

  def checksum(self, buff):
    _result = 255 - (sum(buff)%256)
    return _result

class Publisher(object):
  topic_id = None

  def __init__(self, topic_name, datatype)
    pass

  def publish(self):
    pass

class Subscriber(object):
  topic_id = None

  def __init__(self, topic_name, datatype, callback)
    pass


class Struct:

    def __init__(self, format):
        self.format = format
        self.size = calcsize(format)

    def unpack(self, buf):
        return unpack(self.format, buf)

    def pack(self, *vals):
        return pack(self.format, *vals)