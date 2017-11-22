# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import communication_pb2 as communication__pb2


class CommunicationStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.message = channel.unary_stream(
        '/Communication/message',
        request_serializer=communication__pb2.Request.SerializeToString,
        response_deserializer=communication__pb2.Response.FromString,
        )
    self.put = channel.unary_unary(
        '/Communication/put',
        request_serializer=communication__pb2.PutValues.SerializeToString,
        response_deserializer=communication__pb2.Empty.FromString,
        )
    self.delete = channel.unary_unary(
        '/Communication/delete',
        request_serializer=communication__pb2.DeleteValues.SerializeToString,
        response_deserializer=communication__pb2.Empty.FromString,
        )


class CommunicationServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def message(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def put(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CommunicationServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'message': grpc.unary_stream_rpc_method_handler(
          servicer.message,
          request_deserializer=communication__pb2.Request.FromString,
          response_serializer=communication__pb2.Response.SerializeToString,
      ),
      'put': grpc.unary_unary_rpc_method_handler(
          servicer.put,
          request_deserializer=communication__pb2.PutValues.FromString,
          response_serializer=communication__pb2.Empty.SerializeToString,
      ),
      'delete': grpc.unary_unary_rpc_method_handler(
          servicer.delete,
          request_deserializer=communication__pb2.DeleteValues.FromString,
          response_serializer=communication__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Communication', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
