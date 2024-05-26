import grpc
from concurrent import futures
import os
import cyclecare_pb2
import cyclecare_pb2_grpc

CHUNK_SIZE = 1024 * 1024  # 1MB
MEDIA_DIR = "media"

class CycleCareServiceServicer(cyclecare_pb2_grpc.CycleCareServiceServicer):
    def UploadVideo(self, request_iterator, context):
        filename = ""
        with open(os.path.join(MEDIA_DIR, "temp_video"), "wb") as f:
            for chunk in request_iterator:
                if not filename:
                    filename = chunk.filename
                f.write(chunk.data)
        os.rename(os.path.join(MEDIA_DIR, "temp_video"), os.path.join(MEDIA_DIR, filename))
        return cyclecare_pb2.UploadStatus(message="Upload successful", code=0)

    def StreamVideo(self, request, context):
        filename = request.filename
        file_path = os.path.join(MEDIA_DIR, filename)
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(CHUNK_SIZE)
                if not chunk:
                    break
                yield cyclecare_pb2.VideoChunk(data=chunk, filename=filename)

def serve():
    if not os.path.exists(MEDIA_DIR):
        os.makedirs(MEDIA_DIR)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cyclecare_pb2_grpc.add_CycleCareServiceServicer_to_server(CycleCareServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
