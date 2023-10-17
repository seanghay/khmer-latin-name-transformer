FROM python:3.9
RUN pip install --no-cache-dir pynini
RUN pip install --no-cache-dir khmer-latin-name-transformer
RUN python -c "import pynini"

WORKDIR /app

COPY entrypoint.py .

ENTRYPOINT [ "python", "entrypoint.py" ]