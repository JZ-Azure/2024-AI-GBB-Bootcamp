import os
from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient,command,MpiDistribution

from azure.ai.ml.entities import (
    SshJobService,
    VsCodeJobService,
    JupyterLabJobService,
)

# Retrieve details from environment variables
subscription_id = os.getenv('SUBSCRIPTION_ID')
resource_group = os.getenv('RESOURCE_GROUP')
work_space = os.getenv('WORKSPACE_NAME')
cluster_name = os.getenv('CLUSTER_NAME')

# get a handle to the workspace
ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, work_space)

job = command(
    code="./src",  # local path where the code is stored
    command="bash launch_fairseq.py",
    compute=cluster_name,
    environment="Fairseq-Env:1.0",
    instance_count=1,
    distribution=MpiDistribution(
        process_count_per_instance=1,
    ),
    #distribution={
    #    "type": "PyTorch",
    #    "process_count_per_instance": 1,
    #},
    services={
        "My_jupyterlab": JupyterLabJobService(),
        "My_vscode": VsCodeJobService(),
        "My_ssh": SshJobService(
            nodes="all",  # For distributed jobs, use the `nodes` property to pick which node you want to enable interactive services on. If `nodes` are not selected, by default, interactive applications are only enabled on the head node. Values are "all", or compute node index (for ex. "0", "1" etc.)
            ssh_public_keys="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCq5muNaAXzQa3WJXPKlQwVwRfcTsjNQEqbIecX/XxwBRXADue8N9gRXTLlXvN6UbxxI1G5b4YHz8AJJ0Exu3efpXM7Fk7siRc/w3j83gqF9wlFDb1zUWa7tuedLUwhynGXrZKGAao64FGChu7DQr4VTJEiRM3vlNGO+kGeorQ0H6ptvhn9Pn6dr6LijRIpcjKN57IrUdLx31NygZQsNBWhjVjoOe9WsP8INujZWUxA0yUJqTlimnBw+VKiIVcc2HYVNEX8bmAYMmXAYN70/iZZUjL5lWieUTtJIRLDbl6S8K7f1FotXqRRCD7JFBgnJmxQ25WCmZLZU4Tjiyb17vFHe3e2AknzHAKah5JoRx79+7sjf1gpv9SnprbYdygwLErq1pd7T+T/l4q6pbQx0C3xS00O47+dTc7YqKXyL7piiihXmFo9W0BYehjSCNEb2lSJxQoyfHjt9AiNGWhhJgmTQ4xrsvK5Ga7MV87W4ZYbfeR/NAeRMXoViKGW5FVPx88= jingchao@ms_laptop",
        ),
    }
)

returned_job = ml_client.jobs.create_or_update(job)
ml_client.jobs.stream(returned_job.name)
