FROM continuumio/miniconda3:latest
ADD mlflow /mlflow
RUN conda env create -f /mlflow/environment.yml
EXPOSE 8888 5000
#ENTRYPOINT ["mlflow/run.sh"]
CMD ["/bin/bash"]