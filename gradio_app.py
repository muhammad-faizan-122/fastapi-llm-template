import gradio as gr
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    openai_api_key=os.environ["API_KEY"],
    temperature=float(os.environ["TEMPERATURE"]),
    model=os.environ["MODEL_NAME"]
)


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


# Create a Gradio interface
inputs = gr.Textbox(lines=5, label="Enter Arabic text:", rtl=True)
outputs = gr.Textbox(label="Extracted Information:", rtl=True)

title = "Arabic Information Extractor"
description = "Enter Arabic text and get the extracted information about skills and requirements."

app = gr.Interface(
    fn=extract_arabic_info, 
    inputs=inputs, 
    outputs=outputs, 
    title=title, 
    description=description)

if __name__ == "__main__":
    app.launch(share=True)
