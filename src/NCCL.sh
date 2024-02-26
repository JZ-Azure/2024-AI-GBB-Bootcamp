#!/bin/bash

export NCCL_DEBUG=info
export UCX_TLS=tcp
export NCCL_TOPO_FILE=/workspace/ndv4-topo.xml
export UCX_NET_DEVICES=eth0
export CUDA_DEVICE_ORDER=PCI_BUS_ID
export NCCL_SOCKET_IFNAME=eth0

/workspace/nccl-tests/build/all_reduce_perf -b 8 -f 2 -g 1 -e 8G -c 1