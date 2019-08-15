FROM rhel
RUN yum install python -y
COPY example-application.py /example-application.py
CMD python /example-application.py

