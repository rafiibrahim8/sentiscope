FROM python:3.11-bullseye
RUN apt-get update && apt-get install -y supervisor git-lfs
RUN mkdir /log
COPY . /sentiscope
WORKDIR /sentiscope
RUN pip install -r requirements.txt
RUN sh -c "cd model && git lfs install && git clone https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis"
EXPOSE 5000
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/sentiscope/supervisord.conf"]
