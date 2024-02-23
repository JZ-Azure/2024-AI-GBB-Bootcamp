# AML_NCCL_Test

## Create AML env
```bash
conda env create -f azureml_env.yml
```

## Steps to run this repo

```bash
bash 1_create_RG.sh
source 2_set_env.sh
python 3_create_cluster.py
python 4_create_environment.py
python 5_NCCL_test.py
```

## NCCL `all_reduce` Results
### Single Node
```bash
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
           8             2     float     sum      -1    18.75    0.00    0.00      0    17.60    0.00    0.00      0
          16             4     float     sum      -1    17.94    0.00    0.00      0    18.11    0.00    0.00      0
          32             8     float     sum      -1    18.08    0.00    0.00      0    18.05    0.00    0.00      0
          64            16     float     sum      -1    17.92    0.00    0.01      0    17.58    0.00    0.01      0
         128            32     float     sum      -1    17.92    0.01    0.01      0    17.73    0.01    0.01      0
         256            64     float     sum      -1    18.65    0.01    0.02      0    18.38    0.01    0.02      0
         512           128     float     sum      -1    19.54    0.03    0.05      0    19.58    0.03    0.05      0
        1024           256     float     sum      -1    20.35    0.05    0.09      0    19.93    0.05    0.09      0
        2048           512     float     sum      -1    21.65    0.09    0.17      0    21.48    0.10    0.17      0
        4096          1024     float     sum      -1    23.22    0.18    0.31      0    21.70    0.19    0.33      0
        8192          2048     float     sum      -1    24.43    0.34    0.59      0    23.29    0.35    0.62      0
       16384          4096     float     sum      -1    25.70    0.64    1.12      0    23.65    0.69    1.21      0
       32768          8192     float     sum      -1    29.24    1.12    1.96      0    27.09    1.21    2.12      0
       65536         16384     float     sum      -1    28.32    2.31    4.05      0    27.24    2.41    4.21      0
      131072         32768     float     sum      -1    29.05    4.51    7.90      0    27.62    4.75    8.31      0
      262144         65536     float     sum      -1    28.98    9.05   15.83      0    27.66    9.48   16.58      0
      524288        131072     float     sum      -1    30.23   17.35   30.36      0    28.93   18.12   31.72      0
     1048576        262144     float     sum      -1    37.33   28.09   49.15      0    37.47   27.98   48.97      0
     2097152        524288     float     sum      -1    63.11   33.23   58.16      0    62.69   33.45   58.54      0
     4194304       1048576     float     sum      -1    84.77   49.48   86.59      0    83.70   50.11   87.69      0
     8388608       2097152     float     sum      -1    131.1   63.98  111.97      0    127.6   65.74  115.05      0
    16777216       4194304     float     sum      -1    220.5   76.08  133.14      0    218.5   76.77  134.35      0
    33554432       8388608     float     sum      -1    353.9   94.82  165.94      0    351.9   95.35  166.85      0
    67108864      16777216     float     sum      -1    579.2  115.87  202.78      0    577.7  116.16  203.28      0
   134217728      33554432     float     sum      -1   1157.6  115.94  202.90      0   1157.1  115.99  202.98      0
   268435456      67108864     float     sum      -1   2169.8  123.71  216.50      0   2166.1  123.93  216.87      0
   536870912     134217728     float     sum      -1   4204.0  127.70  223.48      0   4202.7  127.74  223.55      0
  1073741824     268435456     float     sum      -1   8212.6  130.74  228.80      0   8206.4  130.84  228.97      0
  2147483648     536870912     float     sum      -1    16274  131.96  230.93      0    16274  131.96  230.93      0
  4294967296    1073741824     float     sum      -1    32200  133.38  233.42      0    32207  133.35  233.37      0
  8589934592    2147483648     float     sum      -1    64200  133.80  234.15      0    64208  133.78  234.12      0
b7381b7ff32f4b328d3889c2a1717a2e000001:1113:1113 [0] NCCL INFO comm 0x55de2ecc0590 rank 0 nranks 8 cudaDev 0 busId 100000 - Destroy COMPLETE
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 78.8923 
```
### Two Nodes
```bash
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
           8             2     float     sum      -1    37.76    0.00    0.00      0    36.09    0.00    0.00      0
          16             4     float     sum      -1    37.45    0.00    0.00      0    37.07    0.00    0.00      0
          32             8     float     sum      -1    36.38    0.00    0.00      0    35.53    0.00    0.00      0
          64            16     float     sum      -1    37.00    0.00    0.00      0    36.36    0.00    0.00      0
         128            32     float     sum      -1    36.50    0.00    0.01      0    35.26    0.00    0.01      0
         256            64     float     sum      -1    37.62    0.01    0.01      0    36.90    0.01    0.01      0
         512           128     float     sum      -1    38.44    0.01    0.02      0    37.76    0.01    0.03      0
        1024           256     float     sum      -1    40.18    0.03    0.05      0    39.85    0.03    0.05      0
        2048           512     float     sum      -1    44.38    0.05    0.09      0    42.45    0.05    0.09      0
        4096          1024     float     sum      -1    47.48    0.09    0.16      0    46.14    0.09    0.17      0
        8192          2048     float     sum      -1    64.17    0.13    0.24      0    53.94    0.15    0.28      0
       16384          4096     float     sum      -1    105.5    0.16    0.29      0    57.07    0.29    0.54      0
       32768          8192     float     sum      -1    65.22    0.50    0.94      0    56.87    0.58    1.08      0
       65536         16384     float     sum      -1    73.32    0.89    1.68      0    56.58    1.16    2.17      0
      131072         32768     float     sum      -1    66.52    1.97    3.69      0    63.45    2.07    3.87      0
      262144         65536     float     sum      -1    68.98    3.80    7.13      0    67.47    3.89    7.28      0
      524288        131072     float     sum      -1    79.28    6.61   12.40      0    79.27    6.61   12.40      0
     1048576        262144     float     sum      -1    96.57   10.86   20.36      0    96.62   10.85   20.35      0
     2097152        524288     float     sum      -1    127.5   16.45   30.85      0    127.9   16.39   30.74      0
     4194304       1048576     float     sum      -1    147.0   28.53   53.49      0    147.4   28.46   53.37      0
     8388608       2097152     float     sum      -1    210.7   39.82   74.65      0    209.2   40.10   75.18      0
    16777216       4194304     float     sum      -1    332.4   50.48   94.65      0    331.1   50.67   95.00      0
    33554432       8388608     float     sum      -1    614.9   54.57  102.32      0    621.0   54.03  101.30      0
    67108864      16777216     float     sum      -1    947.8   70.81  132.76      0    938.9   71.48  134.02      0
   134217728      33554432     float     sum      -1   1682.8   79.76  149.55      0   1689.0   79.47  149.00      0
   268435456      67108864     float     sum      -1   2975.4   90.22  169.16      0   3000.5   89.46  167.74      0
   536870912     134217728     float     sum      -1   5744.6   93.46  175.23      0   5693.8   94.29  176.80      0
  1073741824     268435456     float     sum      -1    11080   96.91  181.70      0    11095   96.78  181.46      0
  2147483648     536870912     float     sum      -1    21872   98.19  184.10      0    21765   98.66  185.00      0
  4294967296    1073741824     float     sum      -1    43176   99.48  186.52      0    43174   99.48  186.52      0
  8589934592    2147483648     float     sum      -1    85820  100.09  187.67      0    85895  100.01  187.51      0
f1d5e1df5ed649d0b9e618783ea5fdbc000000:1211:1211 [0] NCCL INFO comm 0x5634cae893b0 rank 0 nranks 16 cudaDev 0 busId 100000 - Destroy COMPLETE
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 57.1241 
```

