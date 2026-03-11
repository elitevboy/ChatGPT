
import streamlit as st
from utils import get_chat_response
from langchain.memory import ConversationBufferMemory

# 必须在任何其他 Streamlit 命令之前调用
# st.set_page_config(
#     page_title="GPT知识问答AI助手",      # 浏览器标签页标题
#     menu_items={
#         'Get Help': None,      # 隐藏"帮助"
#         'Report a bug': None,  # 隐藏"报告错误"
#         'About': None          # 隐藏"关于"
#     },
#     page_icon="💬",                # 浏览器标签页图标（可选）
#     layout="wide",                 # 页面布局：'centered' 或 'wide'
#     initial_sidebar_state="expanded"  # 侧边栏初始状态
# )
#
# # 隐藏右上角菜单按钮
# hide_menu_style = """
#     <style>
#     #MainMenu {visibility: hidden;}           /* 隐藏三个点菜单 */
#     header {visibility: hidden;}              /* 隐藏整个顶部栏（可选） */
#     footer {visibility: hidden;}              /* 隐藏底部"Made with Streamlit" */
#     </style>
# """
# st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("🚀GPT知识问答AI助手")

openai_api_key = "sk-jQC9dqBMFtCm8wc9r0TgqWNkAoE6luk6o6cE2WK3zHXoKRvs"

# with st.sidebar:
#     openai_api_key = st.text_input("请输入OpenAI API Key：", type="password")
#     st.markdown("[获取OpenAI API key](https://platform.openai.com/account/api-keys)")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai", "content": "你好，我是你的AI助手，有什么可以帮你的吗？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("请输入你的OpenAI API Key")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中，请稍候..."):
        response = get_chat_response(prompt, st.session_state["memory"], openai_api_key)
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)

