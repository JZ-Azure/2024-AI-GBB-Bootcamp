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

## Launch training job
```bash
python run_fairseq.py
```

## Expected output
```bash
5047e1766a8046d08a2c92ea9faaa871000005:352:352 [0] NCCL INFO Launch mode Parallel
2024-02-29 07:58:54 | INFO | fairseq.trainer | NOTE: gradient overflow detected, ignoring gradient, setting loss scale to: 64.0
2024-02-29 07:59:01 | INFO | fairseq.trainer | NOTE: gradient overflow detected, ignoring gradient, setting loss scale to: 32.0
2024-02-29 07:59:08 | INFO | fairseq.trainer | NOTE: gradient overflow detected, ignoring gradient, setting loss scale to: 16.0
2024-02-29 08:00:28 | INFO | train_inner | {"epoch": 1, "update": 0.012, "loss": "21.229", "moe_gate_loss": "21.6108", "overflow_expert1": "18.819", "overflow_expert2": "58.792", "entropy_gating": "1.964", "expert1_balance_top": "65.29", "expert1_balance_bottom": "2.343", "unused_expert1_count": "0.582", "expert2_balance_top": "50.313", "expert2_balance_bottom": "4.213", "unused_expert2_count": "0.335", "all_to_all_cpu_time_ms": "0", "all_to_all_cuda_time_ms": "0", "inner_loss": "20.917", "ppl": "1.98043e+06", "wps": "11941.9", "ups": "0.12", "wpb": "98304", "bsz": "96", "num_updates": "10", "lr": "7.33333e-06", "gnorm": "27.354", "loss_scale": "16", "train_wall": "257", "cuda_gb_allocated": "26.3", "cuda_gb_reserved": "34.1", "cuda_gb_free": "13.1", "wall": "259"}
2024-02-29 08:01:49 | INFO | train_inner | {"epoch": 1, "update": 0.022, "loss": "15.052", "moe_gate_loss": "18.1337", "overflow_expert1": "8.9", "overflow_expert2": "49.925", "entropy_gating": "2.028", "expert1_balance_top": "53.955", "expert1_balance_bottom": "4.012", "unused_expert1_count": "0.644", "expert2_balance_top": "42.734", "expert2_balance_bottom": "5.921", "unused_expert2_count": "0.484", "all_to_all_cpu_time_ms": "0", "all_to_all_cuda_time_ms": "0", "inner_loss": "14.79", "ppl": "28330.9", "wps": "12181.5", "ups": "0.12", "wpb": "98304", "bsz": "96", "num_updates": "20", "lr": "1.4e-05", "gnorm": "2.701", "loss_scale": "16", "train_wall": "81", "cuda_gb_allocated": "26.3", "cuda_gb_reserved": "34.2", "cuda_gb_free": "13.1", "wall": "340"}
2024-02-29 08:02:30 | INFO | fairseq_cli.train | Stopping training due to num_updates: 25 >= max_update: 25
2024-02-29 08:02:30 | INFO | fairseq.checkpoint_utils | Preparing to save checkpoint for epoch 1 @ 25 updates
2024-02-29 08:02:37 | INFO | fairseq.trainer | Saving checkpoint to ./checkpoint_last-rank-0-shard0.pt
```

## Referece
- [Running Fairseq with AML](https://github.com/JZ-Azure/fairseq_with_AML_public)
- [AML Fairseq](https://github.com/Azure/azurehpc/tree/master/experimental/fairseq_moe_docker_slurm)
