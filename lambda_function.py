import grpc
import proto.recommendation_pb2 as recommendation_pb2
import proto.recommendation_pb2_grpc as recommendation_pb2_grpc
from aws_helper import AwsHelper


class GrpcProcess:
    def __init__(self):
        self.db = "redis implementation for fetching data"
        self.aws_connector = AwsHelper()
        pass

    def process(self):
        list_ip = self.aws_connector.fetch_ip_port()
        for ip in list_ip:
            channel = grpc.insecure_channel(ip)
            stub = recommendation_pb2_grpc.RecommendationStub(channel)
            response = stub.Update(recommendation_pb2.UpdateRequest(VariableName="variable",
                                                                    VariableValue="44"))
            print(f"{ip}\t Response:\t{response}\n")


if __name__ == "__main__":
    process = GrpcProcess()
    process.process()

