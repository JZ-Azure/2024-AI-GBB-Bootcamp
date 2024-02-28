#!/bin/bash

export RG="JZ-AML$(date +%m%d)"
export location=francecentral
export ws_name="JZ-WS$(date +%m%d)"
export acr_id=`az acr show --name jzacr3 --resource-group JZ-ACR --query id --output tsv`

az group create --name $RG --location $location
az ml workspace create --name $ws_name --resource-group $RG --location $location --container-registry $acr_id

