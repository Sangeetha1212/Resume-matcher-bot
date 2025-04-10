import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load API key
os.environ["OPENAI_API_KEY"] = "your-api-key-here"

# Load resume and job description
with open("examples/resume.txt", "r") as f:
    resume = f.read()

with open("examples/job_description.txt", "r") as f:
    job_description = f.read()

# Prompt
template = """
You are a Resume Matcher Bot. Compare the following resume to the job description and do the following:
- State whether the resume is a good match
- Identify key strengths
- Identify skill gaps or mismatches
- Provide suggestions to improve the resume
- Rate the overall match out of 100

Resume:
{resume}

Job Description:
{job}
"""

prompt = PromptTemplate(
    input_variables=["resume", "job"],
    template=template
)

llm = ChatOpenAI(temperature=0.3, model_name="gpt-3.5-turbo")

chain = LLMChain(llm=llm, prompt=prompt)

result = chain.run({"resume": resume, "job": job_description})

print("\n📋 Match Report:\n")
print(result)
