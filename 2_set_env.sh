#!/bin/bash

# Set environment variables for Python script
export RESOURCE_GROUP="JZ-AML$(date +%m%d)"
#export RESOURCE_GROUP="JZ-AML0111"
export WORKSPACE_NAME="JZ-WS$(date +%m%d)"
export SUBSCRIPTION_ID=$(az account show --query id -o tsv)
export CLUSTER_NAME="NDv4"
