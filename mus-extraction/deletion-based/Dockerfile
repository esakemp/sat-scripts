
FROM ubuntu:16.04
RUN apt-get update && apt-get install -y --no-install-recommends \
	python-dev \
	python-pip \
	build-essential libssl-dev libffi-dev \
	libxml2-dev libxslt1-dev zlib1g-dev \
	&& \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

RUN pip install python-sat
COPY . .
CMD ./mus-extractor.sh