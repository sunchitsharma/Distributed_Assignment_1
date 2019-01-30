from concurrent import futures
import time
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        a=request.name
        req_arr=a.split("##")
        menu_iter=req_arr[0]
        menu_value=req_arr[1]
        answer=''
        if(menu_iter=='1'):
            answer = str(menu_value)+" cm is "+str(int(menu_value)*0.3937008)+" inches"
        elif(menu_iter=='2'):
            answer = str(menu_value)+" lb is "+str(int(menu_value)*453.59237)+" gms"
        elif(menu_iter=='3'):
            answer = str(menu_value)+" Celsius is "+str(int(menu_value)*1.8000 + 32)+" farenheit"
        elif(menu_iter=='4'):
            answer = str(menu_value)+" Celsius is "+str(int(menu_value)+273.15)+" kelvin"
        else:
            answer = "Enter something valid"

        return helloworld_pb2.HelloReply(message=answer)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50054')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
