import struct

class rospy(object):
  _publishers = []
  _subscribers = []
  _toPublish = []

  def __init__(self):
    self.usb = pyb.USB_VCP()
    self.usb.setinterrupt(-1)

  def spinOnce(self):   
    # Handle serial communication
    """
      1st Byte - Sync Flag (Value: 0xff)
      2nd Byte - Sync Flag / Protocol version
      3rd Byte - Message Length (N) - Low Byte
      4th Byte - Message Length (N) - High Byte
      5th Byte - Checksum over message length
      6th Byte - Topic ID - Low Byte - 0
      7th Byte - Topic ID - High Byte - 1
      N Bytes  - Serialized Message Data - (2 + N-1)
      Byte N+8 - Checksum over Topic ID and Message Data N+2
    """

    # Publishers
    while len(self._toPublish) > 0:
        msg = self._toPublish.pop()

    # Subscribers
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

        dataLength = int(header[2]) + int(header[3])*256
        
        if header[4] != self.checksum(header):
            self.usb.readall()
            return

        # Topic ID + checksum => dataLength+3
        message_data = bytes(dataLength+3)
        read_bytes = self.usb.readinto(message_data)

        if read_bytes < len(message_data):
            self.usb.readall()
            return

        topic_id = int(message_data[0]) + int(message_data[1])*256

        if message_data[dataLength-1] != self.checksum(message_data):
            self.usb.readall()
            return

        if topic_id == 0:
          return self.send_topics()

        topic_id = int(message_data[0]) + int(message_data[1])*256

        for sub in self._subscribers:
            if sub.topic_id == topic_id:
                result = sub.datatype()
                result.deserialize(message_data[2:-1])
                break;

  def advertise(self, _publisher):
    self._publishers.append(_publisher)
    pass # Send advertisement through USB

  def subscribe(self, _subscriber):
    self._subscribers.append(_subscriber)
    pass # Send subscibe through USB

  def checksum(self, buff):
    _result = 255 - (sum(buff[:-1])%256)
    return _result

  def send_topics(self):
    pass

class Publisher(object):
  topic_id = None

  def __init__(self, topic_name, datatype)
    self.datatype = datatype
    self.topic_name = topic_name
    pass

  def publish(self):
    

class Subscriber(object):
  topic_id = None

  def __init__(self, topic_name, datatype, callback)
    self.datatype = datatype
    self.topic_name = topic_name
    self.callback = callback


class Struct:

    def __init__(self, format):
        self.format = format
        self.size = calcsize(format)

    def unpack(self, buf):
        return unpack(self.format, buf)

    def pack(self, *vals):
        return pack(self.format, *vals)