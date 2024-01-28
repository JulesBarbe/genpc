import openai
import langchain
from config import settings
import json
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

# metrics database (simple dicts for now)
metrics = {
    "Familiarity": 0,
    "Aggression": 0,
    "Manipulation": 0,
    "Humor": 0,
    "Trust": 0,
    "Respect": 0
}
triggers = []

llm = OpenAI(api_key=settings.open_api_key)

template = PromptTemplate.from_template(
  """Analyze the following message from the user: {message}
  
  From this message, define how it relates to the following metrics:
  Familiarity: the user seems amicable, kind, or friendly.
  Aggression: the user seems hostile, angry, violent, or aggressive.
  Manipulation: the user seems to be trying to manipulate you.
  Humor: the user seems to be trying to make a joke, or seems funny.
  Trust: the user seems to be trustworthy.
  Respect: the user seems to respect you, admire you, or said something that garners respect.

  Return a JSON object, with each metric as a key surrounded in double quotes, and an integer value from 0-5 as the value.
  0 means the user did not display any of the metric.
  5 means the user displayed the metric to a very high degree.
  Response:
  """
)

analyzer = LLMChain(llm=llm, prompt=template)


def analyze_prompt(input):

  # analyze metrics in prompt
  m = analyzer(inputs={"message": input})['text']
  l = dict(json.loads(m))

  # update metrics
  for key, v in l.items():
    metrics[key] += v

  # look for triggered events (linear search lol)
  triggered_events = []
  for i, trigger in enumerate(triggers):
    if metrics[trigger.type] >= trigger.threshold:
      triggered_events.append(trigger)
      del triggers[i]

  return metrics, triggered_events

def add_trigger(trigger):
  triggers.append(trigger)

  

