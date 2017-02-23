FROM andrewosh/binder-base

MAINTAINER FJ Navarro <fj.navarro[a]ua.es>

USER root

RUN apt-get install -y libgtk2.0-0
RUN conda install -n python3 -c menpo opencv3=3.1

USER main