## References
- [AML Distributed GPU Training](https://azure.github.io/azureml-cheatsheets/docs/cheatsheets/python/v1/-distributed-training/#mpi)
- [AML debug-and-monitor](https://github.com/Azure/azureml-examples/blob/-dd15e3f7d6a512fedfdfbdb4be19e065e8c1d224/sdk/python/jobs/single-step/debug-and-monitor/-debug-and-monitor.ipynb)
- [AML Compute Class](https://learn.microsoft.com/en-us/python/api/azure-ai-ml/azure.ai.ml.entities.-amlcompute?view=azure-python)
- [CIFAR10](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/single-step/pytorch/-distributed-training/distributed-cifar10.ipynb)
- [NCCL test on AKS NDmV4 VM](https://github.com/JingchaoZhang/JingchaoZhang.github.io/blob/master/-_posts/2023-09-11-NCCL%20test%20on%20AKS%20NDmV4%20VM.md)
- [from azure.ai.ml import command](https://learn.microsoft.com/en-us/python/api/azure-ai-ml/azure.ai.-ml?view=azure-python#azure-ai-ml-command)
- [Create compute with managed identity to access Docker images for training](https://learn.microsoft.-com/en-us/azure/machine-learning/how-to-identity-based-service-authentication?view=azureml-api-2&-tabs=python#create-compute-with-managed-identity-to-access-docker-images-for-training)
- [Manage environments with SDK and CLI (v2)](https://learn.microsoft.com/en-us/azure/machine-learning/-how-to-manage-environments-v2?view=azureml-api-2&tabs=cli)