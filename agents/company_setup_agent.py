from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from utils.model_loader import load_solvio_llm

def get_company_setup_chain():
    with open("prompts/company_setup.txt", "r", encoding="utf-8") as f:
        template = f.read()

    prompt = PromptTemplate(
        input_variables=["question"],
        template=template
    )

    llm = load_solvio_llm()

    return LLMChain(llm=llm, prompt=prompt)
