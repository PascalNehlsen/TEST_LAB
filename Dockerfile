# Use an official Python runtime as a parent image
FROM python:3.9-slim

ARG PASSWORD="changeme"
ARG PORT=2222

ENV PASSWORD=${PASSWORD} \
    PORT=${PORT}

# Install OpenSSH server
RUN apt-get update && \
    apt-get install -y openssh-server && \
    mkdir /var/run/sshd

# Create user Vik and set password
RUN useradd -m -s /bin/bash Vik && \
    echo "Vik:${PASSWORD}" | chpasswd

# Allow Vik login and password authentication
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i "s/#Port 22/Port ${PORT}/" /etc/ssh/sshd_config

# Expose SSH port
EXPOSE ${PORT}

# Start the SSH service
CMD ["/usr/sbin/sshd", "-D"]
