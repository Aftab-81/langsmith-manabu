from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv()

os.environ["LANGCHAIN_PROJECT"] = "Sequential LLM App"

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)


llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    task="text-generation",
    max_new_tokens = 1024
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

config = {
    "run_name": "Sequential Chain", # On LangSmith Dashboard instead of RunnableSequence -> Sequential Chain
    "tags": ["text generation", "summarization", "natural language understanding"],
    "metadata": {
        "parser": "StrOutputParser",
        "model": "DeepSeek",
        "workflow": "sequential"
    }
}

result = chain.invoke({'topic': 'Unemployment in India'}, config = config)

print(result)
