# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='config_message.proto',
  package='config_message.msgs',
  serialized_pb='\n\x14\x63onfig_message.proto\x12\x13\x63onfig_message.msgs\"\xe5\x01\n\rConfigMessage\x12\x11\n\tModelName\x18\x01 \x02(\t\x12\x19\n\rModelPosition\x18\x02 \x03(\x01\x42\x02\x10\x01\x12\x17\n\x0bJointAngles\x18\x03 \x03(\x01\x42\x02\x10\x01\x12\x16\n\x0e\x43onnectedModel\x18\x04 \x01(\t\x12\x13\n\x0b\x43onnectedOn\x18\x05 \x01(\x05\x12\x13\n\x0b\x43onnectedTo\x18\x06 \x01(\x05\x12\x0f\n\x07\x45\x64geDis\x18\x07 \x01(\x01\x12\x0f\n\x07\x45\x64geAng\x18\x08 \x01(\x01\x12\x12\n\nDeleteFlag\x18\t \x01(\x08\x12\x15\n\rQuaternionPos\x18\n \x01(\x08')




_CONFIGMESSAGE = descriptor.Descriptor(
  name='ConfigMessage',
  full_name='config_message.msgs.ConfigMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ModelName', full_name='config_message.msgs.ConfigMessage.ModelName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ModelPosition', full_name='config_message.msgs.ConfigMessage.ModelPosition', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='JointAngles', full_name='config_message.msgs.ConfigMessage.JointAngles', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='ConnectedModel', full_name='config_message.msgs.ConfigMessage.ConnectedModel', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ConnectedOn', full_name='config_message.msgs.ConfigMessage.ConnectedOn', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ConnectedTo', full_name='config_message.msgs.ConfigMessage.ConnectedTo', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='EdgeDis', full_name='config_message.msgs.ConfigMessage.EdgeDis', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='EdgeAng', full_name='config_message.msgs.ConfigMessage.EdgeAng', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='DeleteFlag', full_name='config_message.msgs.ConfigMessage.DeleteFlag', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='QuaternionPos', full_name='config_message.msgs.ConfigMessage.QuaternionPos', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=46,
  serialized_end=275,
)

DESCRIPTOR.message_types_by_name['ConfigMessage'] = _CONFIGMESSAGE

class ConfigMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONFIGMESSAGE
  
  # @@protoc_insertion_point(class_scope:config_message.msgs.ConfigMessage)

# @@protoc_insertion_point(module_scope)
