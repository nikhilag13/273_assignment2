'''
################################## server.py #############################
#
################################## server.py #############################
'''
import time
import grpc
import communication_pb2
import communication_pb2_grpc
import rocksdb
import queue

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24



class MyCommunicationServicer(communication_pb2.CommunicationServicer):


    def __init__(self):
        # TODO
        self.db = rocksdb.DB("master.db", rocksdb.Options(create_if_missing=True))
        self.replicator_queue = queue.Queue()
        print("init")


    def message(self, request, context):
        print(" message method in server...")

        it = self.db.iterkeys()
        it.seek_to_first()
        l = list(it)
        print(list(it))

        for key in l:
            data = self.db.get(key)
            res = communication_pb2.Response(operation="put", key=key.decode('utf-8'), data=data.decode('utf-8'))
            print("put %s %s" % (key.decode('utf-8'), data.decode('utf-8')))
            yield res

        while(1):
            res = self.replicator_queue.get()
            if(res.operation =="put"):
               print("operation %s %s %s" % (res.operation, res.key, res.data))
            else:
                print("operation %s %s" % (res.operation, res.key))

            yield res

    def put_decorator(f):
        def wrapper(self, request, context):
            msg = communication_pb2.Response(
                operation="put",
                key= request.key,
                data=request.data
            )
            self.replicator_queue.put(msg)
            return f(self, request, context)

        return wrapper

    def delete_decorator(f):
        def wrapper(self, request, context):
            msg = communication_pb2.Response(
                operation="delete",
                key=request.key,
                data="none"
            )
            self.replicator_queue.put(msg)
            return f(self, request, context)

        return wrapper


    @put_decorator
    def put(self, request, context):
        #print(" Put Message in server ... ")
        # TODO
        key = request.key
        data = request.data
        self.db.put(key.encode('utf-8'), data.encode('utf-8'))
        return communication_pb2.Empty()

    @delete_decorator
    def delete(self, request, context):
        #print(" Delete Message in server ... ")
        # TODO
        key = request.key
        self.db.delete(key.encode('utf-8'))
        return communication_pb2.Empty()


def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    communication_pb2_grpc.add_CommunicationServicer_to_server(MyCommunicationServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()

    try:
        while True:
            print("Server started at...%d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    print("... here ...")
    run('0.0.0.0', 3000)

