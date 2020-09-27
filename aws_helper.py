from __future__ import print_function
import boto3
import os
import sys
sys.path.append(os.path.abspath(""))


class AwsHelper:
    def __init__(self, **kwargs):
        self.cluster_name = "asharq-ecs01"
        self.client = boto3.client("ecs")
        self.ec2_client = boto3.client("ec2")
        self.service_name = "identv-dev-service-"
        self.task_name = "grpc-recommendation-api"
        self.launch_type = "EC2"

    def get_service(self, max_items=50, page_size=2):
        """
        Add Documentation here
        Args:
            max_items [int] : default : 50
            page_size [int] : default : 2

        Returns:

        """
        services = self.client.list_services(cluster=self.cluster_name, launchType=self.launch_type)
        next_token = services["nextToken"]
        service_list = [data for data in services["serviceArns"] if self.task_name in data]
        if service_list:
            print("Service finder Digging more dipper.")
        else:
            paginator = self.client.get_paginator("list_services")
            response_iterator = paginator.paginate(
                cluster=self.cluster_name,
                PaginationConfig={"MaxItems": max_items, "PageSize": page_size, "StartingToken": next_token},
            )
            service_list = [service for service_list in response_iterator for service in service_list["serviceArns"] if self.task_name in service]
        return service_list

    def get_task(self, max_items=100, page_size=10):
        """
        Add Documentation here
        Args:
            max_items [int] : default : 100
            page_size [int] : default : 10

        Returns:

        """
        output = {"taskArns": []}
        paginator = self.client.get_paginator("list_tasks")
        task_iterator = paginator.paginate(
            cluster=self.cluster_name,
            serviceName=self.service_name + self.task_name,
            PaginationConfig={
                "MaxItems": max_items,
                "PageSize": page_size
            },
        )
        for data in task_iterator:
            if data:
                output = data
        return output

    def get_detail_task(self, task_json):
        """
        Add Documentation Here
        Args:
            task_json:

        Returns:

        """
        result = []
        dectasks = self.client.describe_tasks(cluster=self.cluster_name, tasks=task_json["taskArns"])
        if dectasks["tasks"]:
            arnIds = [task["containerInstanceArn"].split("/")[1] for task in dectasks["tasks"]]
            port = [container["networkBindings"][0]["hostPort"] for task in dectasks["tasks"] for container in task["containers"] if container["name"] == self.task_name]
            containerinstance = self.client.describe_container_instances(
                cluster=self.cluster_name,
                containerInstances=arnIds)

            # -----------------------------------------------------------------------------
            if containerinstance['containerInstances']:
                instanceIds = [data["ec2InstanceId"] for data in containerinstance['containerInstances']]
                instance_detail = self.ec2_client.describe_instances(
                    InstanceIds=instanceIds)

                # -----------------------------------------------------------------------------
                if instance_detail:
                    ip_list = [data["Instances"][0]["PrivateIpAddress"] for data in instance_detail['Reservations']]
                    result = [f"{ip}:{port[key]}" for key, ip in enumerate(ip_list)]
        return result

    def fetch_ip_port(self):
        output = []
        service_list = self.get_service()
        task_json = self.get_task()
        if service_list:
            output = self.get_detail_task(task_json=task_json)
        return output


if __name__ == "__main__":
    update = AwsHelper()
    print(update.fetch_ip_port())
