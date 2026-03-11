
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="gpt-5.2", openai_api_key=openai_api_key, openai_api_base="https://aigc789.top/v1")
    chain = ConversationChain(llm = model, memory = memory)

    response = chain.invoke({"input": prompt})
    return response["response"]

memory = ConversationBufferMemory(return_messages = True)
# print(get_chat_response("牛顿提供那些之名定律", memory, "sk-jQC9dqBMFtCm8wc9r0TgqWNkAoE6luk6o6cE2WK3zHXoKRvs"))

