# AI-Chatbot
An AI Chatbot build using OpenAI APIs

## Clone Repository
```
git clone https://github.com/shadabshaukat/AI-Chatbot.git

cd AI-Chatbot/
```

## Edit the .env file and Add your GPT model and OpenAI API Key

vim .env

```
OPENAI_API_KEY=Paste-Your-OpenAI-API-Key

OPENAI_MODEL=gpt-3.5-turbo
```

## Build the Container Image

```
docker build -t my-ai-chatbot-app .
```

## Run the Container

```
docker run -d -p 8000:8000 --env-file .env my-ai-chatbot-app
```

## Open AI Chatbot from Browser

http://localhost:8000/static/index.html


<img width="822" alt="Screenshot 2024-04-08 at 3 26 42 pm" src="https://github.com/shadabshaukat/AI-Chatbot/assets/39692236/85312674-09fe-4a6c-a72a-ce6171533b59">


## Check Status of the Container
```
docker container ls

docker logs container_id

docker inspect container_id

docker stats container_id

docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_id
```

