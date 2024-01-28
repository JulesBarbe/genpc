## Inspiration
As a video game lover and someone that's been working with Gen AI and LLMs for a while, I really wanted to see what combining both in complex and creative ways could lead to. I truly believe that not too far in the future we'll be able to explore worlds in RPGs where the non-playable-characters feel immersively alive, and part of their world. Also I was sleep-deprived and wanted to hack something silly :3

## What it does
I leveraged generative AI (Large Language Models), as well as Vector Stores and Prompt Chaining to 'train' an NPC without having to touch the model itself. Everything is done in context, and through external memory using the Vector Store. Furthermore, a seperate model is concurrently analyzing the conversation as it goes to calculate conversation metrics (familiarity, aggresivity, trust, ...) to trigger events and new prompts dynamically! Sadly there is no public demo for it, because I didn't want to force anyone to create their own api key to use my product, and the results just wouldn't be the same on small hostable free tier llms.

## How we built it
For the frontend, I wanted to challenge myself and not use any framework or library, so this was all done through good-old html and vanilla JS with some tailwind here and there. For the backend, I used the Python FastAPI framework to leverage async workflows and websockets for token streaming to the frontend. I use OpenAI models combined together using Langchain to create complex pipelines of prompts that work together to keep the conversation going and update its course dynamically depending on user input. Vector Stores serve as external memory for the LLM, which can query them through similarity search (or other algorithms) in real time to supplement its in-context conversation memory through two knowledge sources: 'global' knowledge, which can be made up of thousands of words or small text documents, sources that can be shared by NPCs inhabiting the same 'world'. These are things the NPC should know about the world around them, its history, its geography, etc. The other source is 'local' knowledge, which is mostly unique to the NPC: personal history, friends, daily life, hobbies, occupations, etc. The combination of both, accessible in real time, and easily enhanceable through other LLMs (more on this in 'what's next) leads us to a chatbot that's been essentially gaslit into a whole new virtual life! Furthermore, heuristically determined conversation 'metrics' are dynamically analyzed by a separate llm on the side, to trigger pre-determined events based on their evolution. Each NPC can have pre-set values for these metrics, along with their own metric-triggered events, which can lead to complex storylines and give way to cool applications (quest giving, ...)

## Challenges we ran into
I wanted to do this project solo, so I ran out of time on a few features. The token streaming for the frontend was somehow impossible to make work correctly. It was my first time coding a 'raw' API like this, so that was also quite a challenge, but got easier once I got the hang of it. I could say a similar thing for the frontend, but I had so much fun coding it that I wouldn't even count it as a challenge!
Working with LLM's is always quite a challenge, as trying to get correctly formatted outputs can be compared to asking a toddler 

## Accomplishments that we're proud of
I'm proud of the idea and the general concept and design, as well as all the features and complexities I noted down that I couldn't implement! I'm also proud to have dedicated so much effort to such a useless, purely-for-fun scatter-brained 3-hours-of-sleep project in a way that I really haven't done before. I guess that's the point of hackathons! Despite a few things not working, I'm proud to have architectured quite a complex program in very little time, by myself, starting from nothing but sleep-deprivation-fueled jotted-down notes on my phone.

## What we learned
I learned a surprising amount of HTML, CSS and JS from this, elements of programming I always pushed away because I am a spoiled brat. I got to implement technologies I hadn't tried before as well, like Websockets and Vector Stores. As with every project, I learned about feature creep and properly organising my ideas in a way that something, anything can get done. I also learned that there is such a thing as too much caffeine, which I duely noted and will certainly regret tonight.

## What's next for GENPC
There's a lot of features I wanted to work on but didn't have time, and also a lot of potential for future additions. One I mentioned earlier is too automatically extend global or local knowledge through a separate LLM: given keywords or short phrases, a ton of text can be added to complement the existing data and further fine-tune the NPC.
There's also an 'improvement mode' I wanted to add, where you can directly write data into static memory through the chat mode. I also didn't have time to completely finish the vector store or conversation metric graph implementations, although at the time I'm writing this devpost I still have 2 more hours to grind >:)
There's a ton of stuff that can arise from this project in the future: this could become a scalable web-app, where NPCs can be saved and serialized to be used elsewhere. Conversations could be linked to voice-generation and facial animation AIs to further boost the immersiveness. A ton of heuristic optimizations can be added around the metric and trigger systems, like triggers influencing different metrics. The prompt chaining itself could become much more complex, with added layers of validation and analysis. The NPCs could be linked to other agentic models and perform complex actions in simulated worlds!

## Dependencies:
- OpenAI with API key
- Langchain
- FastAPI, uvicorn 
- aiofiles 
- qdrant-client (async vectorstore)
- pydantic-settings
