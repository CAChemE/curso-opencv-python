FROM andrewosh/binder-base

MAINTAINER FJ Navarro <fj.navarro[a]ua.es>

USER root

RUN apt-get update
RUN apt-get install -y libgtk2.0-common
RUN conda create -n pyOCV python==3.5.0 
RUN /bin/bash -c "source activate pyOCV && conda install -c menpo opencv3=3.1"

USER main
