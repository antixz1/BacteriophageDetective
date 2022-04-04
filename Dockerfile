FROM tikhonovapolly/phigaro:latest
RUN /bin/bash -c "/root/miniconda3/bin/pip install phigaro --upgrade"

RUN conda -c conda-forge ncbi-datasets-cli
