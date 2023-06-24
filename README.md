![test-workflow]

# sentiscope
A simple sentiment analysis API made with Flask.

## Getting started
The best way to run this project is with Docker. If you don't have Docker, you can run it without Docker, but you will need to install the dependencies manually.

### Run with Docker

```bash
docker-compose up
```
Don't have Docker? [Install it](https://docs.docker.com/get-docker/).

### Run without Docker
It is highly recommended to use a virtual environment to run this project without Docker. You can use [venv](https://docs.python.org/3/library/venv.html) or [virtualenv](https://virtualenv.pypa.io/en/latest/).

Install the dependencies:

```bash
pip install -r requirements.txt
```
Run the server:

```bash
flask run
```
or
```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

## Sending requests
You need to send a POST request to the `/api/v1/analyze` endpoint with a JSON body containing the text you want to analyze. The response will be a JSON with the sentiment score and the sentiment label.

Here's an example using cURL:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "I love this project!"}' http://localhost:5000/api/v1/analyze
```

## Running tests

```bash
python -m unittest -v
```

## Downloading the model
The model used in this project is [finiteautomata/bertweet-base-sentiment-analysis](https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis). The project will download the model automatically when you run it. But if you want to download it manually, say, to use it in another project, or not depending on cached files, you can download the model in the `model` directory. The application will look for the model in the `model` directory first, and if it doesn't find it, it will download/use the cached model.

```bash
cd model
git clone https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis
```

Note that you need to have [git-lfs](https://git-lfs.github.com/) installed to download the model.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[test-workflow]: https://github.com/rafiibrahim8/sentiscope/actions/workflows/test.yml/badge.svg
