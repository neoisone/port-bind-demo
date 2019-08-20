FROM registry.access.redhat.com/rhel7:latest
# RUN yum install python -y
COPY example-application.py /opt/example-application.py
RUN setcap 'cap_net_bind_service=+ep' /opt/example-application.py
CMD python /opt/example-application.py

