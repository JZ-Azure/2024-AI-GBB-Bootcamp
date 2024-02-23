#!/bin/bash

export RG="JZ-AML$(date +%m%d)"
#export RG="JZ-AML0111"
export location=southcentralus
export ws_name="JZ-WS$(date +%m%d)"
export acr_id="/subscriptions/75d1e0d5-9fed-4ae1-aec7-2ecc19de26fa/resourceGroups/JZ-ACR/providers/Microsoft.ContainerRegistry/registries/jzacr3"

az group create --name $RG --location $location
az ml workspace create --name $ws_name --resource-group $RG --location $location --container-registry $acr_id

