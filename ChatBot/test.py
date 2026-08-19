from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen3-0.6B",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
        max_length=None,
    ),
)

chat_model = ChatHuggingFace(llm=llm)

ai_chat= chat_model.invoke("who is pm of india ?")

print(ai_chat.content)