FROM python:3.10-bullseye

WORKDIR /bot

COPY . .

RUN python -m pip install -r requirements.txt

WORKDIR /bot

ENTRYPOINT [ "python", "bot.py" ]