FROM tikhonovapolly/phigaro:latest
RUN bin/bash -c "/root/miniconda3/bin/pip install phigaro --upgrade"
RUN bin/bash -c "/root/miniconda3/bin/conda install -c conda-forge ncbi-datasets-cli --yes"
RUN bin/bash -c "/root/miniconda3/bin/conda install -c bioconda blast --yes"
RUN apt-get update && apt-get install -y unzip vim
RUN touch /root/accessions.txt
ADD main.py /root/

