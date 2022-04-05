FROM tikhonovapolly/phigaro:latest
RUN /bin/bash -c "/root/miniconda3/bin/pip install phigaro --upgrade"
RUN /bin/bash -c "/root/miniconda3/bin/conda update -n base -c defaults conda"
RUN /bin/bash -c "/root/miniconda3/bin/conda install -c conda-forge ncbi-datasets-cli"
