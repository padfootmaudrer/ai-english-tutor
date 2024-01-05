from dotenv import find_dotenv, load_dotenv
from secret_key import huggingface_api_key,openai_api_key
import os
from openai import OpenAI

os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingface_api_key
os.environ["OPENAI_API_KEY"] = openai_api_key

load_dotenv(find_dotenv())

client = OpenAI()

repo_id = 'gpt-3.5-turbo'
def get_completion(input_text, model=repo_id):
    messages = [{"role": "user", "content": get_prompt(input_text)}]
    response = client.chat.completions.create(model=model,
    messages=messages,
    temperature=0)
    return response.choices[0].message.content

def get_prompt(input_text):
  prompt = f"""proof read this text: ```{input_text}``` 

  Summarize the analysis on the basis of Grammar and Syntax, Vocabulary and Language Use, \
  Comprehension and Responsiveness, Content and Structure and Creativity and Originality. \

  For each parameter respond in a JSON structure, give marks out of 10 and suggestion on how to improve it.
  """
  return prompt