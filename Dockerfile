FROM python:3
RUN echo "Début \n"

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot
RUN pip install discord

COPY . .

CMD [ "python3" , "DiscordBot.py" ]