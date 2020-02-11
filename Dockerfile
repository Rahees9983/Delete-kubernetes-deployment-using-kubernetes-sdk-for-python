# FROM python:slim
FROM python:3.6-slim
RUN apt upgrade
RUN apt update
RUN pip3 install flask
RUN pip3 install kubernetes

WORKDIR  /pvc_deploy_file
COPY  . /pvc_deploy_file

# COPY  . /data/get_deployment_files
# WORKDIR  /data/get_deployment_files

EXPOSE  5778
CMD [ "python3","for_k8s_delete_dploy.py" ]