

---

## 🧠 `prompts.py`

```python
from langchain.prompts import PromptTemplate

resume_match_template = """
You are an intelligent Resume Matcher Bot.

Compare the following RESUME with the JOB DESCRIPTION.

Please provide:
1. Whether the resume is a good match (Yes/No)
2. Key matching skills or experiences
3. Skills or experience gaps
4. Suggestions to improve the resume for this role
5. Match score out of 100

Respond in a clear, structured format.

RESUME:
{resume}

JOB DESCRIPTION:
{job}
"""

resume_match_prompt = PromptTemplate(
    input_variables=["resume", "job"],
    template=resume_match_template
)
