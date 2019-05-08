FROM wataken44/ubuntu-latest-sshd
LABEL maintainer "%user%"

ENV DOCKER "YES"
ENV LANG C.UTF-8

RUN set -xe \
    && apt update -y \
    && apt dist-upgrade -y \
    && apt install -y git-core

USER ubuntu

RUN set -xe \
    && cd /home/ubuntu/ \
    && git clone https://github.com/%user%/%repo%
    
USER root

EXPOSE 22
CMD  service ssh start && tail -f /dev/null
