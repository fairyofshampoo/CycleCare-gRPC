import grpc
import cyclecare_pb2
import cyclecare_pb2_grpc

def stream_video(stub, filename):
    request = cyclecare_pb2.StreamVideoRequest(filename=filename)
    for response in stub.streamVideo(request):
        print(f"Received {len(response.data)} bytes")
        # Reproducir video

def run():
    SERVER_PORT = 3000
    SERVER_ADDRESS = 'localhost:' + SERVER_PORT

    # Crea el canal de comunicación con el servidor
    channel = grpc.insecure_channel(SERVER_ADDRESS)
    # Crea el stub para acceder a los métodos del servicio CycleCare
    stub = cyclecare_pb2_grpc.CycleCareServiceStub(channel)
    filename = ""

    try:
        # Solicita al servidor que transmita el video y procesa los chunks recibidos
        filename = "video.mp4"  # Nombre de tu archivo de video
        stream_video(stub, filename)

    except KeyboardInterrupt:
        pass
    finally:
        # Cierra el canal de comunicación al finalizar
        channel.close()

if __name__ == "__main__":
    run()