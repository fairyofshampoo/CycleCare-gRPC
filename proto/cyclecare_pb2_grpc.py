# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import cyclecare_pb2 as cyclecare__pb2


class CycleCareServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadVideo = channel.stream_unary(
                '/cyclecare.CycleCareService/UploadVideo',
                request_serializer=cyclecare__pb2.VideoChunk.SerializeToString,
                response_deserializer=cyclecare__pb2.UploadStatus.FromString,
                )
        self.StreamVideo = channel.unary_stream(
                '/cyclecare.CycleCareService/StreamVideo',
                request_serializer=cyclecare__pb2.VideoRequest.SerializeToString,
                response_deserializer=cyclecare__pb2.VideoChunk.FromString,
                )


class CycleCareServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UploadVideo(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamVideo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CycleCareServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadVideo': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadVideo,
                    request_deserializer=cyclecare__pb2.VideoChunk.FromString,
                    response_serializer=cyclecare__pb2.UploadStatus.SerializeToString,
            ),
            'StreamVideo': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamVideo,
                    request_deserializer=cyclecare__pb2.VideoRequest.FromString,
                    response_serializer=cyclecare__pb2.VideoChunk.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cyclecare.CycleCareService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CycleCareService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UploadVideo(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/cyclecare.CycleCareService/UploadVideo',
            cyclecare__pb2.VideoChunk.SerializeToString,
            cyclecare__pb2.UploadStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamVideo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/cyclecare.CycleCareService/StreamVideo',
            cyclecare__pb2.VideoRequest.SerializeToString,
            cyclecare__pb2.VideoChunk.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)