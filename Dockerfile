FROM ubuntu
MAINTAINER Bhargava
USER root
WORKDIR .
COPY odbm.py .
RUN apt-get update \
   && apt-get install -y python3 pip \
   && pip install requests omdbapi pprintpp
ENTRYPOINT ["python3", "odbm.py"]

  