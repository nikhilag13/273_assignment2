'''
################################## client.py #############################
#
################################## client.py #############################
'''
import grpc
import communication_pb2
import argparse

PORT = 3000


class DataClient():
    def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = communication_pb2.CommunicationStub(self.channel)

    def put(self, key, value):
        return self.stub.put(communication_pb2.PutValues(key=key, data=value))

    def delete(self, key):
        return self.stub.delete(communication_pb2.DeleteValues(key=key))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="display a square of a given number")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    client = DataClient(host=args.host)


    client.put("key1","abc")

    client.put("key2","def")

    client.put("key3", "ghi")

    client.delete("key1")



if __name__ == "__main__":
    main()

