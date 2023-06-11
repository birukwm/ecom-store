FROM python:3.11

RUN ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
RUN echo "America/Los_Angeles" > /etc/timezone

RUN mkdir /automation
WORKDIR /automation
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY . .

WORKDIR /automation/ecom_store
ENTRYPOINT ["python3", "-m", "pytest", "tests"]