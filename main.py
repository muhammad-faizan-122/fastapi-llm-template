from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from pydantic import BaseModel
import os
from fastapi import FastAPI

load_dotenv()

app = FastAPI()
# TODO: set parameter according to your own use-case
llm = ChatOpenAI(
    openai_api_key=os.environ["API_KEY"],
    temperature=os.environ["TEMPERATURE"],
    model=os.environ["MODEL_NAME"]
    )

# TODO: Update following your own case by adding your input key-value pair
class ArabicTextInfo(BaseModel):
    arabic_text: str


# TODO: update the prompt, inputs for use-case
def extract_arabic_info(arabic_text):
    """
    Extract arabic information from input arabic text.

    Parameters:
    - arabic_text (str): Job description text in arabic language.

    Returns:
    - response (str): Extracted skill or requirements for input arabic job description in arabic language.
    """

    prompt = PromptTemplate(
        input_variables=["arabic_text"],
        template="""
        You are an expert Arabic language information extractor. Your task is to extract the skills and requirements for the job from the given Arabic input text and return the output information in Arabic.
        Arabic input text: ```{arabic_text}```
        """
    )

    llm_chain = LLMChain(llm=llm, prompt=prompt, verbose=False)
    response = llm_chain.run(arabic_text=arabic_text)

    return response

@app.post("/extract_arabic_info/")
async def post_extract_arabic_info(arabic_text: ArabicTextInfo):
    """
    Endpoint to extract Arabic information from input Arabic text.

    Parameters:
    - arabic_text (str): Job description text in Arabic language.

    Returns:
    - response (str): Extracted skills or requirements for the input Arabic job description in Arabic language.
    """
    arabic_info_dict = arabic_text.model_dump()
    response = extract_arabic_info(arabic_info_dict['arabic_text'])
    
    return response
