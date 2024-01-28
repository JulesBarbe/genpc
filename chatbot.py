import openai
import langchain
from config import settings
from openai import ChatCompletion
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

llm = OpenAI(api_key=settings.open_api_key)


# $ := dev prompt
# % := user input
# Instructs llm on what information he can relay, and how to respond to prompts down the line
base_prompt = """You are an actor. From now on, there will be two types of prompt you receive.
Prompts starting with $ are prompts that you should not relay to the user. These indicate the manner in which you need to respond in the future.
Prompts starting with % are from the user. These are the prompts you should respond to in accordance with the $ prompts you received before.
You cannot relay any information from the user that you have no learned, directly or indirectly, from $ prompts.
From now on, you will only respond to % prompts in the FIRST PERSON. Keep your answers under 100 characters, and only include letters and numbers.
"""

morshu = "Morshu is the owner of the general store in the Goronu area of Koridai. His shop sits at the base of the valley pass, atop a small bridge next to a rapid waterfall. Should Link interact with him, he will name the wares he sells, Lantern Oil, Ropes, and Bombs, and inform Link that he can have them should he have the money to pay for them. Should Link not have enough rubies, he will tell him to come back when he is richer. "

# make chain from baseprompt + local template
localTemplate = PromptTemplate.from_template(
  """
  {base_prompt}
  ${local_prompt}
  %{user_prompt}
  """
)
localChain = LLMChain(llm=llm, prompt=localTemplate)

# def stream_response(prompt: str):
#     # TODO: use vector store chain retriever
#     for chunk in client.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=prompt,
#         stream=True,
#     ):
#         content = chunk["choices"][0].get("delta", {}).get("content")
#         if content is not None:
#             print("CONTENT", content)
#             yield content

def get_response(message):
  #TODO: include vector store query, retriever chain
  # prompt = localTemplate.format(base_prompt=base_prompt, local_prompt=morshu, user_prompt=message)
  return localChain.stream(input={"base_prompt": base_prompt, "local_prompt": morshu, "user_prompt": message})



