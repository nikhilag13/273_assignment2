#Assignment2

I have installed rocksdb, grpcio in my Docker image and using it to Run the commads

#Commands:

To run the server.py which replicates the data in master.db:

docker run -p 3000:3000 -it -- --name lab1-server -v "$PWD":/usr/src/myapp -w /usr/src/myapp ubuntu-python3.6-rocksdb-grpc:1.0 python3.6 server.py

To Run the Client which receives teh data from master.db and stores  in client.db

docker run -it --rm --name lab1-client1 -v "$PWD":/usr/src/myapp -w /usr/src/myapp ubuntu-python3.6-rocksdb-grpc:1.0 python3.6 client.py 192.168.0.1

We need to send new data operations to Server file which replicates the data to the client.db. For this please run DataClient.py

docker run -it --rm --name lab1-client2 -v "$PWD":/usr/src/myapp -w /usr/src/myapp ubuntu-python3.6-rocksdb-grpc:1.0 python3.6 DataClient.py 192.168.0.1
