FROM ubuntu:22.04

RUN mkdir /prj

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC \
    apt-get install -y \
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-extra \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /prj
ENTRYPOINT [ "pdflatex" ]
