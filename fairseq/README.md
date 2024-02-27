## Create fairseq container
```bash
$ sudo su -
# az login
# az account set -s AG_CI_CE_SWHPC_2_kanchanm
# az acr login --name jzacr3
Login Succeeded
```
```bash
# git clone https://github.com/JZ-Azure/2024-AI-GBB-Bootcamp.git
# cd 2024-AI-GBB-Bootcamp/fairseq/Docker
# docker build -t jzacr3.azurecr.io/aml_fairseq_2110:latest .
# docker push jzacr3.azurecr.io/aml_fairseq_2110:latest
```

## Create Fairseq env in AML
```bash
python create_environment.py
```
