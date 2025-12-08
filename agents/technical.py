from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b", api_key=os.getenv("GROQ_API_KEY"))


# ---------- Technical Node ----------
def technical_llm(state):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a technical support bot. Help the user with their technical issues."),
        ("user", "Issue: {Issue}")
    ])

    chain = prompt | llm
    user_msg = state["messages"][-2].content
    response = chain.invoke({"Issue": user_msg})

    return {"messages": state["messages"] + [response]}