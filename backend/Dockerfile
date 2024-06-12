# Usa la imagen base de Ubuntu 22.04
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

# Actualiza el índice de paquetes e instala los paquetes necesarios
RUN apt-get update


# Actualiza el índice de paquetes nuevamente
RUN apt-get update

# Instala los paquetes necesarios (incluyendo OpenStack y FastAPI)
RUN apt-get install -y \
    python3-pip \
    && pip3 install fastapi uvicorn 

# RUN apt-get install -y docker.io


#CMD ["bash", "-c", "tail -f /dev/null"]

# Copiar los archivos de tu aplicación (si los tienes) al contenedor
# COPY . /app

# Comando para iniciar tu aplicación FastAPI (si tienes uno)
WORKDIR /project


### OPENSTACK
# Instala las dependencias necesarias
ENV USER=root

RUN apt-get update && \
    apt-get install -y \
        git \
        python3-dev \
        libffi-dev \
        gcc \
        libssl-dev \
        python3-venv \
        sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Crea un directorio de trabajo
WORKDIR /project

# Clona los repositorios de Kolla Ansible
RUN git clone --branch master https://opendev.org/openstack/kolla-ansible

# Crea y activa el entorno virtual
RUN python3 -m venv opendev && \
    /bin/bash -c "source ./opendev/bin/activate"

# Actualiza pip dentro del entorno virtual
RUN /bin/bash -c "pip install -U pip"

# Instala Ansible Core dentro del entorno virtual
RUN /bin/bash -c "pip install 'ansible-core>=2.15,<2.16.99'"

# Instala Ansible en el sistema
RUN apt-get update && \
    apt-get install -y ansible && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clona el repositorio Kolla Ansible y lo instala
RUN pip install ./kolla-ansible

# Configura Kolla Ansible
RUN mkdir -p /etc/kolla && \
    chown -R $USER:$USER /etc/kolla && \
    cp -r kolla-ansible/etc/kolla/* /etc/kolla && \
    cp kolla-ansible/ansible/inventory/* .

# Genera las contraseñas
RUN cd kolla-ansible/tools && \
    python3 ./generate_passwords.py

COPY globals.yml /etc/kolla/

RUN kolla-ansible install-deps

RUN cd kolla-ansible/tools && \
    sudo ./kolla-ansible -i ../../all-in-one bootstrap-servers

RUN kolla-ansible -i ../../all-in-one prechecks

RUN kolla-ansible -i ../../all-in-one deploy

RUN pip install python-openstackclient -c https://releases.openstack.org/constraints/upper/master

RUN cd kolla-ansible/tools && \
    ./kolla-ansible post-deploy

RUN kolla-ansible/tools/init-runonce

#CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]

CMD ["/usr/sbin/sshd", "-D"]
