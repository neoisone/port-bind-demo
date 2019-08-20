FROM rhel7:latest
RUN yum install python -y
COPY example-application.py /opt/example-application.py
CMD python /example-application.py

