import rocksdb;
import time;
import grpc
import communication_pb2
import argparse

PORT = 3000


class Client(object):
    def __init__(self, host='0.0.0.0', port=PORT):
        print("init")
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = communication_pb2.CommunicationStub(self.channel)
        self.db = rocksdb.DB("client.db", rocksdb.Options(create_if_missing=True))
        self.sync()

    def sync(self):
        print("sync")
        req = communication_pb2.Request(data="start")
        messages = self.stub.message(req)

        for message in messages:
            if message.operation == "put":
                print("Messages : " + message.operation + " " + message.key + " " + message.data)
                self.db.put(message.key.encode('utf-8'), message.data.encode('utf-8'))
            elif message.operation == "delete":
                print("Messages : " + message.operation + " " + message.key)
                self.db.put(message.key.encode('utf-8'), message.data.encode('utf-8'))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="display a square of a given number")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    client = Client(host=args.host)


if __name__ == "__main__":
    main()
