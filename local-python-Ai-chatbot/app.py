import streamlit as st
import ollama

# Page setup
st.set_page_config(page_title="Ollama Chatbot", page_icon="🤖", layout="wide")

st.title("🤖 AI Chatbot (Ollama)")

# --- Chat State ---
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Models
model_options = ["llama2", "mistral"]

if "model_choice" not in st.session_state or st.session_state["model_choice"] not in model_options:
    st.session_state["model_choice"] = "llama2"

# --- Layout with two columns ---
left_col, right_col = st.columns([1, 3])

with left_col:
    st.subheader("options")
    st.session_state["model_choice"] = st.selectbox(
        "Choose Model",
        model_options,
        index=model_options.index(st.session_state["model_choice"])
    )

    # Styled Clear button
    clear_style = """
        <style>
        div[data-testid="stButton"] button {
           background-color: #d4f8d4;  /* Black button */
            color: black;                /* White text */
            border: none;
            padding: 0.6rem 1.2rem;
            border-radius: 10px;
            font-weight: bold;
            width: 100%;
            transition: 0.3s ease;
        }
        div[data-testid="stButton"] button:hover {
            background-color: #333333;   /* Dark gray on hover */
            color: #00ffcc;              /* Neon green text hover */
            transform: scale(1.02);      /* Slight zoom */
        }
        </style>
    """
    st.markdown(clear_style, unsafe_allow_html=True)

    if st.button("Clear Chat"):
        st.session_state["messages"] = []
        st.rerun()

with right_col:
    # --- Chat Bubble Styles ---
    bubble_style = """
        <style>
        .chat-bubble {
            padding: 0.7rem 1rem;
            border-radius: 15px;
            margin: 0.3rem 0;
            max-width: 70%;
            word-wrap: break-word;
            font-size: 0.95rem;
        }
        .user-bubble {
           background-color: #d4e9ff; /* light gray instead of blue */
            color: black;
            margin-left: auto;
            text-align: right;
        }
        .assistant-bubble {
            background-color: #2f2f2f;
            color: white;
            margin-right: auto;
            text-align: left;
        }
        </style>
    """
    st.markdown(bubble_style, unsafe_allow_html=True)

    # --- Display Chat with bubbles ---
    for msg in st.session_state["messages"]:
        role_class = "user-bubble" if msg["role"] == "user" else "assistant-bubble"
        st.markdown(f'<div class="chat-bubble {role_class}">{msg["content"]}</div>', unsafe_allow_html=True)

    # Input box at bottom
    user_input = st.chat_input("Type your message...")

    if user_input:
        # Add user bubble immediately
        st.session_state["messages"].append({"role": "user", "content": user_input})

        # Create a placeholder for assistant streaming
        placeholder = st.empty()
        streamed_reply = ""

        # Stream response
        stream = ollama.chat(
            model=st.session_state["model_choice"],
            messages=st.session_state["messages"],
            stream=True
        )
        for chunk in stream:
            if "message" in chunk and "content" in chunk["message"]:
                streamed_reply += chunk["message"]["content"]
                # Update the assistant bubble live
                placeholder.markdown(
                    f'<div class="chat-bubble assistant-bubble">{streamed_reply}</div>',
                    unsafe_allow_html=True
                )

        # Save assistant reply
        st.session_state["messages"].append({"role": "assistant", "content": streamed_reply})
        st.rerun()
