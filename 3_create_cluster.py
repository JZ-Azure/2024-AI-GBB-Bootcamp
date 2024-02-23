import os
import argparse
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import (IdentityConfiguration, AmlCompute, AmlComputeSshSettings, ComputeInstance)
from azure.ai.ml.constants import ManagedServiceIdentityType

# Set up argument parser
parser = argparse.ArgumentParser(description="Create Azure ML compute resources.")
parser.add_argument("--compute", action="store_true", help="Create a compute instance instead of a compute cluster.")
parser.add_argument("--cluster", action="store_true", default=True, help="Create a compute cluster (default action).")
args = parser.parse_args()

# Retrieve details from environment variables
subscription_id = os.getenv('SUBSCRIPTION_ID')
resource_group = os.getenv('RESOURCE_GROUP')
work_space = os.getenv('WORKSPACE_NAME')
cluster_name = os.getenv('CLUSTER_NAME')

# get a handle to the workspace
ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, work_space)

# Create an identity configuration for a system-assigned managed identity
identity_config = IdentityConfiguration(type=ManagedServiceIdentityType.SYSTEM_ASSIGNED)

# Common SSH settings for both compute cluster and compute instance
cluster_ssh = AmlComputeSshSettings(
    admin_username="azureuser",
    ssh_key_value="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCq5muNaAXzQa3WJXPKlQwVwRfcTsjNQEqbIecX/XxwBRXADue8N9gRXTLlXvN6UbxxI1G5b4YHz8AJJ0Exu3efpXM7Fk7siRc/w3j83gqF9wlFDb1zUWa7tuedLUwhynGXrZKGAao64FGChu7DQr4VTJEiRM3vlNGO+kGeorQ0H6ptvhn9Pn6dr6LijRIpcjKN57IrUdLx31NygZQsNBWhjVjoOe9WsP8INujZWUxA0yUJqTlimnBw+VKiIVcc2HYVNEX8bmAYMmXAYN70/iZZUjL5lWieUTtJIRLDbl6S8K7f1FotXqRRCD7JFBgnJmxQ25WCmZLZU4Tjiyb17vFHe3e2AknzHAKah5JoRx79+7sjf1gpv9SnprbYdygwLErq1pd7T+T/l4q6pbQx0C3xS00O47+dTc7YqKXyL7piiihXmFo9W0BYehjSCNEb2lSJxQoyfHjt9AiNGWhhJgmTQ4xrsvK5Ga7MV87W4ZYbfeR/NAeRMXoViKGW5FVPx88= jingchao@ms_laptop",
    admin_password="password123",)

if args.compute:
    # Code to create a compute instance
    compute_instance = ComputeInstance(
        name=cluster_name,
        type="ComputeInstance",
        size="Standard_ND96asr_v4",  # Example size, adjust as needed
        ssh_public_access_enabled=True,
        ssh_settings=cluster_ssh,
        identity=identity_config)
    
    operation = ml_client.begin_create_or_update(compute_instance)
    result = operation.result()
    print(f"Compute instance '{cluster_name}' has been created/updated.")
    print(f"Compute instance information: {result}")

elif args.cluster:
    # Existing code to create a compute cluster
    cluster_basic = AmlCompute(
        name=cluster_name,
        type="amlcompute",
        size="Standard_ND96asr_v4",
        ssh_public_access_enabled=True,
        ssh_settings=cluster_ssh,
        min_instances=1,
        max_instances=2,
        idle_time_before_scale_down=120,
        identity=identity_config)

    operation = ml_client.begin_create_or_update(cluster_basic)
    result = operation.result()
    print(f"Cluster '{cluster_name}' has been created/updated.")
    print(f"Cluster information: {result}")
