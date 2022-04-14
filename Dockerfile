FROM mcr.microsoft.com/playwright
WORKDIR /code
RUN apt-get -y update
RUN apt-get -y install python3 python3-pip
RUN pip3 install nextcord TikTokApi python-dotenv nest-asyncio
COPY . .
CMD ["python3", "./bot.py"]