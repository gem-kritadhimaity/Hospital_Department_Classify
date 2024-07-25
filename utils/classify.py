from langchain import PromptTemplate, LLMChain

import config as cf

# Initialize the prompt template
prompt = PromptTemplate(
    input_variables=["input"],
    template=cf.prompt_template
)

llm_chain = LLMChain(prompt=prompt, llm=cf.llm)

def classify_department(symptoms):
    input_symptoms = symptoms
    # print(input_text)
    result = llm_chain.run(input=input_symptoms)
    # print("Checking result: ", result)
    return result