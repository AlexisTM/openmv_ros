from microros import Struct
import struct

class TopicInfo(object):
  _md5sum = "0ad51f88fc44892f8c10684077646005"
  _type = "rosserial_msgs/TopicInfo"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# special topic_ids
uint16 ID_PUBLISHER=0
uint16 ID_SUBSCRIBER=1
uint16 ID_SERVICE_SERVER=2
uint16 ID_SERVICE_CLIENT=4
uint16 ID_PARAMETER_REQUEST=6
uint16 ID_LOG=7
uint16 ID_TIME=10
uint16 ID_TX_STOP=11

# The endpoint ID for this topic
uint16 topic_id

string topic_name
string message_type

# MD5 checksum for this message type
string md5sum

# size of the buffer message must fit in
int32 buffer_size
"""
  # Pseudo-constants
  ID_PUBLISHER = 0
  ID_SUBSCRIBER = 1
  ID_SERVICE_SERVER = 2
  ID_SERVICE_CLIENT = 4
  ID_PARAMETER_REQUEST = 6
  ID_LOG = 7
  ID_TIME = 10
  ID_TX_STOP = 11

  __slots__ = ['topic_id','topic_name','message_type','md5sum','buffer_size']
  _slot_types = ['uint16','string','string','string','int32']

  def __init__(self, *args, **kwds):
    self.topic_id = 0
    self.topic_name = ''
    self.message_type = ''
    self.md5sum = ''
    self.buffer_size = 0

  def serialize(self):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    buff = bytes(0)
    buff += _struct_H.pack(self.topic_id)
    _x = self.topic_name
    _x = _x.encode('utf-8')
    length = len(_x)
    buff += struct.pack('<I%sB'%length, length, *_x)
    _x = self.message_type
    _x = _x.encode('utf-8')
    length = len(_x)
    buff += struct.pack('<I%sB'%length, length, *_x)
    _x = self.md5sum
    _x = _x.encode('utf-8')
    length = len(_x)
    buff += struct.pack('<I%sB'%length, length, *_x)
    buff += _struct_i.pack(self.buffer_size)
    return buff

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 2
      (self.topic_id,) = _struct_H.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.topic_name = str[start:end].decode('utf-8')
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.message_type = str[start:end].decode('utf-8')
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.md5sum = str[start:end].decode('utf-8')
      start = end
      end += 4
      (self.buffer_size,) = _struct_i.unpack(str[start:end])
      return self
    except:
      pass

  def __str__(self):
    return "Topic ID {0}, topic_name {1}, message_type {2}, md5sum {3}, buffer_size {4}".format(self.topic_id, self.topic_name, self.message_type, self.md5sum, self.buffer_size)

_struct_I = Struct('<I')
_struct_i = Struct("<i")
_struct_H = Struct("<H")
