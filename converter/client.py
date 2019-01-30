from __future__ import print_function
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


def run(x,y):
    with grpc.insecure_channel('localhost:50054') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name=str(x)+"##"+str(y)))
    print("Received : " + response.message)

if __name__ == '__main__':
    logging.basicConfig()
    x=6
    while(x!='e'):
        print ("=============MENU================")
        print ("Press 1 for cm to inches")
        print ("Press 2 for lb to gms")
        print ("Press 3 for Celsius to farenheit")
        print ("Press 4 for Celsius to kelvin")
        print ("Press e to exit")
        print ("=============END=================")
        x=raw_input()
        if x!='e':
            print("Enter the value to convert")
            y=raw_input()
            run(x,y)
        else:
            break
