# Is for Python3 on openMV camera

import struct

class rospy(object):
  _publishers = []
  _subscribers = []

  START_BYTE = 0xFF
  INDIGO_VERSION = 0xFE

  def __init__(self):
    self.usb = pyb.USB_VCP()
    self.usb.setinterrupt(-1)

  def spinOnce(self):   
    # Handle serial communication
    """
      ROSSerial protocol:
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

    # Publish first as it can publish while reveiving
    for pub in self._publishers:
        for msg in pub.to_publish:
            if pub.topic_id != None:
                data_buff = msg.serialize()
                header_buff = bytes([255, 254]) # sync
                header_buff += len(data_buff).to_bytes(2, "little") # Length of the message
                header_buff += bytes(1) # Placeholder for checksum
                header_buff[4] = self.checksum(header_buff)
                msg_buff = bytes(0)
                msg_buff += pub.topic_id.to_bytes(2, "little") # topic
                msg_buff += data_buff
                msg_buff += bytes(1)
                msg_buff[len(msg_buff)-1] = self.checksum(msg_buff)
                self.usb.send(header_buff + msg_buff)
        pub.to_publish=[]

    # Subscribers
    if self.usb.any():
        start_tracker = bytes(1)
        # CHECK readinto return number of bytes written?
        # Read while we have data
        while self.usb.readinto(start_tracker) > 1:
            # Sync, if in sync, read the message and call back
            if start_tracker == self.START_BYTE:
                self.usb.readinto(start_tracker)
                if start_tracker == self.INDIGO_VERSION:
                    self.readMessage()

  def readMessage(self):
    header_end = bytes(3)
    read_bytes = self.usb.readinto(header_end)

    if read_bytes != len(header_end):
        # Wrong number of bytes in header
        return

    header = bytes([self.START_BYTE, self.INDIGO_VERSION]) + header_end
    data_len = int(header[2]) + int(header[3])*256
    
    if not checksum(header):
        # Wrong checksum in header
        return

    data = bytes(data_len + 3)
    read_bytes = self.usb.readinto(data)

    if read_bytes != len(data):
        # Wrong number of bytes in data
        return

    if not checksum(data):
        # Wrong checksum in data
        return

    topic_id = int(data[0]) + int(data[1])*256

    # CHECK make lookup table with topicID => Subscriber, dataType
    msg = data[2:-1]

    for sub in self._subscribers:
        if topic_id == sub.topic_id:
            result = sub.datatype()
            result.deserialize(message_data[2:-1])
            sub.callback(result)
            return

    # Got no subscriber for this message.
    if topic_id == 0:
        self.send_topics()

  def advertise(self, _publisher):
    self._publishers.append(_publisher)
    pass # Send advertisement through USB

  def subscribe(self, _subscriber):
    self._subscribers.append(_subscriber)
    pass # Send subscibe through USB

  def checksum(self, buff):
    _result = 255 - (sum(buff[:-1])%256)
    _crc = buff[len(buff)-1]
    return _result == _crc

  def send_topics(self):
    pass

class Publisher(object):
  topic_id = None
  to_publish = []

  def __init__(self, topic_name, datatype)
    self.datatype = datatype
    self.topic_name = topic_name

  def publish(self, msg):
    self.to_publish.append(msg)

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