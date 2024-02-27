import os
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Environment

# Retrieve details from environment variables
subscription_id = os.getenv('SUBSCRIPTION_ID')
resource_group = os.getenv('RESOURCE_GROUP')
work_space = os.getenv('WORKSPACE_NAME')
cluster_name = os.getenv('CLUSTER_NAME')

# get a handle to the workspace
ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, work_space)

# Define Docker image for the custom environment
env_name = "Fairseq-Env"
custom_env = Environment(
    name=env_name,
    image='jzacr3.azurecr.io/aml_fairseq_2110:latest',
    version="1.0",
)

# Register the Environment
registered_env = ml_client.environments.create_or_update(custom_env)

# Print useful information about the environment
print(f"Environment '{env_name}' has been created/updated.")
print(f"Environment information: {registered_env}")
