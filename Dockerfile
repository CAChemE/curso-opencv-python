FROM andrewosh/binder-base

MAINTAINER Raymond Speth <speth@mit.edu>

USER root

RUN apt-get install -y libgtk2.0-0
RUN conda install -n python3 -c menpo opencv3=3.1

USER main
