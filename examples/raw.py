import grpc
import olcarpc.generated as gen

channel = grpc.insecure_channel('localhost:%i' % 8080, options=[
    ('grpc.max_send_message_length', 1024 * 1024 * 1024),
    ('grpc.max_receive_message_length', 1024 * 1024 * 1024),
])

service = gen.DataFetchServiceStub(channel)
