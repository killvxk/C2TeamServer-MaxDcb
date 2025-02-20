# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import TeamServerApi_pb2 as TeamServerApi__pb2


class TeamServerApiStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetListeners = channel.unary_stream(
                '/teamserverapi.TeamServerApi/GetListeners',
                request_serializer=TeamServerApi__pb2.Empty.SerializeToString,
                response_deserializer=TeamServerApi__pb2.Listener.FromString,
                _registered_method=True)
        self.AddListener = channel.unary_unary(
                '/teamserverapi.TeamServerApi/AddListener',
                request_serializer=TeamServerApi__pb2.Listener.SerializeToString,
                response_deserializer=TeamServerApi__pb2.Response.FromString,
                _registered_method=True)
        self.StopListener = channel.unary_unary(
                '/teamserverapi.TeamServerApi/StopListener',
                request_serializer=TeamServerApi__pb2.Listener.SerializeToString,
                response_deserializer=TeamServerApi__pb2.Response.FromString,
                _registered_method=True)
        self.GetSessions = channel.unary_stream(
                '/teamserverapi.TeamServerApi/GetSessions',
                request_serializer=TeamServerApi__pb2.Empty.SerializeToString,
                response_deserializer=TeamServerApi__pb2.Session.FromString,
                _registered_method=True)
        self.StopSession = channel.unary_unary(
                '/teamserverapi.TeamServerApi/StopSession',
                request_serializer=TeamServerApi__pb2.Session.SerializeToString,
                response_deserializer=TeamServerApi__pb2.Response.FromString,
                _registered_method=True)
        self.GetHelp = channel.unary_unary(
                '/teamserverapi.TeamServerApi/GetHelp',
                request_serializer=TeamServerApi__pb2.Command.SerializeToString,
                response_deserializer=TeamServerApi__pb2.CommandResponse.FromString,
                _registered_method=True)
        self.SendCmdToSession = channel.unary_unary(
                '/teamserverapi.TeamServerApi/SendCmdToSession',
                request_serializer=TeamServerApi__pb2.Command.SerializeToString,
                response_deserializer=TeamServerApi__pb2.Response.FromString,
                _registered_method=True)
        self.GetResponseFromSession = channel.unary_stream(
                '/teamserverapi.TeamServerApi/GetResponseFromSession',
                request_serializer=TeamServerApi__pb2.Session.SerializeToString,
                response_deserializer=TeamServerApi__pb2.CommandResponse.FromString,
                _registered_method=True)
        self.SendTermCmd = channel.unary_unary(
                '/teamserverapi.TeamServerApi/SendTermCmd',
                request_serializer=TeamServerApi__pb2.TermCommand.SerializeToString,
                response_deserializer=TeamServerApi__pb2.TermCommand.FromString,
                _registered_method=True)


class TeamServerApiServicer(object):
    """Interface exported by the server.
    """

    def GetListeners(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddListener(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopListener(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSessions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHelp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendCmdToSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetResponseFromSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendTermCmd(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TeamServerApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetListeners': grpc.unary_stream_rpc_method_handler(
                    servicer.GetListeners,
                    request_deserializer=TeamServerApi__pb2.Empty.FromString,
                    response_serializer=TeamServerApi__pb2.Listener.SerializeToString,
            ),
            'AddListener': grpc.unary_unary_rpc_method_handler(
                    servicer.AddListener,
                    request_deserializer=TeamServerApi__pb2.Listener.FromString,
                    response_serializer=TeamServerApi__pb2.Response.SerializeToString,
            ),
            'StopListener': grpc.unary_unary_rpc_method_handler(
                    servicer.StopListener,
                    request_deserializer=TeamServerApi__pb2.Listener.FromString,
                    response_serializer=TeamServerApi__pb2.Response.SerializeToString,
            ),
            'GetSessions': grpc.unary_stream_rpc_method_handler(
                    servicer.GetSessions,
                    request_deserializer=TeamServerApi__pb2.Empty.FromString,
                    response_serializer=TeamServerApi__pb2.Session.SerializeToString,
            ),
            'StopSession': grpc.unary_unary_rpc_method_handler(
                    servicer.StopSession,
                    request_deserializer=TeamServerApi__pb2.Session.FromString,
                    response_serializer=TeamServerApi__pb2.Response.SerializeToString,
            ),
            'GetHelp': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHelp,
                    request_deserializer=TeamServerApi__pb2.Command.FromString,
                    response_serializer=TeamServerApi__pb2.CommandResponse.SerializeToString,
            ),
            'SendCmdToSession': grpc.unary_unary_rpc_method_handler(
                    servicer.SendCmdToSession,
                    request_deserializer=TeamServerApi__pb2.Command.FromString,
                    response_serializer=TeamServerApi__pb2.Response.SerializeToString,
            ),
            'GetResponseFromSession': grpc.unary_stream_rpc_method_handler(
                    servicer.GetResponseFromSession,
                    request_deserializer=TeamServerApi__pb2.Session.FromString,
                    response_serializer=TeamServerApi__pb2.CommandResponse.SerializeToString,
            ),
            'SendTermCmd': grpc.unary_unary_rpc_method_handler(
                    servicer.SendTermCmd,
                    request_deserializer=TeamServerApi__pb2.TermCommand.FromString,
                    response_serializer=TeamServerApi__pb2.TermCommand.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'teamserverapi.TeamServerApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('teamserverapi.TeamServerApi', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TeamServerApi(object):
    """Interface exported by the server.
    """

    @staticmethod
    def GetListeners(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/teamserverapi.TeamServerApi/GetListeners',
            TeamServerApi__pb2.Empty.SerializeToString,
            TeamServerApi__pb2.Listener.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddListener(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/teamserverapi.TeamServerApi/AddListener',
            TeamServerApi__pb2.Listener.SerializeToString,
            TeamServerApi__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StopListener(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/teamserverapi.TeamServerApi/StopListener',
            TeamServerApi__pb2.Listener.SerializeToString,
            TeamServerApi__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetSessions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/teamserverapi.TeamServerApi/GetSessions',
            TeamServerApi__pb2.Empty.SerializeToString,
            TeamServerApi__pb2.Session.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StopSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/teamserverapi.TeamServerApi/StopSession',
            TeamServerApi__pb2.Session.SerializeToString,
            TeamServerApi__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetHelp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/teamserverapi.TeamServerApi/GetHelp',
            TeamServerApi__pb2.Command.SerializeToString,
            TeamServerApi__pb2.CommandResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SendCmdToSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/teamserverapi.TeamServerApi/SendCmdToSession',
            TeamServerApi__pb2.Command.SerializeToString,
            TeamServerApi__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetResponseFromSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/teamserverapi.TeamServerApi/GetResponseFromSession',
            TeamServerApi__pb2.Session.SerializeToString,
            TeamServerApi__pb2.CommandResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SendTermCmd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/teamserverapi.TeamServerApi/SendTermCmd',
            TeamServerApi__pb2.TermCommand.SerializeToString,
            TeamServerApi__pb2.TermCommand.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
