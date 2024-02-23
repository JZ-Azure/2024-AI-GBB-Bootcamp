FROM nvcr.io/nvidia/pytorch:23.03-py3

RUN apt update && apt-get install -y \
    build-essential \
    infiniband-diags \
    openssh-server \
    kmod \
    bc \
    && rm -rf /var/lib/apt/lists/*

COPY nccl-tests.sh .
RUN ./nccl-tests.sh

COPY ndv4-topo.xml .
